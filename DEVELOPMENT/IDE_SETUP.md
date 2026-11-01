# Standalone Lesson: Installing and Configuring a Development Environment

## Overview

A development environment is the set of tools used to create, run, test, and maintain programs. An integrated development environment (IDE) combines a source-code editor with tools such as project navigation, language support, diagnostics, debugging, extensions, and a terminal.

This lesson covers three IDE choices:

- **Visual Studio Code (VS Code):** the course's default recommendation.
- **VSCodium:** a community-built, telemetry-disabled distribution of the VS Code source code. The request's “Vicodin” is interpreted here as **VSCodium**.
- **Eclipse Theia IDE:** an open-source, extensible desktop IDE with a similar keyboard-oriented editor model.

The steps below establish a general workspace. A language curriculum must still explain how to install its own runtime, compiler, SDK, debugger, and language extension.

## Learning objectives

By the end of this lesson, learners should be able to:

- Distinguish an IDE from a text editor and from a compiler or interpreter.
- Install one supported IDE on their operating system.
- Open a project folder rather than editing isolated files in an unknown location.
- Configure and test keyboard and screen-reader access.
- Identify the editor, file explorer, command palette, integrated terminal, and diagnostics.
- Explain the trade-offs between an IDE and a lightweight text editor.
- Describe the course policy for AI-assisted features.

## Prerequisites

- A supported Windows, macOS, or Linux computer.
- Permission to install software, or assistance from an administrator.
- A keyboard and the learner's usual access technology (screen reader, braille display, magnification, or another input/output configuration).
- The preliminary [terminal skills course](../TERMINAL/TERMINAL_README.md).
- Internet access to download the selected application.

## Lesson 1: Choose an editor or IDE

### What is the difference?

A **text editor** edits text files. A **code editor** adds programming-oriented features such as syntax highlighting and indentation. An **IDE** usually adds a broader set of project, language, build, test, and debugging tools. The categories overlap: modern editors can become IDE-like through extensions.

A compiler or interpreter is a separate tool that translates or executes source code. Installing an IDE does not automatically install Python, Java, Node.js, .NET, Rust, or another language toolchain.

### Comparison

| Tool | Typical strengths | Trade-offs |
|---|---|---|
| VS Code | Broad language support, integrated terminal, extensions, debugging, diagnostics, project navigation, large user community | Many panels and commands; extension quality and accessibility vary; frequent suggestions can distract beginners |
| VSCodium | VS Code-derived editing experience, open-source binary distribution, telemetry disabled by default | Extension catalog differs; some Microsoft-published extensions and services may be unavailable or require extra configuration |
| Theia IDE | Open-source and extensible; desktop and hosted options; supports language tooling through extensions and language servers | Smaller ecosystem and community than VS Code; available extensions and screen-reader behavior can differ |
| Notepad++ | Lightweight Windows text editor, fast startup, simple interface, syntax highlighting | Not a full IDE; limited integrated debugging and project tooling |
| BBEdit | macOS text editor with strong text-processing and file-editing features | Not a full IDE; compiler, debugger, and project workflow are separate |
| Sublime Text | Fast, cross-platform editor with powerful navigation and extensibility | Some features require configuration or packages; commercial license; not a complete IDE by itself |
| Basic Linux text editor (for example, Gedit, Kate, Mousepad, or nano) | Low overhead, direct editing, useful for learning terminal and compiler workflows | Fewer integrated diagnostics, refactoring, completion, and debugging features; more work happens in the terminal |

### Advantages of an IDE

- Keeps editing, project files, terminal commands, diagnostics, and debugging in one application.
- Language extensions can provide completion, documentation lookup, linting, formatting, and error reporting.
- Project-wide search and navigation become useful as programs grow.
- Integrated debugging helps inspect program state and execution.
- A consistent editor can support several languages.

### Disadvantages of an IDE

- The interface can be complex and expose many controls that a beginner does not yet need.
- Screen-reader users may encounter changing focus, noisy announcements, inaccessible extension views, or poorly labeled controls.
- Automatic completion, code actions, templates, and generated project files can hide language details if introduced too early.
- Extensions can conflict, consume resources, or change behavior.
- IDE convenience can make it harder to understand the underlying compiler, interpreter, build command, and filesystem.

### Advantages of a lightweight text editor

- Fewer interface concepts to learn at the beginning.
- Encourages students to understand file extensions, directory structure, compiler/interpreter commands, and terminal output.
- Makes it easier to see the complete source file without project panels or pop-up tooling.
- Can be faster and more accessible for a learner whose screen reader works better with a simpler interface.

