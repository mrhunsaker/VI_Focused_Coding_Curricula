# Screen-reader-accessible GUI libraries and implementation guidance

This guide identifies GUI frameworks and libraries that can expose application interfaces to screen readers and other assistive technologies for every language and focused module in this curriculum. It also identifies approaches that should not be selected for an accessibility-critical interface without substantial additional engineering and platform testing.

> **Important: no GUI library can guarantee accessibility by itself.** Accessibility depends on the framework, the controls selected, application code, operating-system accessibility APIs, assistive-technology combinations, content, and testing. Treat the recommendations below as technology-selection guidance, not as a conformance certificate or a promise that an application is accessible. Require manual testing with real screen readers and users with disabilities before release.

The phrase *screen-reader accessible* is used throughout. The guide also covers keyboard-only operation, focus visibility, zoom and text scaling, contrast, reduced motion, captions, and other requirements that affect people with disabilities.

## 1. Baseline requirements for every GUI

Use **WCAG 2.2 Level AA** as the default design and testing target for web content and web-based interfaces. For native applications, apply the relevant platform accessibility API and human-interface guidance as well as WCAG principles. A WCAG checklist alone does not replace platform-specific testing.

Every interactive control must expose, as applicable:

- **Role:** button, link, checkbox, radio button, text field, heading, table, menu item, slider, dialog, and so on.
- **Accessible name:** a concise, meaningful name that identifies the control's purpose. Visible labels should normally provide the name.
- **Value and state:** current text, selected value, checked state, expanded/collapsed state, progress, invalid state, and other relevant information.
- **Relationships:** programmatic association between labels, descriptions, errors, help text, groups, table headers, and the controls they describe.
- **Keyboard operation:** every action must be possible without a pointer. Focus order must be logical; focus must be visible and must not be trapped.
- **Change notifications:** validation errors, status updates, asynchronous results, and dialog openings must be communicated without unexpectedly moving focus.
- **Structure:** headings, landmarks, lists, tables, grouping, and reading order must reflect the meaning and visual organization of the interface.

Also:

1. Prefer built-in, platform-native controls over custom-drawn controls.
2. Never communicate meaning through color, shape, position, sound, or animation alone. Provide text or another perceivable equivalent.
3. Provide text alternatives for meaningful images and accessible names for icon-only controls. Mark decorative images as decorative.
4. Support text resizing, high-contrast or forced-colors modes, adequate contrast, and layouts that reflow without clipping.
5. Respect reduced-motion preferences. Avoid flashing content and autoplaying motion; provide pause, stop, or hide controls where required.
6. Give charts, maps, diagrams, canvases, and other visualizations a complete textual or tabular equivalent. A label on the canvas is not an equivalent.
7. Do not use positive tabindex values on the web. Do not remove focus outlines without an equally visible replacement.
8. Make dialogs announce their title and purpose, manage focus on open, contain focus while modal, and return focus to the invoking control on close.
9. Keep accessible names localized and understandable. Avoid redundant announcements such as repeating a visible label in both the name and description.
10. Document known platform limitations and test the exact packaged application, not just a development preview.

## 2. Web interfaces: HTML, CSS, JavaScript, and TypeScript

These languages share the browser accessibility platform. **Semantic HTML is the primary accessibility toolkit.** JavaScript frameworks do not replace HTML semantics, and TypeScript does not change browser accessibility behavior.

### Recommended foundations and libraries

| Technology | Assessment and use |
|---|---|
| Semantic HTML5 | First choice. Use `button`, `a`, `input`, `label`, `select`, `textarea`, `fieldset`, `legend`, headings, landmarks, lists, and data tables for their intended purposes. Native elements provide roles, keyboard behavior, and accessibility mappings. |
| React | Suitable when components render semantic HTML and manage focus and state correctly. Prefer native controls; use the React accessibility guidance and test rendered DOM, not component names. |
| Angular | Suitable when templates use semantic HTML and Angular CDK accessibility utilities where needed. CDK utilities assist with focus management, live announcements, and keyboard patterns; they do not make arbitrary components accessible automatically. |
| Vue | Suitable when components render semantic HTML and implement correct keyboard and focus behavior. Audit third-party component libraries individually. |
| Svelte / SvelteKit | Suitable on the same basis: semantic output, accessible state changes, correct focus management, and tested components. Compiler warnings are useful but do not prove conformance. |
| WAI-ARIA Authoring Practices Guide (APG) patterns | Use as implementation guidance for custom widgets such as tabs, menus, tree views, and comboboxes. Follow the complete keyboard interaction pattern, not just its ARIA attributes. |
| Accessible component systems (for example, React Aria) | Useful when a custom interaction is genuinely needed. Confirm current framework, browser, and assistive-technology support, and retain semantic HTML wherever possible. |

