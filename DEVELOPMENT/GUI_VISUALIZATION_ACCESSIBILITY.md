# GUI, Visualization, and Workbench Accessibility Reference

This guide is the shared reference for the language introductions. It distinguishes **screen-reader support for application controls** from **access to the information represented by a chart, canvas, map, or other visual output**. A toolkit can expose its buttons and menus while leaving the chart itself inaccessible.

## Course-wide rule

Core lessons, exercises, and assessments must remain completable without sight. Use a keyboard-operable, screen-reader-readable terminal or semantic document as the baseline. A GUI may be an optional extension only when its controls have accessible names, roles, states, values, focus order, keyboard operation, and useful announcements. Every visualization must also have a data table or structured textual equivalent, a concise interpretation, units, and a description of important trends or exceptions.

There is **no universal screen-reader command-line flag**. Accessibility is normally provided by the platform accessibility API and the toolkit's accessibility implementation. Do not add guessed flags to launch commands. The activation settings below apply only to the named platform/toolkit.

## Status meanings

- **Recommended:** has a supported accessibility API or semantic platform model and is a reasonable candidate after testing with the target screen reader.
- **Conditional:** can work, but support depends on platform, toolkit version, component, implementation, or additional configuration. Do not assume every widget or visualization is exposed.
- **Avoid as a required activity:** does not reliably expose the essential interface or visual information to screen readers. It may be shown as an optional visual supplement only when an equivalent accessible route is supplied.

## Language-by-language guidance

### Python

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Terminal/CLI, standard input/output | **Recommended** | Preferred baseline. No accessibility flag. Keep prompts, errors, and output textual and deterministic. |
| PySide6/PyQt (Qt Widgets) | **Conditional / preferred Python GUI option** | Qt has QAccessible and platform bridges (Windows MSAA/UIA, macOS Accessibility, Linux AT-SPI). Use standard Qt widgets, labels, layouts, keyboard focus, and accessible names; custom-painted widgets need their own accessibility interface. On Linux/X11, if AT-SPI is not activated by the desktop, set `QT_LINUX_ACCESSIBILITY_ALWAYS_ON=1` before launching. This is not a universal Windows/macOS flag. Test the exact screen-reader/Qt combination. |
| wxPython | **Conditional** | Uses native platform controls in many cases, so results vary by OS and widget. No general screen-reader flag; test each control and provide a text alternative. |
| Tkinter / Tcl-Tk | **Avoid as a required GUI for blind learners** | The Python standard library documents the wrapper and supported platforms, but does not promise a cross-platform screen-reader accessibility layer. There is no Tkinter screen-reader flag that makes it reliably accessible. Do not use it as the course's default GUI; prefer CLI or a tested Qt/web interface. |
| Kivy and custom canvas/game interfaces | **Avoid as required activities** | Canvas-first interaction and custom-drawn controls are not automatically exposed as semantic controls. No single activation flag repairs this. |
| Matplotlib, Seaborn, Plotly, Bokeh | **Conditional visualizations** | A chart is not a substitute for its data. Include a sorted table/data export, chart title, axis labels, units, and plain-language findings. Matplotlib has no general screen-reader activation flag. Plotly's SVG/HTML output can expose some structure, but do not treat that as full chart accessibility. For web charts, use a maintained accessibility module where available and still provide a table/description. |

**Python recommendation:** teach CLI first. For optional desktop GUI work, evaluate Qt Widgets on the actual learner platform. Do not teach Tkinter as an accessible default. For charts, always expose the underlying values and interpretation as text.

### JavaScript and TypeScript

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Semantic HTML, native form controls, and browser document UI | **Recommended** | Use native `button`, `input`, `select`, `label`, headings, landmarks, lists, and tables. Prefer native HTML semantics over custom ARIA. No screen-reader flag; accessibility is exposed through the browser/platform accessibility tree. |
| React, Vue, Angular, Svelte | **Conditional / recommended when semantic** | Frameworks do not make a page accessible automatically. Use native elements, labels, correct heading structure, managed focus, and live regions only when needed. No framework-wide screen-reader flag. |
| Electron | **Conditional** | Web technologies inherit browser accessibility; ensure the renderer uses semantic HTML and keyboard support. No general Electron screen-reader flag is required. |
| Chart.js / canvas charts | **Avoid as sole information channel** | Canvas pixels do not provide a complete semantic chart by default. Add a data table and textual summary; provide accessible controls separately. No flag enables chart semantics. |
| Highcharts | **Conditional / preferred charting option when configured** | Include and initialize the Highcharts Accessibility module (for example, `import "highcharts/modules/accessibility";` in supported module setups). Configure descriptive chart titles, axis titles, series descriptions, keyboard navigation, and data-table access. Module inclusion is necessary but does not replace testing or a textual interpretation. |
| D3.js / custom SVG | **Conditional** | Use semantic SVG title/description, meaningful labels, keyboard-operable interactions, and a text/table equivalent. Custom visualization logic must implement accessible names, roles, states, and focus. |
| Node.js terminal programs | **Recommended** | Preferred TypeScript/JavaScript course baseline. No flag. |

