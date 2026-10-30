param(
	[string]$OutputDir = "output",
	[switch]$SkipPdf,
	[string]$PdfEngine = "xelatex",
	[string]$MainFont = "DejaVu Serif",
	[string]$MonoFont = "DejaVu Sans Mono",
	[switch]$NoPdfLogs
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-ScriptRoot {
	if ($PSScriptRoot) {
		return $PSScriptRoot
	}

	return Split-Path -Parent $MyInvocation.MyCommand.Path
}

function Resolve-RequiredFiles {
	param(
		[string]$RootPath,
		[string[]]$RelativePaths
	)

	$resolved = New-Object System.Collections.Generic.List[string]

	foreach ($relativePath in $RelativePaths) {
		$fullPath = Join-Path $RootPath $relativePath
		if (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
			throw "Missing required file: $relativePath"
		}

		$resolved.Add($fullPath)
	}

	return $resolved
}

function New-CombinedMarkdown {
	param(
		[string[]]$SourceFiles,
		[string]$OutputFile,
		[string]$RootPath,
		[switch]$NormalizeHeadingLinks
	)

	$builder = New-Object System.Text.StringBuilder

	for ($index = 0; $index -lt $SourceFiles.Count; $index++) {
		$sourceFile = $SourceFiles[$index]
		$relative = [System.IO.Path]::GetRelativePath($RootPath, $sourceFile).Replace("\\", "/")
		$content = Get-Content -LiteralPath $sourceFile -Raw

		if ($NormalizeHeadingLinks) {
			# Pandoc auto-identifiers omit numeric list prefixes, so links like
			# (#1-heading-title) should become (#heading-title) for PDF builds.
			$content = [System.Text.RegularExpressions.Regex]::Replace(
				$content,
				"\(#([^)]+)\)",
				{
					param($match)
					$anchor = $match.Groups[1].Value
					$anchor = [System.Text.RegularExpressions.Regex]::Replace($anchor, "^[0-9]+-", "")
					$anchor = [System.Text.RegularExpressions.Regex]::Replace($anchor, "-+", "-")
					return "(#$anchor)"
				},
				[System.Text.RegularExpressions.RegexOptions]::Multiline
			)
		}

		# Replace glyphs that are not supported by the configured PDF mono font.
		$content = $content.Replace("[x]", "[OK]")

		[void]$builder.AppendLine("<!-- Source: $relative -->")
		[void]$builder.AppendLine($content.TrimEnd())

		if ($index -lt ($SourceFiles.Count - 1)) {
			[void]$builder.AppendLine()
			[void]$builder.AppendLine("\\newpage")
			[void]$builder.AppendLine()
		}
	}

	[System.IO.File]::WriteAllText($OutputFile, $builder.ToString(), [System.Text.UTF8Encoding]::new($false))
}

function New-PdfFromMarkdown {
	param(
		[string]$MarkdownFile,
		[string]$PdfFile,
		[string]$Engine,
		[string]$BodyFont,
		[string]$CodeFont,
		[string]$LogFile
	)

	if ($LogFile) {
		$logDirectory = Split-Path -Parent $LogFile
		if (-not (Test-Path -LiteralPath $logDirectory)) {
			New-Item -Path $logDirectory -ItemType Directory | Out-Null
		}

		$startLog = @(
			"Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')",
			"Markdown: $MarkdownFile",
			"PDF: $PdfFile",
			""
		)
		[System.IO.File]::WriteAllLines($LogFile, $startLog, [System.Text.UTF8Encoding]::new($false))

		& pandoc $MarkdownFile `
			-o $PdfFile `
			--pdf-engine=$Engine `
			-V "mainfont=$BodyFont" `
			-V "monofont=$CodeFont" *>&1 | Tee-Object -FilePath $LogFile -Append | Out-Host

		$endLog = "Completed: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ExitCode=$LASTEXITCODE"
		Add-Content -LiteralPath $LogFile -Value $endLog
	}
	else {
		& pandoc $MarkdownFile `
			-o $PdfFile `
			--pdf-engine=$Engine `
			-V "mainfont=$BodyFont" `
			-V "monofont=$CodeFont"
	}

	if ($LASTEXITCODE -ne 0) {
		throw "Pandoc failed while creating: $PdfFile"
	}
}

function Write-PdfWarningSummary {
	param(
		[string[]]$LogFiles,
		[string]$SummaryFile
	)

	$warnings = New-Object System.Collections.Generic.List[string]

	foreach ($logFile in $LogFiles) {
		if (-not (Test-Path -LiteralPath $logFile -PathType Leaf)) {
			continue
		}

		$logWarnings = Select-String -Path $logFile -Pattern "\[WARNING\]" | ForEach-Object {
			$_.Line.Trim()
		}

		foreach ($warning in $logWarnings) {
			$warnings.Add($warning)
		}
	}

	$builder = New-Object System.Text.StringBuilder
	[void]$builder.AppendLine("PDF Warning Summary")
	[void]$builder.AppendLine("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
	[void]$builder.AppendLine()

	if ($warnings.Count -eq 0) {
		[void]$builder.AppendLine("No warnings were found in PDF logs.")
	}
	else {
		$grouped = $warnings | Group-Object | Sort-Object Count -Descending
		foreach ($group in $grouped) {
			[void]$builder.AppendLine(("{0}x {1}" -f $group.Count, $group.Name))
		}
	}

	[System.IO.File]::WriteAllText($SummaryFile, $builder.ToString(), [System.Text.UTF8Encoding]::new($false))
}

$root = Get-ScriptRoot
$outputPath = Join-Path $root $OutputDir

if (-not (Test-Path -LiteralPath $outputPath)) {
	New-Item -Path $outputPath -ItemType Directory | Out-Null
}

$logPath = Join-Path $outputPath "logs"
$runStamp = Get-Date -Format "yyyyMMdd_HHmmss"
$pdfLogFiles = New-Object System.Collections.Generic.List[string]

$curriculumMap = [ordered]@{
	"python" = @(
		"python/teachers-guide.md",
		"python/unit00-setup.md",
		"python/unit01-foundations.md",
		"python/unit02-numeric-computations.md",
		"python/unit03-control-flow.md",
		"python/unit04-06-data-functions.md",
		"python/unit07-09-oop-files.md",
		"python/unit10-11-projects-capstone.md"
	)
	"java" = @(
		"java/README.md",
		"java/teachers-guide.md",
		"java/unit00-01-setup-foundations.md",
		"java/unit02-04-io-control-arrays.md",
		"java/unit05-08-strings-methods-oop-files.md",
		"java/unit09-11-collections-projects.md"
	)
	"javascript" = @(
		"javascript/README.md",
		"javascript/teachers-guide.md",
		"javascript/unit00-01-setup-foundations.md",
		"javascript/unit02-04-io-control-data.md",
		"javascript/unit05-08-strings-functions-oop-files.md",
		"javascript/unit09-11-modules-collections-projects.md"
	)
}

$overallRelativeFiles = New-Object System.Collections.Generic.List[string]
$overallRelativeFiles.Add("README.md")

foreach ($language in $curriculumMap.Keys) {
	foreach ($relative in $curriculumMap[$language]) {
		$overallRelativeFiles.Add($relative)
	}
}

if (-not $SkipPdf) {
	if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
		throw "Pandoc is required unless -SkipPdf is specified."
	}
}

foreach ($language in $curriculumMap.Keys) {
	$languageFiles = Resolve-RequiredFiles -RootPath $root -RelativePaths $curriculumMap[$language]
	$languageMarkdown = Join-Path $outputPath ("{0}_curriculum.md" -f $language)
	$languagePdf = Join-Path $outputPath ("{0}_curriculum.pdf" -f $language)

	New-CombinedMarkdown -SourceFiles $languageFiles -OutputFile $languageMarkdown -RootPath $root -NormalizeHeadingLinks
	Write-Host "Created: $languageMarkdown"

	if (-not $SkipPdf) {
		$pdfLogFile = if ($NoPdfLogs) { $null } else { Join-Path $logPath ("pdf_{0}_{1}.log" -f $language, $runStamp) }
		if ($pdfLogFile) {
			$pdfLogFiles.Add($pdfLogFile)
		}

		New-PdfFromMarkdown `
			-MarkdownFile $languageMarkdown `
			-PdfFile $languagePdf `
			-Engine $PdfEngine `
			-BodyFont $MainFont `
			-CodeFont $MonoFont `
			-LogFile $pdfLogFile

		Write-Host "Created: $languagePdf"
	}
}

$overallFiles = Resolve-RequiredFiles -RootPath $root -RelativePaths $overallRelativeFiles
$overallMarkdown = Join-Path $outputPath "all_curricula.md"
$overallPdf = Join-Path $outputPath "all_curricula.pdf"

New-CombinedMarkdown -SourceFiles $overallFiles -OutputFile $overallMarkdown -RootPath $root -NormalizeHeadingLinks
Write-Host "Created: $overallMarkdown"

if (-not $SkipPdf) {
	$overallPdfLogFile = if ($NoPdfLogs) { $null } else { Join-Path $logPath ("pdf_all_curricula_{0}.log" -f $runStamp) }
	if ($overallPdfLogFile) {
		$pdfLogFiles.Add($overallPdfLogFile)
	}

	New-PdfFromMarkdown `
		-MarkdownFile $overallMarkdown `
		-PdfFile $overallPdf `
		-Engine $PdfEngine `
		-BodyFont $MainFont `
		-CodeFont $MonoFont `
		-LogFile $overallPdfLogFile

	Write-Host "Created: $overallPdf"

	if (-not $NoPdfLogs) {
		$summaryFile = Join-Path $logPath ("pdf_warning_summary_{0}.txt" -f $runStamp)
		Write-PdfWarningSummary -LogFiles $pdfLogFiles -SummaryFile $summaryFile
		Write-Host "Created: $summaryFile"
	}
}

Write-Host "Curriculum build complete."