### Implementation rules

- Use a native `<button>` for actions and an `<a href>` for navigation. Do not simulate them with clickable `div` or `span` elements.
- Associate every form control with a visible `<label>`. Use `fieldset` and `legend` for related controls. Connect error and help text using `aria-describedby`; set `aria-invalid="true"` when appropriate.
- Use headings in a meaningful hierarchy and landmarks such as `header`, `nav`, `main`, and `footer`.
- Use ARIA only when native HTML cannot express the required semantics. ARIA changes accessibility-tree information; it does not add keyboard behavior, focus management, or functionality.
- For live updates, use a restrained `aria-live` region or appropriate status/alert role. Do not announce every keystroke or flood the screen reader.
- For custom tabs, menus, listboxes, grids, and comboboxes, implement the full APG keyboard model, including arrow keys, Home/End where specified, Escape, and focus restoration.
- For single-page applications, manage document titles, route announcements, skip links, and focus after navigation.
- Avoid replacing native form controls with visually styled generic elements unless there is a compelling reason and the full interaction model is implemented and tested.

### JavaScript and TypeScript framework cautions

Avoid or treat as high-risk:

- Component libraries whose controls are built from generic containers and have no documented keyboard and screen-reader behavior.
- Canvas, WebGL, SVG-only, or absolutely positioned interfaces that expose only a single image-like object instead of individual meaningful controls.
- Drag-and-drop-only interactions, hover-only menus, pointer-only gestures, and custom scrollbars without keyboard alternatives.
- Automatically generated ARIA attributes that do not match the actual role, state, or behavior.
- Framework-specific accessibility claims based solely on lint rules or compile-time warnings.

A framework's accessibility linting is a useful early warning system, not a substitute for browser and assistive-technology testing.

## 3. Python

Python has several desktop GUI choices. The accessibility of each depends on its native backend and the operating system.

| Library / approach | Assessment and recommended use |
|---|---|
| **PySide6 / Qt for Python** | Preferred general-purpose cross-platform desktop option when a full GUI is needed. Qt provides accessibility interfaces and standard controls expose roles, names, states, and actions. Use Qt Widgets for conventional forms and controls; test Qt Quick/QML controls and custom QML components on every target platform. |
| **PyQt6** | Uses the same underlying Qt accessibility infrastructure as PySide6. The primary distinction is licensing and packaging, not the accessibility model. Apply the same Qt guidance and testing. |
| **PyGObject with GTK 4** | Strong choice for Linux/GNOME-oriented applications. GTK's built-in widgets expose accessibility information through the platform accessibility stack. Prefer standard GTK widgets and follow GNOME HIG guidance. Cross-platform behavior must be verified. |
| **wxPython** | Can use native platform widgets and provides accessibility extension points. Treat accessibility as platform-dependent; the documented `wx.Accessible` interface has historically had platform/API limitations. Test the exact wxPython and OS versions. |
| **Tkinter** | Convenient standard-library GUI for small teaching examples. Accessibility behavior varies by Tcl/Tk version and operating system. Use standard widgets, visible labels, keyboard traversal, and test with the target screen reader. Do not assume that a working Tab order proves screen-reader support. |
| **Toga (BeeWare)** | Uses native widgets on supported platforms, which is a useful design direction. Verify the accessibility behavior of each backend and supported platform before choosing it for an accessibility-critical application. |
| **Web UI with a Python backend (for example, Flask, Django, FastAPI, or NiceGUI)** | Often a good option when the interface can be a browser application. The browser still needs semantic HTML and tested components; a Python server framework does not make its generated UI accessible. |

### Python: avoid or restrict