**Web rule:** ARIA is not a repair switch. Use native HTML first; add ARIA only when native semantics do not express the interaction.

### Java

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Terminal applications | **Recommended** | Preferred baseline; no flag. |
| Swing / Java Foundation Classes | **Conditional / supported** | Swing implements the Java Accessibility API. On Windows, enable Java Access Bridge for the JDK with `%JAVA_HOME%\\bin\\jabswitch -enable`, then restart the screen reader and Java application. The application must use accessible Swing components and meaningful names/descriptions. This command is Windows-specific; do not add it to macOS/Linux launch commands. |
| JavaFX | **Conditional** | Provides accessibility support for standard controls, but custom controls and complex scenes need explicit accessible roles/text and testing. No general JavaFX screen-reader flag. |
| JavaFX Canvas, Swing custom painting, game/graphics canvases | **Avoid as required activities** | Visual drawing is not equivalent to a semantic control tree. Supply a structured textual/data representation and keyboard route. |

### Kotlin

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Kotlin/JVM terminal applications | **Recommended** | Preferred baseline; no flag. |
| Swing | **Conditional** | Same Java Accessibility API and Windows Java Access Bridge requirement as Java: `%JAVA_HOME%\\bin\\jabswitch -enable`. Use standard accessible Swing controls and test. |
| JavaFX | **Conditional** | Same limitations as JavaFX in Java. No universal activation flag. |
| Android Jetpack Compose / native Android views | **Conditional / recommended for platform-specific extension** | Use standard semantics and Compose `Modifier.semantics`, content descriptions, and proper roles/state descriptions. TalkBack is provided by Android; there is no general application launch flag. Test with TalkBack. |

### C and C++

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Terminal / curses-style text UI | **Recommended with care** | Use ordinary text output for the core course. For terminal TUIs, preserve logical reading order, avoid constant screen repainting, and ensure every action has a keyboard command. No universal flag. |
| Qt Widgets (C++ or bindings) | **Conditional / preferred desktop GUI candidate** | Qt QAccessible exposes platform accessibility APIs. Use standard widgets and implement accessibility interfaces for custom controls. On Linux/X11, set `QT_LINUX_ACCESSIBILITY_ALWAYS_ON=1` before launch if the AT-SPI bridge is not activated. |
| GTK | **Conditional / preferred on GTK desktop environments** | GTK widgets expose AT-SPI on Linux when the accessibility bus is available. No general per-app screen-reader flag; confirm the desktop accessibility bus and test the specific GTK version. |
| wxWidgets | **Conditional** | Native-control integration can help, but support varies by platform and widget. No universal activation flag. |
| SDL, OpenGL, DirectX, SFML, raylib, custom drawing | **Avoid as required activities** | Primarily visual rendering; controls and graphics are not automatically a semantic accessibility tree. Include a text-mode alternative and do not require visual inspection. |

### C#

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Console applications | **Recommended** | Preferred baseline; no flag. |
| WPF standard controls | **Recommended / conditional by implementation** | Standard WPF controls expose Microsoft UI Automation. Set `AutomationProperties.Name`, `HelpText`, and appropriate control properties when defaults are insufficient. Custom controls require AutomationPeers. No global WPF screen-reader flag. |
| Windows Forms standard controls | **Conditional** | Standard controls expose accessibility information; set accessible name, role, description, and keyboard order. Custom-drawn controls need explicit accessibility support. No global activation flag. |
| WinUI 3 / .NET MAUI | **Conditional** | Use platform-native semantic properties and labels; verify each target OS. No universal screen-reader flag. |
| Unity UI / custom game canvases | **Avoid as required activities** | A visually rendered game interface is not automatically exposed to platform screen readers. Use a documented accessible UI layer and provide a nonvisual equivalent; do not assume the editor or runtime has an activation flag that solves this. |

