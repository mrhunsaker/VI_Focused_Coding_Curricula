# Development Editors and Integrated Development Environments

## Purpose and scope

An integrated development environment (IDE) combines source editing with language-aware services such as diagnostics, navigation, refactoring, debugging, testing, and project management. A code editor may provide some of these capabilities through extensions. The terms overlap in everyday use; the practical distinction is the depth of project and language tooling.

This reference identifies the development environments used or discussed in this curriculum and explains their appropriate roles. **It is not an installation, configuration, or setup guide.** Do not treat product descriptions as instructions to install software, select extensions, configure settings, or connect accounts. Follow institution-approved technical support and vendor documentation for those operational tasks.

The curriculum's general-purpose editor choices are **Visual Studio Code (VS Code)** and **Eclipse Theia**. They are distinct products, not interchangeable names for one application.

## Curriculum-supported editor choices

### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a cross-platform source-code editor with an extension ecosystem, integrated terminal, source control interface, language services, debugging interfaces, and workspace features. It is suitable for introductory programming and multi-language projects where learners benefit from a consistent editor across Python, JavaScript, TypeScript, Java, C-family languages, and other supported languages.

VS Code is an editor platform rather than a compiler or runtime. A language extension can provide syntax-aware editing and communicate with a language server, but the relevant compiler, interpreter, SDK, debugger, or external service remains a separate toolchain dependency.

Accessibility considerations include keyboard operation, editor accessibility support, screen-reader announcements, accessible integrated terminal interaction, and the ability to inspect diagnostics and source-control changes without relying on color or spatial layout. Accessibility is version-, extension-, operating-system-, and assistive-technology-dependent. Validate the complete edit, run, debug, and test workflow with the learner's actual screen reader or other access technology. An extension's presence in a marketplace is not evidence that its interface is accessible.

### Eclipse Theia