- **Kivy** and other interfaces that primarily render custom-drawn widgets: do not select for a screen-reader-critical desktop application unless the current release demonstrably exposes a complete accessibility tree and supports the target assistive technologies.
- **Dear PyGui**, **Pygame**, and raw OpenGL/Canvas-style interfaces: suitable for graphics, games, and visualization experiments, but not a default choice for form-heavy accessible desktop applications. A separate accessible control surface is required.
- **CustomTkinter**: visual styling does not improve the underlying Tk accessibility model. Treat it with the same platform-specific caution as Tkinter.
- **Matplotlib plots embedded in a GUI**: do not make the plot the only way to access data. Supply a structured table, textual summary, keyboard-accessible controls, and exportable data.

## 4. Java

| Library / approach | Assessment and recommended use |
|---|---|
| **Java Swing** | Established desktop option with the Java Accessibility API (JFC accessibility support). Prefer standard Swing components, meaningful accessible names/descriptions where needed, and correct labels and relationships. Test the selected JDK and operating system. |
| **JavaFX** | Suitable for modern desktop interfaces. Standard controls expose accessibility roles and text/value information through JavaFX accessibility support. Set accessible text/help where defaults are insufficient; verify custom controls and skins. |
| **Browser UI with Java backend** | Use semantic HTML and a tested web component strategy. The backend language does not determine browser accessibility. |

### Java: avoid or restrict

- **AWT Canvas**, JavaFX `Canvas`, custom-painted Swing components, and custom JavaFX controls without complete accessibility metadata and keyboard behavior.
- Third-party JavaFX skins or Swing Look-and-Feels that replace standard controls without documented accessibility testing.
- Interfaces where mouse listeners are the only way to activate a control.

For custom controls, implement the relevant Java accessibility interfaces and expose role, name, description, state, value, actions, and events. Validate using the target platform's screen reader and accessibility inspection tools.

## 5. Kotlin

| Library / approach | Assessment and recommended use |
|---|---|
| **Jetpack Compose for Android** | Preferred modern Android UI approach. Use Material/Foundation components and Compose semantics. Supply `contentDescription` for meaningful icon-only controls, appropriate roles and state descriptions, and logical traversal semantics. |
| **Compose Multiplatform** | Promising shared UI approach for Android, iOS, desktop, and web. It has a semantic tree and accessibility APIs, but platform support and behavior can differ. Test every target, including desktop accessibility enablement and iOS VoiceOver behavior. |
| **Android Views / Material Components** | Mature native Android approach. Standard widgets integrate with TalkBack. Use labels, hints, state descriptions, and accessibility delegates only where the default semantics are insufficient. |
| **JavaFX / Swing from Kotlin/JVM** | Kotlin can use the same Java accessibility support as Java. Choose standard controls and test as described in the Java section. |
| **Web UI with Kotlin backend or Kotlin/JS** | Use semantic HTML and web accessibility practices from Section 2. |

### Kotlin: avoid or restrict

- Compose `Canvas`, custom drawing, and graphics-only controls as the sole interaction or data representation.
- Custom composables that omit semantics, merge unrelated children, or provide misleading `contentDescription` values.
- Desktop or multiplatform UI libraries whose accessibility support is undocumented or untested on the exact target platform.
- Android layouts that depend on color, touch gestures, or position without equivalent semantics and keyboard/switch access.

## 6. C

C has no single standard cross-platform GUI library. Prefer a toolkit that connects controls to the operating system's accessibility API.

| Library / approach | Assessment and recommended use |
|---|---|
| **GTK 4** | Strong choice for Linux desktop applications. Standard widgets provide accessibility support through the GTK accessibility stack. Use GTK controls and GNOME accessibility guidance. |
| **Win32 common controls / Windows UI Automation** | Appropriate for Windows-only native applications when implemented with standard controls and correct UI Automation providers/patterns. Custom controls must expose equivalent UIA information. |
| **Qt through C bindings or a C-compatible interface** | Qt's accessibility architecture is strong, but Qt is primarily a C++ framework. Use an established, maintained binding rather than inventing a C ABI bridge. |
| **AccessKit C bindings** | An accessibility infrastructure option for developers implementing custom-rendered interfaces. It is not a complete GUI toolkit; the application still has to construct and update a correct accessibility tree and support platform adapters. |

### C: avoid or restrict

- **SDL**, **GLFW**, raw OpenGL/Vulkan, and framebuffer-only interfaces as the sole UI for an accessibility-critical application.
- Custom widget systems that expose pixels but no accessible roles, names, states, actions, or events.
- Legacy or abandoned GUI bindings without current platform accessibility support.