For third-party WPF controls, follow the vendor's exact instructions. For example, some DevExpress WPF controls remove UI Automation peers/events for performance; that vendor documents launching a screen reader before the application or setting its `ScreenReader` parameter to `true`. This is **vendor-specific**, not a WPF setting.

### Go

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Console applications | **Recommended** | Preferred baseline; no flag. |
| Fyne | **Conditional / do not assume** | Test the exact widgets and OS with the target screen reader before adopting. No universal Fyne screen-reader flag. Provide a CLI route. |
| Gio / Ebiten / game-oriented canvas frameworks | **Avoid as required activities** | Custom-rendered interfaces do not automatically provide a complete semantic accessibility tree. Provide a text interface and do not make visual interaction mandatory. |
| Wails / web front end | **Conditional** | Accessibility comes primarily from the web renderer: use semantic HTML, keyboard interaction, and accessible names. No general Wails flag. |

### Julia

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| REPL / terminal scripts | **Recommended** | Preferred baseline; no flag. |
| Pluto notebooks / Jupyter | **Conditional** | Notebook interfaces and cell output require testing with the learner's browser/screen reader. Provide scripts and sequential text output as an equivalent path. No Julia-specific screen-reader flag. |
| Makie, Plots.jl, Gadfly, GR | **Conditional visualizations** | Charts are visual outputs. Provide the source data as tables/CSV and a plain-language interpretation; no general Julia plotting accessibility flag. |
| Gtk.jl / Qt-based GUI packages | **Conditional** | Depends on the underlying toolkit and platform bridge; apply GTK/Qt guidance above and test the specific package version. |

### Lua

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Lua interpreter / terminal programs | **Recommended** | Preferred baseline; no flag. |
| wxLua / GTK bindings | **Conditional** | Inherit the underlying toolkit's platform support; test actual controls. No Lua-specific activation flag. |
| LÖVE, Solar2D, custom game UI | **Avoid as required activities** | Graphics-first interfaces are not automatically exposed as semantic screen-reader controls. Provide a text-mode equivalent and never require visual-only play. |

### Rust

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| CLI applications | **Recommended** | Preferred baseline; no flag. |
| GTK4 / native platform widgets | **Conditional** | GTK accessibility relies on the platform accessibility bus (AT-SPI on Linux). No general Rust flag; follow GTK platform setup. |
| Iced / egui / Slint | **Conditional** | Accessibility support varies by framework version and widget. Check whether the exact release exposes AccessKit/platform semantics and test all controls; do not infer full screen-reader support from a feature flag alone. |
| Bevy / wgpu / custom GPU rendering | **Avoid as required activities** | Rendering is not an accessible control tree. Provide an independent text interface and textual state descriptions. |

### Swift

| Technology | Status | Guidance and activation |
| --- | --- | --- |
| Swift command-line programs | **Recommended** | Preferred baseline; no flag. |
| SwiftUI standard controls | **Recommended / conditional by design** | Apple platforms expose standard controls to VoiceOver. Add `.accessibilityLabel(_:)`, `.accessibilityValue(_:)`, `.accessibilityHint(_:)`, and grouping/element modifiers where needed. No launch flag; VoiceOver is an OS feature. |
| UIKit / AppKit standard controls | **Recommended / conditional by design** | Use native controls and accessibility properties; custom-drawn controls must implement accessibility elements. No launch flag. |
| SpriteKit / SceneKit / Metal custom scenes | **Avoid as required activities unless explicitly made accessible** | Visual scenes are not automatically equivalent to semantic navigation. Supply accessible elements and a textual equivalent. |

### R, HTML/CSS, SQL, Bash, and PowerShell modules