[Eclipse Theia](https://theia-ide.org/) is an extensible IDE framework and platform for building desktop or browser-based development environments. It shares some interaction conventions and extension concepts with VS Code, but it is a separate project with its own release, packaging, extension compatibility, and product distribution decisions.

Theia is relevant to hosted development environments, institution-managed workspaces, cloud development platforms, and organizations that need to tailor an IDE experience. Its browser-based form can reduce the need for learners to manage a full local toolchain, but it introduces dependence on network access, remote workspace availability, browser accessibility, and the accessibility of the particular Theia distribution.

Do not assume that every VS Code extension works in every Theia deployment. Do not assume that a hosted Theia environment has the same features, keyboard commands, screen-reader behavior, or permissions as another Theia-based product. Evaluate the actual distribution used by the course or institution.

## Other professional development environments

The following products are discussed for professional context. They are not required course dependencies, and this curriculum does not provide setup instructions for them.

### JetBrains IDE family

[JetBrains](https://www.jetbrains.com/) develops language- and workflow-focused IDEs. Its products are often selected when deep language intelligence, integrated refactoring, test discovery, framework support, and mature debugging workflows are important.

- **IntelliJ IDEA** is a general-purpose IDE particularly associated with Java and Kotlin development, JVM projects, build systems, and enterprise application work.
- **PyCharm** focuses on Python development, including project navigation, debugging, testing, virtual environments, scientific workflows, and web frameworks.
- **WebStorm** focuses on JavaScript, TypeScript, and web application development, with framework-aware navigation, refactoring, and testing support.
- **CLion** targets C and C++ development, including native build systems, debugger integration, and code analysis.
- **Rider** focuses on .NET development and is commonly used for C#, ASP.NET Core, and Unity workflows.
- **DataGrip** is a database IDE for querying, exploring, and managing relational and other supported data platforms.

JetBrains IDEs are relevant when a sustained project uses a language or ecosystem for which the corresponding IDE provides substantial integrated tooling. Product editions, licensing, supported platforms, and accessibility behavior vary. Assess the specific product and version rather than generalizing from one JetBrains IDE to the entire family.

### Databricks workspace and notebooks

[Databricks](https://www.databricks.com/) is a data and AI platform, not simply a general-purpose desktop IDE. Its workspace combines collaborative notebooks, data engineering workflows, SQL analytics, machine learning, governed data access, jobs, and managed compute. It is commonly used with Apache Spark and the lakehouse architecture.

Databricks notebooks support exploratory and collaborative work in languages such as Python, SQL, Scala, and R, depending on the runtime and workspace configuration. They are useful for data preparation, distributed processing, analytics, experimentation, and production data pipelines. Notebook execution is stateful: cells may depend on prior execution order and shared session state. This differs from a conventional source file executed as a fresh process. Professional workflows therefore need attention to reproducibility, dependency management, data permissions, compute cost, version control, and the distinction between exploratory analysis and production jobs.

The platform is a managed service with workspace-specific permissions, compute policies, and organizational governance. It is not a prerequisite for this introductory curriculum.

### JupyterLab and notebook environments

[JupyterLab](https://jupyter.org/) is a web-based interactive computing environment built around notebooks, consoles, terminals, and file-based project work. It is widely used in education, scientific computing, data analysis, and exploratory research. A notebook interleaves executable code, output, and explanatory text.

Notebook workflows are useful for incremental experimentation and communicating analysis. They can also conceal execution-order dependencies, mutable session state, and hidden environmental assumptions. Learners should understand the underlying language and runtime rather than treating a notebook as a substitute for programming fundamentals. Keyboard and screen-reader accessibility must be assessed with the exact notebook version and extensions in use.

### RStudio / Posit

[RStudio](https://posit.co/products/open-source/rstudio/) is an IDE strongly associated with R, statistical analysis, data visualization, Quarto, and reproducible research. It provides an integrated source editor, console, package and project workflows, debugging, and data-oriented tools. Posit also develops products and services for publishing and managing data applications and analytical work.

RStudio is especially relevant to statisticians, researchers, analysts, and teams whose work centers on R. The R language module in this curriculum is introductory; RStudio is contextual information, not a required platform.

### Microsoft Visual Studio

[Microsoft Visual Studio](https://visualstudio.microsoft.com/) is a full-featured IDE for Windows-centric development, especially .NET, C#, C++, desktop applications, and enterprise workloads. It is distinct from Visual Studio Code. Visual Studio typically provides a more integrated project-system and debugger experience for supported Microsoft development stacks.

### Xcode

[Xcode](https://developer.apple.com/xcode/) is Apple's IDE for developing software for Apple platforms, including iOS, iPadOS, macOS, watchOS, and tvOS. It integrates Swift and Objective-C editing, Apple SDKs, simulators, signing, testing, and application distribution workflows. Apple-platform application development generally depends on Xcode and the corresponding Apple toolchain.

### Eclipse IDE

[Eclipse IDE](https://www.eclipse.org/ide/) is a long-established extensible IDE platform with a strong history in Java and enterprise development, as well as support for other languages through project-specific tooling. It remains relevant in organizations with established Eclipse-based workflows, plugins, and build systems.

## Choosing an environment by task

| Work type | Typical environment fit | Why |
|---|---|---|
| Introductory multi-language coursework | VS Code or an institution-provided Theia environment | Consistent editing and terminal workflows across tracks |
| Java or Kotlin application development | IntelliJ IDEA; also VS Code or Eclipse in suitable projects | JVM-aware navigation, refactoring, build and test integration |
| Python application development | VS Code or PyCharm | Language services, testing, debugging, and environment awareness |
| Front-end JavaScript and TypeScript | VS Code or WebStorm | Type-aware editing and web-framework workflows |
| Native C and C++ | VS Code, CLion, or Visual Studio | Compiler, build-system, and debugger integration |
| .NET and C# | Visual Studio or Rider; VS Code for lighter workflows | .NET project and debugger support |
| Apple-platform applications | Xcode | Apple SDK, simulator, signing, and platform toolchain integration |
| Statistical analysis in R | RStudio / Posit | Statistical and reproducible-research workflows |
| Exploratory scientific computing | JupyterLab | Interactive code, narrative, and results |
| Enterprise data engineering and analytics | Databricks workspace | Distributed data processing, governed data, jobs, and collaborative notebooks |
| Database query and schema work | DataGrip or a database-specific client | Querying, schema exploration, and database-aware tooling |

These are common fits, not exclusive rules. A product's marketing category does not establish that it is appropriate for a particular course, accessible to a particular learner, or approved by an institution.

## Accessibility and procurement criteria

When evaluating any editor or IDE, assess the complete workflow rather than the source editor alone:

1. Keyboard access to files, navigation, search, diagnostics, terminal, debugging, testing, and source control.
2. Screen-reader announcement of editor text, punctuation, indentation, completion lists, diagnostics, and status changes.
3. Stable focus order and predictable focus restoration when panels, dialogs, or tool windows open and close.
4. Ability to inspect errors and warnings as text, navigate between them, and understand their source locations.
5. Ability to run and debug a program without relying on unlabeled icons, color-only indicators, drag-and-drop, or inaccessible graphical output.
6. Compatibility with the learner's operating system, screen reader, braille display, magnification, and keyboard configuration.
7. Whether the workflow depends on a cloud account, persistent network connection, remote desktop, or institution-managed permissions.
8. Whether the organization can provide a text-based alternative when a specialized interface is not accessible.

A tool should not be mandated solely because it is popular or used by a professional team. The instructional objective is programming competence; an IDE is a means of supporting that objective. Provide an equivalent accessible route when a product interface blocks participation.

## Course expectation

Students should learn to create and manage source files, understand project folders, run programs, interpret diagnostics, and use version control concepts. Those skills transfer between editors. The course does not require learners to master every product described here, and it does not prescribe installation or configuration steps for third-party IDEs.

## Further reading

- [Visual Studio Code documentation](https://code.visualstudio.com/docs)
- [Eclipse Theia documentation](https://theia-ide.org/docs/)
- [JetBrains product documentation](https://www.jetbrains.com/help/)
- [Databricks documentation](https://docs.databricks.com/)
- [Jupyter documentation](https://docs.jupyter.org/)
- [Posit documentation](https://docs.posit.co/)
- [Visual Studio documentation](https://learn.microsoft.com/visualstudio/)
- [Xcode documentation](https://developer.apple.com/documentation/xcode)
- [Eclipse documentation](https://help.eclipse.org/)