If a graphics library is needed, provide a parallel semantic interface with equivalent functionality and synchronize state and events between the two.

## 7. C++

| Library / approach | Assessment and recommended use |
|---|---|
| **Qt 6 (Widgets / Qt Quick)** | Preferred cross-platform C++ GUI toolkit for accessibility-critical desktop applications. Qt exposes accessibility metadata and APIs for custom controls. Prefer standard Widgets controls for conventional interfaces; verify QML/custom controls separately. |
| **GTK 4 with gtkmm** | Strong Linux/GNOME-oriented option. Standard GTK widgets expose accessible names and roles; follow GTK and GNOME HIG guidance. |
| **wxWidgets** | Uses native controls where available and provides accessibility mechanisms. Confirm the current platform-specific implementation and test it; do not assume identical support on Windows, macOS, and Linux. |
| **Win32 / Windows UI Automation** | Suitable for Windows-specific applications using native controls or complete UIA providers for custom controls. |
| **Web UI embedded in a desktop shell** | A browser-based front end can use semantic HTML and the practices in Section 2. Verify the embedded webview's browser engine and assistive-technology integration. |

### C++: avoid or restrict

- **Dear ImGui**, **SDL**, **GLFW**, custom OpenGL/Vulkan interfaces, and game-engine UI as the only interface for a general-purpose accessible application unless a verified accessibility bridge and complete keyboard/screen-reader model are provided.
- Qt/GTK custom-painted widgets that do not implement accessible interfaces.
- Unmaintained wrappers or bindings that lag behind the toolkit's accessibility APIs.

Qt's `QAccessible` interfaces are the extension point for custom Qt widgets. A custom widget is not accessible merely because it is drawn inside a Qt window.

## 8. C#

| Library / approach | Assessment and recommended use |
|---|---|
| **WPF** | Strong Windows desktop option. Standard controls integrate with Windows UI Automation. Use AutomationProperties and standard control patterns; implement automation peers for custom controls. |
| **WinUI 3** | Native Windows option with UI Automation integration. Prefer standard controls and expose appropriate automation properties and patterns for custom controls. |
| **Windows Forms** | Mature Windows-only option. Standard controls have accessibility support; custom controls require accessible object/provider work. Test keyboard navigation, Narrator, and UIA. |
| **.NET MAUI** | Suitable for cross-platform mobile/desktop applications when platform-specific semantics are tested. Use semantic properties for descriptions, hints, and headings; test VoiceOver, TalkBack, and desktop screen readers separately. |
| **Avalonia UI** | Cross-platform .NET option with automation peers and platform accessibility mappings (UI Automation, NSAccessibility, AT-SPI). Prefer built-in controls; supply AutomationProperties and test each supported platform. |
| **Blazor / ASP.NET Core web UI** | Browser-based interfaces should use semantic HTML and Section 2 guidance. Use accessible component libraries only after testing their actual rendered behavior. |

### C#: avoid or restrict

- **MonoGame**, **Unity UI**, **Win2D**, SkiaSharp custom drawing, and canvas-based interfaces as the only interaction layer for an accessibility-critical business application.
- Custom WPF/Avalonia templates that remove labels, focus visuals, automation peers, or keyboard behavior.
- Third-party controls that claim accessibility but do not document UI Automation patterns and screen-reader testing.

For WPF and WinUI, verify that each custom control exposes the correct UI Automation control type, name, help text, state, supported patterns, and events. For MAUI and Avalonia, test every operating system separately.

## 9. Julia

Julia's desktop GUI ecosystem is smaller than those of Python, Java, and C++. Choose an established toolkit or a browser interface rather than assuming a plotting package is a full GUI.

| Library / approach | Assessment and recommended use |
|---|---|
| **Gtk.jl (GTK)** | Practical route to GTK's native accessibility support, especially for Linux desktop applications. Prefer standard GTK widgets and validate the Julia binding and GTK version used. |
| **QML.jl / Qt Quick integration** | Can provide a Qt-based UI. Qt has accessibility APIs, but validate the specific Julia binding, Qt version, QML controls, and custom components. |
| **Browser-based Julia applications (for example, Genie/Stipple or Pluto notebooks)** | Use browser semantics and the web practices in Section 2. Ensure generated controls, notebook cells, outputs, and interactive plots are keyboard and screen-reader usable. |
| **Native host application plus Julia computation** | Often a sound architecture: use an accessible host UI (for example, a web front end or native toolkit) and call Julia for computation. |