### Disadvantages of a lightweight text editor

- Students must run compilers, interpreters, tests, and debuggers separately.
- Diagnostics and completion may be absent or require manual setup.
- Navigating a large multi-file project is less convenient.
- Debugging and refactoring may require additional tools.

**Course recommendation:** teach the command line and the language toolchain regardless of editor choice. Use VS Code as the common documented environment, but allow VSCodium, Theia, or a text editor when it is more accessible or better suited to the learner. Do not grade students on which editor they use.

## Lesson 2: Install Visual Studio Code

### Official download

Use the official [Visual Studio Code download page](https://code.visualstudio.com/Download). Choose the build for the computer's operating system and processor architecture. Prefer the user installer on Windows unless an administrator needs to install it for all users.

### Windows

1. Open the official download page and select **Windows**.
2. Download the **User Installer** that matches the computer (usually x64; use ARM64 for an ARM-based Windows device).
3. Open the downloaded `.exe` installer.
4. Accept the license, retain the default destination unless the instructor specifies another location, and complete the installation.
5. Keep the option to add VS Code to PATH enabled if offered.
6. Launch **Visual Studio Code** from the Start menu.
7. Open the Command Prompt or PowerShell and run:

```powershell
code --version
```

If the command is not found, close and reopen the terminal. If it remains unavailable, launch VS Code from the Start menu and use **File → Open Folder** instead.

### macOS

1. Open the official download page and select **macOS**.
2. Choose the build matching the Mac's processor: Apple silicon (ARM64) or Intel (x64).
3. Open the downloaded `.zip` archive.
4. Move **Visual Studio Code.app** into the **Applications** folder.
5. Open it from Applications. If macOS asks for confirmation, verify that the application came from the official VS Code download before allowing it to open.
6. To enable the `code` terminal command, open the Command Palette and run **Shell Command: Install 'code' command in PATH** if that command is available in the installed version.
7. Open a new Terminal window and run `code --version`.

### Linux

1. Open the official [Linux installation instructions](https://code.visualstudio.com/docs/setup/linux).
2. Choose the package for the distribution: DEB for Debian/Ubuntu, RPM for Fedora/RHEL-compatible systems, or another supported package method.
3. Install the downloaded package using the distribution's software installer or the documented package-manager command.
4. Launch **Visual Studio Code** from the applications menu.
5. Open a terminal and run:

```bash
code --version
```

6. If the command is unavailable, check the package installation instructions for the distribution and confirm that the executable is on PATH.

### First-run configuration and accessibility

1. Start VS Code.
2. Open the Command Palette with **Ctrl+Shift+P** on Windows/Linux or **Command+Shift+P** on macOS.
3. Search for **Help: Open Accessibility Help** and review the context-specific guidance.
4. Enable Screen Reader Optimized Mode when prompted, or use the **Help: Toggle Screen Reader Accessibility Mode** command if available.
5. Open Settings and confirm that **Editor: Accessibility Support** is set to **on** if automatic detection does not work reliably. The corresponding setting is `editor.accessibilitySupport`.
6. Keep the screen reader running and test reading the editor line by line, moving by word and character, navigating headings and controls, and reading terminal output.
7. Use the keyboard to move between the editor, Explorer, Search, Extensions, Problems, and integrated terminal. Do not assume that a mouse-only tutorial is accessible.
8. Install only the language extension specified by the current language curriculum. Verify the extension publisher and compatibility before installation.

Official reference: [VS Code accessibility features](https://code.visualstudio.com/docs/configure/accessibility/accessibility).

## Lesson 3: Install VSCodium

VSCodium provides community-built binaries based on the VS Code source repository. It is not the Microsoft-branded VS Code distribution. Its defaults disable telemetry, and its extension marketplace configuration differs. Some extensions available in Microsoft's Marketplace may not be available through the default Open VSX registry.

Use the official [VSCodium installation page](https://vscodium.com/#install) or [VSCodium releases](https://github.com/VSCodium/vscodium/releases). Do not download installers from third-party download sites.

### Windows

1. Open the official VSCodium installation page.
2. If Windows Package Manager (winget) is installed, open PowerShell and run:

```powershell
winget install -e --id VSCodium.VSCodium
```

3. Alternatively, download the matching Windows User Installer from the official VSCodium releases page and run it.
4. Launch **VSCodium** from the Start menu.
5. Open a new PowerShell window and run:

```powershell
codium --version
```

6. If `codium` is not recognized, launch the application from the Start menu and check the installer/PATH configuration.

### macOS

1. Confirm whether the Mac uses Apple silicon or Intel.
2. If Homebrew is installed, run:

```bash
brew install --cask vscodium
```

3. Alternatively, download the matching official `.dmg` release and move VSCodium to Applications.
4. Launch VSCodium and test its keyboard and screen-reader behavior.
5. If the `codium` terminal command is unavailable, use the application's command palette or installation documentation to configure the command-line launcher.

### Linux

1. Open the official VSCodium installation page.
2. Choose a package appropriate to the distribution and architecture. Options include DEB, RPM, Snap, Flatpak, or a release archive.
3. Install using the official instructions for that package source. For example, on a system with Snap support:

```bash
sudo snap install codium --classic
```

4. Launch VSCodium from the applications menu.
5. Open a terminal and run:

```bash
codium --version
```

6. If the command is unavailable, confirm the package's executable name and PATH.

### Configure extensions and accessibility

1. Open the Extensions view.
2. Check which extension registry is configured. VSCodium commonly uses Open VSX by default.
3. Search for the language extension required by the course. Confirm that the extension is available for VSCodium and supports the required language runtime.
4. If an extension is missing, do not download an unverified VSIX file. Ask the instructor to approve an alternative or use VS Code/Theia for that language.
5. Test screen-reader navigation in the editor, command palette, extension view, terminal, and diagnostics. Similarity to VS Code does not guarantee identical accessibility or extension behavior.

## Lesson 4: Install Eclipse Theia IDE

Theia IDE is an open-source desktop IDE built on the Eclipse Theia platform. The official site provides desktop builds for Windows, Linux, and macOS. A time-limited online demo is also available; it is useful for exploration but should not be treated as a permanent course workspace.

Use the official [Theia IDE download page](https://theia-ide.org/). Confirm the current installer and system requirements before installing.

### Windows

1. Open the official Theia IDE website and choose **Windows** under Download Theia IDE.
2. Download the current Windows installer.
3. Run the installer and follow its prompts. Use the default installation location unless the instructor or administrator specifies otherwise.
4. Launch **Theia IDE** from the Start menu.
5. On first launch, choose or create a workspace folder when prompted.
6. Open a terminal and test the language runtime separately; Theia does not install every language compiler or SDK automatically.

### macOS

1. Open the official Theia IDE website.
2. Select the build matching the Mac's architecture: Apple silicon (ARM) or Intel (x86).
3. Download and open the disk image or archive provided by the official site.
4. Move Theia IDE into Applications if the installer requires it.
5. Launch Theia IDE. If macOS blocks the application, verify the download source and follow the current vendor/macOS guidance rather than bypassing security checks indiscriminately.
6. Create or open a workspace folder.

### Linux

1. Open the official Theia IDE website.
2. Select the Linux AppImage or Snap package appropriate to the distribution.
3. For an AppImage, download it, mark it executable using the file manager or `chmod +x`, then launch it. For Snap, follow the official Snap installation link.
4. Launch Theia IDE from the application menu or the downloaded AppImage.
5. Create or open a workspace folder.
6. Confirm the required compiler or interpreter is installed separately and callable from the integrated terminal.

### First-run and accessibility checks

1. Locate the file explorer, editor, command/search interface, terminal, and problems/diagnostics view using the keyboard.
2. Confirm the operating system's screen reader can announce the active editor and read source text.
3. Test moving between the editor and terminal without using a mouse.
4. Open a small plain-text source file and verify that punctuation, indentation, and line navigation are understandable.
5. Check the extension/plugin registry and install only the language tools required by the course.
6. If a required control or extension cannot be operated accessibly, switch to VS Code, VSCodium, or a simpler editor rather than forcing an inaccessible workflow.

The online Theia demo may have a session time limit and should be used only to evaluate the interface, not to store course projects.

## Lesson 5: Create and test a project workspace

The same project habits apply in any editor.

1. Create a course folder in a location you can find again, such as `Documents/CS-Course`.
2. Inside it, create a project folder for the current language, such as `python-practice` or `c-practice`.
3. Open the project folder in the IDE using **File → Open Folder** or the equivalent command.
4. Create a source file with the correct extension for the language.
5. Save the file before running it.
6. Open the integrated terminal and confirm its current directory is the project folder.
7. Run the language-specific verification command taught in the language's setup unit.
8. Read the complete output, including warnings and errors. Confirm that the program's output is text and can be read with the learner's access technology.
9. Close the IDE and reopen the same folder to confirm the project can be found and resumed.

Do not create a separate project for every tiny experiment unless the language's tooling requires it. Keep course work organized in named folders and use version control when it is introduced.

## Lesson 6: AI features in modern IDEs — course policy

Modern IDEs may offer AI-powered chat, code completion, inline suggestions, explanations, test generation, and agent-like actions. VS Code can be configured with AI extensions and services such as GitHub Copilot. VSCodium may support compatible third-party AI extensions, subject to its extension registry. Theia IDE includes an AI-oriented architecture and can connect to selected model providers.

Availability, account requirements, pricing, privacy terms, and extension compatibility change. An AI feature appearing in an editor does not mean that the course endorses or requires it.

<blockquote>
**Course rule:** AI tools are for personal exploration of concepts and reinforcement of learning only. They must not be used to write, complete, autocomplete, repair, or generate code for course lessons, exercises, quizzes, projects, or assessments.
</blockquote>

Appropriate uses, when allowed by the instructor:

- Ask for a plain-language explanation of a concept already introduced in the lesson.
- Ask for an analogy or a second explanation of a term.
- Ask the tool to quiz you on definitions or ask conceptual questions.
- Ask for a comparison of two concepts without requesting a code solution.
- Ask for a non-code explanation of why a programming concept is useful.

Not permitted for course learning tasks:

- Asking AI to write a program, function, class, query, or shell command for an assignment.
- Accepting generated completions or inline suggestions as the student's own work.
- Asking AI to solve an exercise, complete missing code, or generate a project.
- Asking AI to rewrite a student's solution or silently apply a code change.
- Using an AI agent to edit files, run commands, or make project changes for the student.

The purpose is to build independent problem-solving and code-reading skills. If an AI explanation is used, the student should verify it against course material or official documentation and be able to explain the concept without the tool. Follow the instructor's stricter rules during quizzes and assessments. Never submit passwords, API keys, student records, private source code, or other sensitive information to an AI service.

## IDE versus text editor: choosing the learning environment

The IDE is not the learning objective. Students should be able to describe what source code is, where files are stored, how the language runtime/compiler is invoked, how output is produced, and how to interpret errors whether they use VS Code or a plain editor.

A learner may prefer:

- **Notepad++** on Windows for lightweight text editing.
- **BBEdit** on macOS for text editing and text-processing workflows.
- **Sublime Text** on Windows, macOS, or Linux for fast, extensible editing.
- **A Linux desktop editor** such as Gedit, Kate, or Mousepad.
- **A terminal editor** such as nano when a terminal-first workflow is appropriate.

These are valid choices if the learner can create and save files, run the required compiler/interpreter, read output, and complete debugging tasks accessibly. The instructor should assess the programming concepts, not the presence of IDE-specific features.

## Activities

1. Choose one IDE from this lesson and install it.
2. Use only the keyboard to open a project folder, create a source file, save it, and open the integrated terminal.
3. Ask the screen reader to read the source file by line, word, and character. Record any punctuation or focus-navigation difficulties.
4. Run the language-specific verification command from the corresponding course setup unit.
5. Repeat the same simple edit-and-run workflow in a lightweight text editor, using the terminal to run the program.
6. Write a short comparison identifying which environment is more efficient and accessible for your current needs.

## Skills checklist

- [ ] I can explain the difference between an IDE, a text editor, and a compiler/interpreter.
- [ ] I installed and launched one IDE or text editor.
- [ ] I can open a project folder and create a source file.
- [ ] I can navigate the editor and terminal using the keyboard.
- [ ] I tested the workflow with my screen reader or other access technology.
- [ ] I can run a program using the language toolchain rather than relying only on an IDE run button.
- [ ] I can explain at least two advantages and two disadvantages of an IDE.
- [ ] I understand the course restrictions on AI-assisted coding.

## Further learning and official references

- [Visual Studio Code downloads](https://code.visualstudio.com/Download)
- [Visual Studio Code setup documentation](https://code.visualstudio.com/docs/setup/setup-overview)
- [Visual Studio Code accessibility documentation](https://code.visualstudio.com/docs/configure/accessibility/accessibility)
- [VSCodium installation instructions](https://vscodium.com/#install)
- [VSCodium releases](https://github.com/VSCodium/vscodium/releases)
- [Eclipse Theia IDE downloads and documentation](https://theia-ide.org/)
- [Theia IDE documentation](https://theia-ide.org/docs/)

---

Complete this lesson before installing language-specific extensions. Then return to the selected language curriculum and follow its runtime, compiler, SDK, and project setup instructions.