| Subject/tool | Status | Guidance and activation |
| --- | --- | --- |
| R console and scripts | **Recommended** | Preferred baseline; no flag. |
| RStudio IDE | **Conditional** | Screen-reader behavior varies by release, platform, and pane. Verify editor, console, environment, plots, and data viewer separately; keep scripts and console output usable independently. No universal RStudio launch flag should be assumed. |
| Base R graphics, ggplot2, lattice | **Conditional visualizations** | Plots are not self-describing. Supply data tables, accessible captions, units, and narrative findings. No general R plotting screen-reader flag. |
| HTML/CSS in modern browsers | **Recommended when semantic** | Native HTML, correct headings/landmarks, form labels, tables, keyboard focus, and sufficient contrast. No browser or HTML screen-reader flag. ARIA does not compensate for poor semantics. |
| CSS-only visual indicators / charts | **Avoid as sole information channel** | Provide equivalent text and data; do not rely on color, position, or shape alone. |
| SQL command-line clients (SQLite CLI, psql) | **Recommended** | Prefer query text and sequential result output. SQLite: use `.headers on` and `.mode list` (or `.mode line`) for predictable text; no screen-reader flag. |
| Database GUI result grids (DB Browser, DBeaver, pgAdmin, etc.) | **Conditional** | Grid accessibility differs by client/version/OS. Test query editor, result navigation, row/column headers, dialogs, and export. Always teach a CLI/text-export route. No universal SQL client flag. |
| Bash / PowerShell terminals | **Recommended** | Use a terminal that works with the learner's screen reader; no shell-specific accessibility flag. Avoid progress bars, cursor-position rewrites, color-only status, and output that disappears. |

## Launch flags and settings quick reference

Only use the following when the corresponding platform/toolkit is in use:

| Platform/toolkit | Setting | Scope |
| --- | --- | --- |
| Qt on Linux/X11 | `QT_LINUX_ACCESSIBILITY_ALWAYS_ON=1` | Forces Qt's Linux accessibility activation path. Set in the environment before launching the Qt application; not a Windows/macOS setting. |
| Java Swing on Windows | `%JAVA_HOME%\\bin\\jabswitch -enable` | Enables Java Access Bridge for Windows assistive technologies. Restart the screen reader and Java application afterward. |
| DevExpress WPF controls | Launch screen reader before app **or** set vendor's `ScreenReader=true` parameter | Vendor-specific optimization; not required for ordinary WPF controls. |

Most recommended technologies have **no command-line accessibility flag**. They use operating-system accessibility services automatically. For web content, use semantic HTML and test with a screen reader. For Apple platforms, use VoiceOver and native accessibility APIs. For Windows desktop apps, expose UI Automation names, roles, values, and events. For Linux desktop apps, verify AT-SPI integration.

## Minimum validation protocol before adopting a GUI or visualization

1. Identify the exact operating system, screen reader/version, toolkit/runtime version, and component set.
2. Start the screen reader before launching the application if the vendor/toolkit requires it.
3. Complete the whole task using only the keyboard: open, navigate, edit, submit, recover from errors, and exit.
4. Verify accessible names, roles, values, states, labels, focus order, announcements, and error messages.
5. For charts, navigate to the underlying data and obtain the same conclusion without seeing the plot. Check values, units, axis meaning, series, outliers, and uncertainty.
6. Repeat after changing the window size, theme, zoom, and relevant application settings.
7. Record tested combinations and known barriers. A toolkit's accessibility API is not proof that every application built with it is accessible.

## Authoritative references

- [Qt QAccessible and platform bridges](https://doc.qt.io/qt-6/qaccessible.html)
- [Oracle: Java Access Bridge](https://www.oracle.com/java/technologies/javase/javase-tech-access-bridge.html)
- [Oracle: enabling and testing Java Access Bridge](https://docs.oracle.com/en/java/javase/13/access/enabling-and-testing-java-access-bridge.html)
- [Microsoft: develop accessible Windows apps](https://learn.microsoft.com/en-us/windows/apps/develop/accessibility)
- [Microsoft: WPF/UI Automation accessibility practices](https://learn.microsoft.com/en-us/dotnet/framework/ui-automation/accessibility-best-practices)
- [Apple: SwiftUI accessibility fundamentals](https://developer.apple.com/documentation/swiftui/accessibility-fundamentals)
- [Chrome: semantic HTML and ARIA guidance](https://developer.chrome.com/docs/modern-web-guidance/guides/accessibility/accessibility)
- [Python: tkinter documentation](https://docs.python.org/3/library/tkinter.html)

**Verification note:** These classifications are curriculum guidance, not certification. Accessibility can change between operating systems, screen readers, toolkit releases, and individual widgets. Test before making a tool mandatory.