### Julia: avoid or restrict

- **Makie**, **Plots.jl**, **GLMakie**, and other visualization packages as the only way to present results. A chart is not a substitute for a data table, text summary, or downloadable data.
- Experimental GUI wrappers with no documented accessibility-tree support.
- Interfaces that require precise mouse interaction with a plot, notebook output, or custom canvas.

For every visualization, expose the underlying values, labels, relationships, and trends in a structured alternative. Provide keyboard-accessible controls for changing plotted variables.

## 10. Swift

| Library / approach | Assessment and recommended use |
|---|---|
| **SwiftUI** | Preferred declarative approach for new Apple-platform interfaces. Standard controls have built-in accessibility. Use `accessibilityLabel`, `accessibilityValue`, `accessibilityHint`, appropriate traits, and grouping/focus APIs when needed. |
| **UIKit** | Preferred native iOS/iPadOS approach where imperative control is useful. Standard views and controls support VoiceOver; expose custom elements using UIAccessibility APIs and containers. |
| **AppKit** | Native macOS framework with accessibility support. Use standard controls and implement the NSAccessibility protocol for custom views. |
| **WebKit / browser UI** | A web front end can use semantic HTML. Test in the actual WKWebView and target macOS/iOS versions. |

### Swift: avoid or restrict

- **SpriteKit**, **SceneKit**, Metal-rendered screens, custom-drawn `Canvas` views, and game interfaces as the sole interface for non-game tasks or essential information.
- SwiftUI views that use decorative labels as the only control name, hide meaningful children, or combine unrelated controls into one accessibility element.
- Custom UIKit/AppKit views that do not expose accessibility elements, actions, values, and focus behavior.

Test VoiceOver, Voice Control, Switch Control, keyboard navigation on macOS, Dynamic Type, increased contrast, and Reduce Motion. A SwiftUI control that works on iOS is not automatically verified on macOS or watchOS.

## 11. Rust

Rust's GUI ecosystem is evolving. Accessibility support varies considerably by toolkit and target platform. Verify current release notes and platform coverage before committing to a toolkit.

| Library / approach | Assessment and recommended use |
|---|---|
| **GTK 4 via gtk-rs** | Strong choice for Linux desktop applications. GTK's built-in widgets expose accessible information; gtk-rs documentation covers accessible labels and descriptions. |
| **Slint** | A cross-platform toolkit with an AccessKit-based accessibility feature. Enable the feature, use semantic controls, and verify platform coverage and current version behavior. |
| **egui / eframe** | Has AccessKit integration on some platforms/releases. Treat support as platform- and version-specific; do not infer full cross-platform coverage from the existence of the integration. |
| **Tauri with a web front end** | Often a strong choice when browser-based UI is acceptable. Use semantic HTML and tested web components; Rust provides application logic while the system webview renders the UI. |
| **Dioxus desktop/web** | Can use web semantics for browser/webview targets. Verify the generated DOM, keyboard model, and assistive-technology behavior for the exact target. |
| **AccessKit** | Accessibility infrastructure for custom toolkit developers, not a turnkey GUI. Use its platform adapters and maintain a complete, accurate accessibility tree. |

### Rust: avoid or restrict

- **Iced** or other custom-rendered toolkits when the current release has no verified screen-reader accessibility integration for the target platforms. Re-check current status before adoption; this is a technology-selection warning, not a permanent claim about the project.
- **Bevy**, **macroquad**, **minifb**, raw wgpu/winit, and game/graphics frameworks as the sole interface for a conventional accessible desktop application.
- Any custom widget toolkit that has keyboard focus but does not expose semantic roles, names, states, values, and events.

For custom rendering, AccessKit can bridge to platform accessibility APIs, but it does not automatically infer the meaning of the pixels. The application must create and update the semantic tree correctly.

## 12. Go

Go does not include a standard GUI toolkit. The best choice depends on whether the application needs a native desktop interface or can use a browser.

| Library / approach | Assessment and recommended use |
|---|---|
| **Wails with HTML/CSS/JavaScript front end** | Often the most practical accessibility-oriented desktop approach. Use semantic web controls and test the actual platform webview (WebView2, WKWebView, or WebKitGTK as applicable). |
| **Web application with Go backend** | Strong option when desktop-native behavior is not required. Use semantic HTML, accessible components, and Section 2 testing. |
| **GTK via Go bindings** | Can access GTK's native accessibility infrastructure. Check binding maintenance, GTK version, and platform support before adoption. |
| **Native platform APIs** | Windows UI Automation, macOS accessibility APIs, or Linux AT-SPI can be used through bindings or system calls, but this is a specialist implementation path. |

### Go: avoid or restrict

- **Fyne**, **Gio**, **Ebiten**, and other custom-rendered toolkits as the default for screen-reader-critical applications unless current documentation and tests demonstrate support for every required platform and control type. Do not infer accessibility from cross-platform support or keyboard navigation alone.
- Old or inactive GUI bindings with unclear platform accessibility support.
- Custom canvas widgets without a parallel semantic control tree.

Fyne and similar libraries may be suitable for many applications, but accessibility must be verified at the current version and target platform. If a webview front end is selected, remember that browser accessibility still depends on semantic HTML and correct component behavior.

## 13. Lua

Lua is commonly embedded in applications and games, so the host toolkit often determines accessibility more than Lua itself.

| Library / approach | Assessment and recommended use |
|---|---|
| **wxLua / wxWidgets** | Can use native controls and wxWidgets accessibility mechanisms. Verify the current binding, target OS, and screen-reader support; do not assume the full C++ toolkit's support is perfectly exposed by every Lua binding. |
| **IUP** | Provides native GUI controls on supported platforms. Accessibility behavior is platform-dependent; test the exact controls and OS combinations before using it for essential workflows. |
| **Web UI hosted by a Lua application/server** | Use semantic HTML and the practices in Section 2. This can be preferable to custom-drawn interfaces. |
| **Host application's native UI API** | When Lua is embedded in an existing product, use that host's documented accessible UI framework rather than drawing a parallel interface. |

### Lua: avoid or restrict

- **LÖVE (Love2D)**, **Defold**, **Solar2D**, and other game/graphics frameworks as the only interface for conventional form-based or data-entry applications. They are not substitutes for a native semantic widget toolkit.
- Custom OpenGL/canvas widgets without an accessibility bridge and equivalent keyboard interface.
- Abandoned Lua bindings whose accessibility behavior cannot be confirmed.

For games, provide accessible menus, text alternatives, remappable controls, narration or audio cues where useful, non-color-only indicators, and a way to access game state without relying exclusively on visual effects. Game accessibility is a specialized discipline; a screen-reader label alone is not sufficient.

## 14. R

R is primarily used for statistical computing and data analysis. For user-facing applications, prefer browser interfaces or native controls with a structured alternative to every plot.

| Library / approach | Assessment and recommended use |
|---|---|
| **Shiny** | Recommended for interactive data applications when built with semantic HTML, accessible form controls, keyboard operation, and carefully managed status announcements. Audit Shiny modules and third-party inputs individually. |
| **Quarto websites / documents** | Suitable for accessible reports when headings, links, tables, code, and figures are authored semantically and checked in the rendered output. |
| **R Markdown** | Can produce accessible HTML documents with semantic structure. Verify the chosen output format and theme. |
| **tcltk** | R's Tcl/Tk interface can create desktop controls, but accessibility varies with the Tcl/Tk version and platform. Test before relying on it. |
| **R + accessible web front end** | R can provide analysis through Shiny or an API while a web front end supplies semantic controls. |

### R: avoid or restrict

- **ggplot2**, **plotly**, **htmlwidgets**, and dashboard charts as the only representation of data. Provide a data table, concise textual interpretation, and accessible controls for changing the view.
- Custom HTML widgets that use mouse-only controls or expose no semantic structure.
- RStudio Viewer or notebook output as the only access path for essential information without testing the rendered document in a browser and screen reader.

For charts, include a meaningful title, summary, data table, and clear descriptions of trends and outliers. Do not rely on color alone to distinguish series.

## 15. HTML and CSS focused module

HTML and CSS are not standalone GUI toolkits. They define the document and presentation layer used by browser interfaces. Use the web recommendations in Section 2.

Prefer native HTML controls and semantic elements. CSS must preserve focus visibility, reading order, zoom, reflow, contrast, and forced-colors behavior. Avoid CSS that visually reorders content in a way that conflicts with DOM reading order, hides focus, clips enlarged text, or removes meaningful content from the accessibility tree.

Do not use CSS-generated text as the only source of essential information. Do not use `display: none` or `visibility: hidden` for content that must remain available to assistive technology. Use visually-hidden techniques only when content should be available to screen readers but not visually displayed, and ensure it remains understandable.

## 16. SQL focused module

SQL is a query language, not a GUI toolkit. Accessibility depends on the database client, administration tool, report interface, and application built around the database.

- Choose database clients that support keyboard navigation, accessible grids, labeled controls, and screen-reader testing.
- Prefer structured query results that can be navigated as tables with column headers and predictable row/column movement.
- Provide export to accessible CSV or other structured formats where appropriate.
- Do not make a visual query-plan diagram, database schema canvas, or color-coded result grid the only way to inspect information.
- When building a database application, use the accessibility guidance for its host language and GUI framework.

A database driver or SQL engine does not make the application interface accessible.

## 17. Bash and PowerShell

Bash and PowerShell are shell languages, not general-purpose GUI frameworks. Their normal interfaces are command-line terminals.

- Prefer terminal emulators with screen-reader support and accessible text output.
- Ensure commands produce meaningful text, stable headings, explicit status messages, and useful error messages.
- Do not use color as the only signal. Respect terminal accessibility settings and avoid unnecessary cursor-positioning or full-screen output that disrupts screen-reader reading.
- For interactive terminal user interfaces (TUIs), provide keyboard navigation, predictable focus, text labels, and screen-reader-tested output. A TUI library's ability to draw boxes or handle keypresses does not establish accessibility.
- When a script needs a graphical interface, delegate to a supported native or web GUI framework and follow the corresponding language/platform guidance.

Avoid making a full-screen terminal UI the only route through a critical workflow unless it has been tested with the target terminal, screen reader, and operating system.

## 18. Testing and release gate

Accessibility is a release requirement, not a final cosmetic pass. Test the actual application, on each supported operating system, with the screen readers and input methods used by the intended audience.

### Minimum manual test matrix

| Environment | Screen reader / accessibility tools | Required checks |
|---|---|---|
| Windows | Narrator; NVDA; Windows UI Automation inspection tools | Names, roles, values, state changes, keyboard navigation, focus, dialogs, tables, high contrast, text scaling. |
| macOS | VoiceOver; Accessibility Inspector | Reading order, labels, groups, keyboard access, focus, Dynamic Type/text scaling where supported, contrast, dialogs. |
| iOS / iPadOS | VoiceOver; Switch Control; Voice Control | Swipe navigation, rotor/navigation structure, labels, hints, state, custom actions, touch alternatives, larger text. |
| Android | TalkBack; Switch Access; Accessibility Scanner (as a supplemental tool) | Traversal order, labels, state, headings, touch targets, switch/keyboard access, large font and display scaling. |
| Linux desktop | Orca; Accerciser; AT-SPI inspection | Accessible names/roles/states, keyboard traversal, focus, GTK/Qt controls, large text, high contrast. |
| Web browsers | NVDA with Firefox/Chrome; VoiceOver with Safari; keyboard-only testing | Semantic structure, forms, live regions, route changes, dialogs, custom widgets, zoom/reflow, forced colors. |

Not every combination is available or equally supported. Select combinations based on the platforms actually shipped, and add combinations requested by users or required by procurement or regulation.

### Automated checks (supplement, never replacement)

- Web: axe-core, Accessibility Insights, Lighthouse, and browser developer tools.
- Android: Accessibility Scanner and Espresso accessibility checks where applicable.
- Apple platforms: Xcode Accessibility Inspector and XCTest accessibility support.
- Windows: Accessibility Insights for Windows and UI Automation inspection tools.
- Linux: Accerciser and AT-SPI inspection tools.
- Cross-platform: automated tests for keyboard paths, focus behavior, and accessible names where the framework exposes them.

Automated tools detect only a subset of accessibility defects. They cannot reliably judge whether a label is meaningful, whether reading order makes sense, whether instructions are understandable, or whether a workflow is usable.

### Release checklist

- [ ] Every control has a correct role, accessible name, state, and value.
- [ ] Every action works with keyboard-only input; focus is visible and logical.
- [ ] Screen-reader navigation and announcements are understandable and non-redundant.
- [ ] Forms expose labels, instructions, validation errors, and required status.
- [ ] Dialogs, menus, tabs, and dynamic content manage focus and announcements correctly.
- [ ] Text can be enlarged; content reflows; high-contrast/forced-colors modes remain usable.
- [ ] Color is never the only means of communicating information.
- [ ] Motion can be reduced; flashing and autoplay behavior are controlled.
- [ ] Charts, images, diagrams, and visualizations have equivalent text or structured data.
- [ ] Tests were performed on every supported platform with real assistive technology.
- [ ] Known limitations, workarounds, and unsupported combinations are documented.
- [ ] Users with disabilities have been included in usability testing before release.

## 19. Selection summary

For a new accessibility-critical interface, start with these defaults:

| Language / area | Preferred starting point |
|---|---|
| Python | PySide6/Qt Widgets or GTK 4; browser UI where suitable |
| JavaScript / TypeScript | Semantic HTML with a tested framework/component system |
| Java | Swing or JavaFX standard controls |
| Kotlin | Jetpack Compose on Android; Compose Multiplatform only after target-by-target verification |
| C | GTK 4 or native Windows controls/UI Automation |
| C++ | Qt 6 Widgets or GTK 4/gtkmm |
| C# | WPF/WinUI on Windows; .NET MAUI or Avalonia after platform testing |
| Julia | GTK.jl, Qt/QML integration, or a browser-based interface |
| Swift | SwiftUI; UIKit or AppKit where platform-specific control is needed |
| Rust | GTK 4, Slint with AccessKit, or Tauri with semantic web UI |
| Go | Wails with semantic web UI, or GTK bindings |
| Lua | Host-native UI, wxLua/IUP after verification, or a semantic web UI |
| R | Shiny with accessible HTML controls and data alternatives |
| HTML/CSS | Native semantic HTML and standards-based CSS |
| SQL | Accessible database client and host-language application |
| Bash / PowerShell | Accessible terminal output; native/web GUI when a GUI is required |

The safest default is not “choose the library with the longest accessibility feature list.” It is: choose mature semantic controls that integrate with the target operating system, minimize custom rendering, expose complete accessible information, and prove the result through assistive-technology testing.

## 20. Authoritative references

Standards and cross-platform guidance:

- [W3C Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C WAI-ARIA Overview](https://www.w3.org/WAI/standards-guidelines/aria/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [MDN: HTML as a basis for accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML)
- [MDN: Accessible web applications and widgets](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Accessible_web_applications_and_widgets)

Toolkit and platform references:

- [Qt: UI accessibility](https://www.qt.io/development/qt-framework/ui-accessibility)
- [Qt: QAccessible](https://doc.qt.io/qt-6/qaccessible.html)
- [GNOME Human Interface Guidelines: Accessibility](https://developer.gnome.org/hig/guidelines/accessibility.html)
- [GTK-rs: Accessibility](https://gtk-rs.org/gtk4-rs/stable/latest/book/accessibility.html)
- [wxPython: wx.Accessible](https://docs.wxpython.org/wx.Accessible.html)
- [Oracle: Java Accessibility](https://docs.oracle.com/javase/8/docs/technotes/guides/access/index.html)
- [Android: Accessibility principles](https://developer.android.com/guide/topics/ui/accessibility)
- [Jetpack Compose: Accessibility](https://developer.android.com/develop/ui/compose/accessibility)
- [Compose Multiplatform: Accessibility](https://kotlinlang.org/docs/multiplatform/compose-accessibility.html)
- [Microsoft: WPF accessibility](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/wpf-accessibility)
- [Microsoft: .NET MAUI semantic properties and accessibility](https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/accessibility)
- [Avalonia: Accessibility](https://docs.avaloniaui.net/docs/app-development/accessibility)
- [Apple: SwiftUI accessibility fundamentals](https://developer.apple.com/documentation/swiftui/accessibility-fundamentals)
- [Apple: Accessibility for UIKit](https://developer.apple.com/documentation/uikit/accessibility-for-uikit)
- [Apple: Accessibility for AppKit](https://developer.apple.com/documentation/appkit/accessibility-for-appkit)
- [AccessKit](https://accesskit.dev/)
- [Rust GTK: Accessibility](https://gtk-rs.org/gtk4-rs/stable/latest/book/accessibility.html)

Recheck framework documentation and supported platform matrices before adopting a library. Accessibility capabilities change across toolkit versions, operating systems, and assistive technologies.
