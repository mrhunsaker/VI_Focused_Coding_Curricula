# Development Editors, IDEs, and Project Development Containers

## Purpose and scope

An integrated development environment (IDE) combines source editing with language-aware services such as diagnostics, navigation, refactoring, debugging, testing, and project management. A code editor may provide many of these capabilities through extensions. The practical distinction is the depth of project and language tooling.

This reference identifies the development environments used or discussed in this curriculum and explains their appropriate roles. **It is not an installation guide for third-party IDEs.** Product descriptions are not instructions to install software, select extensions, configure accounts, or alter operating-system settings. Follow institution-approved technical support and vendor documentation for operational procedures.

The curriculum's general-purpose editor choices are **Visual Studio Code (VS Code)** and **Eclipse Theia**. They are distinct products, not interchangeable names for one application. The recommended project-environment model is to keep the development toolchain reproducible and project-scoped, preferably through a **Development Container (Dev Container)** when compiler, linter, formatter, test runner, or system-library consistency is important.

## Development Containers: the recommended project model

A **Development Container**, often shortened to *Dev Container*, is a containerized workspace configured specifically for software development. It is not merely a container that runs the finished application. It provides the language runtime, compiler, SDK, build tools, linters, formatters, test tools, libraries, and supporting command-line utilities needed to work on a repository.

The [Development Containers Specification](https://containers.dev/) defines a tool-neutral metadata format for describing such environments. A project commonly stores its configuration in `.devcontainer/devcontainer.json`, alongside an optional Dockerfile, Compose configuration, scripts, and supporting files. A compatible editor or service interprets that metadata and connects the development interface to the environment. The project can therefore document and version the toolchain as part of the repository rather than relying on undocumented differences between learners' computers. [Specification](https://containers.dev/) · [VS Code overview](https://code.visualstudio.com/docs/devcontainers/containers) · [Specification-supported tools](https://containers.dev/supporting)

### Why this is especially useful in a programming course

A course may require a compiler and runtime, a linter, a formatter, a test framework, a debugger, system headers or libraries, and a particular version of each. These tools interact. A learner may otherwise have a correct source file but an incompatible compiler, a missing system library, a linter version that reports different diagnostics, or a test runner that behaves differently from the instructor's.

A repository-defined Dev Container can standardize:

- **Language toolchains:** interpreters, compilers, SDKs, JDKs, and runtime versions.
- **Code quality tools:** linters, static analyzers, formatters, and documentation checkers.
- **Build and test tools:** build systems, test frameworks, coverage tools, and test data.
- **System dependencies:** headers, native libraries, and command-line utilities required by the project.
- **Editor integration:** supported language services and project-specific editor customizations.
- **Supporting services:** databases, message brokers, or other dependencies when a lesson genuinely requires them.
- **Reproducibility metadata:** pinned image versions, feature versions, environment variables that are not secrets, and documented lifecycle commands.

This can make a learning environment more predictable across Windows, macOS, and Linux hosts. The host still supplies the container runtime and operating-system kernel; the container supplies a controlled user-space environment. A container is not a full virtual machine and does not provide a different kernel.

### Typical project structure

A project may use a structure such as:

```text
project/
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
│   └── compose.yaml          # optional; for multi-service environments
├── src/
├── tests/
├── scripts/
├── README.md
└── language-specific project and lock files
```

Not every project needs all these files. A simple project may refer to a maintained development image directly. A project with additional system packages may build from a Dockerfile. A project that depends on multiple services may use Compose. The `.devcontainer` directory contains the development-environment description; source code and tests remain ordinary project files.

### What the configuration describes

A `devcontainer.json` commonly identifies or builds the development image, configures the workspace location, declares development-container Features, sets a non-root user, defines environment variables, forwards development ports, and describes lifecycle commands. Editor-specific customizations may identify extensions or settings for a compatible editor.

A Dockerfile describes how the image is built: its base image, system packages, users, and other image contents. Compose can describe a group of related services, such as a development workspace and a database. The Dev Container configuration ties the developer's workspace experience to these container resources.

Illustrative configuration (not a complete course image):

```json
{
  "name": "Course development environment",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "remoteUser": "vscode",
  "forwardPorts": [],
  "customizations": {
    "vscode": {
      "extensions": []
    }
  }
}
```

This example shows the shape of project metadata only. It does not install a compiler, select a language version, or constitute a ready-to-run environment. A real course repository must provide a maintained Dockerfile or image, explicit tool versions, validation commands, and any required features.

### Dev Containers as a teaching and assessment control

For this curriculum, an instructor can publish a known development environment for a language unit or project. The environment can include the exact compiler and linter versions used by automated checks. Learners then run the same project scripts locally inside the container that CI runs in a clean build environment.

A robust project should expose clear commands for tasks such as:

- formatting checks (for example, verify formatting without silently changing submitted files);
- linting and static analysis;
- compilation or build;
- unit tests and integration tests;
- expected-output checks for instructional examples;
- documentation and link validation where applicable.

These commands should be documented in the repository and, where practical, invoked by the same CI workflow. A Dev Container is a development convenience and consistency mechanism; **it does not replace continuous integration**. CI should independently build and test a clean checkout so that a learner's persistent container state cannot conceal missing files, undeclared dependencies, or order-dependent tests.

### Images, versions, and reproducibility

A development image is a versioned filesystem and toolchain template from which a container is created. For instructional use, avoid relying on floating tags such as `latest` when a change could alter compiler diagnostics or program behavior without a course revision. Prefer explicit supported release tags or immutable digests for controlled teaching environments. Pin language versions, package manager versions, Dev Container Features, and relevant system dependencies when reproducibility matters.

Rebuilds should be intentional and tested. Updating the base image, compiler, or linter can change warnings, formatting, generated files, or test behavior. Treat such changes as curriculum maintenance: review them, run the validation suite, and record the resulting toolchain baseline.

### Dev Containers and accessibility

A container does not automatically make an editor accessible. The editor may run on the host while language servers, compilers, and extensions run inside the container. This separation can improve consistency, but it also creates multiple components that must work together.

Evaluate keyboard navigation, screen-reader announcements, braille output, editor diagnostics, terminal interaction, build output, test results, debugger behavior, and remote-session focus. Check whether the editor's remote-development extension is accessible in the actual version used. Ensure that essential instructions and results are available as text. Do not require a graphical container dashboard or mouse-only workflow as the only way to complete an assignment.

### Risks and operational boundaries

Containers are isolation mechanisms, not guarantees of security. A development container may have access to mounted source files, network resources, credentials, and host resources. Treat untrusted images, Features, package install scripts, and workspace lifecycle commands as executable code.

- Use trusted base images and inspect their provenance.
- Prefer a non-root development user.
- Do not bake access tokens, passwords, SSH private keys, or personal data into an image or repository.
- Avoid mounting the container runtime's control socket into a learner's development container unless the task explicitly requires it and the security implications have been reviewed.
- Limit privileged mode, Linux capabilities, host networking, and broad host filesystem mounts.
- Keep source code in version control; do not commit generated container layers, caches, or secrets.
- Use synthetic data for coursework unless a governed data environment is explicitly approved.
- Consider resource quotas and lifecycle policies for shared institutional hosts.

## Container engines and tools: Docker and Podman

A Dev Container is the development-environment pattern and metadata; Docker and Podman are container engines/tooling that can build and run containers. They solve related but different parts of the workflow. The choice of engine affects compatibility, operations, security boundaries, and platform support.

### Docker

[Docker](https://www.docker.com/) is a widely used container platform. Its ecosystem includes the Docker Engine, Docker CLI, Docker Desktop, image registries, build tooling, and Compose. Docker Engine commonly uses a long-running daemon to manage images, containers, networks, and volumes. Docker Desktop packages a managed experience for macOS and Windows, where Linux containers generally run in a lightweight Linux virtual machine.

Docker has broad industry adoption and extensive documentation, image availability, Compose workflows, and integration with developer tooling. VS Code's Dev Containers documentation primarily describes a Docker-compatible workflow. This makes Docker the most straightforward baseline when an instructional environment is designed around the default VS Code Dev Containers experience.

Docker Desktop licensing and organizational use are subject to Docker's current terms. Institutional adoption should review licensing, administration, and data-handling requirements rather than assume every deployment has identical terms.

### Podman

[Podman](https://podman.io/) is an open-source container engine designed to manage OCI containers and images. On Linux it can operate without a central daemon and supports rootless containers, allowing many container operations to run under an ordinary user account. Podman also provides a command-line interface familiar to Docker users and supports pods, image builds, registries, and Compose-oriented workflows through associated tooling.

On macOS and Windows, Linux containers require a Linux environment; Podman commonly uses a managed virtual machine, called a Podman machine. On Linux, rootless operation can reduce the need for a privileged daemon, but it does not eliminate the need to understand user namespaces, storage, networking, and host permissions.

Podman can be attractive for Linux-based teaching labs, organizations prioritizing daemonless and rootless workflows, and teams that prefer open-source container tooling. It supports Docker-compatible interfaces for many common operations, but compatibility is not absolute. Compose behavior, networking, volume permissions, socket/API behavior, build features, and IDE integrations should be tested against the exact versions in use.

### Docker and Podman compared

| Concern | Docker | Podman |
|---|---|---|
| Core model | Engine commonly managed by a daemon | Daemonless architecture on Linux; API service can be exposed when needed |
| Rootless use | Supported in specific configurations | A major design capability on Linux |
| macOS / Windows | Docker Desktop provides a managed Linux-container environment | Podman machine provides a managed Linux environment |
| CLI familiarity | Native Docker CLI | Docker-like CLI for many operations |
| Image format | OCI-compatible images and Docker ecosystem formats | OCI-compatible images |
| Multi-container workflows | Docker Compose is widely used | Compose-compatible workflows are available, but compatibility should be checked |
| Dev Container integration | Common baseline for VS Code documentation and workflows | Possible through compatible interfaces/tooling, but validate the specific editor, extension, and runtime versions |
| Common selection rationale | Broad adoption, mature ecosystem, low-friction editor support | Rootless/daemonless model, open-source preference, Linux host integration |

Neither engine is universally better. The appropriate choice depends on the operating system, institutional policy, editor integration, desired security model, and the exact development-container features used by the project.

### Dev Container compatibility is a separate question

A project may conform to the Development Containers Specification while still depending on implementation-specific behavior. The specification describes metadata; it does not guarantee every editor, service, and container engine supports every property or lifecycle feature in the same way.

- **VS Code:** its Dev Containers extension is a mature implementation and its official documentation uses Docker as the standard engine workflow. Podman compatibility can depend on the Docker-compatible API endpoint and extension/runtime versions. Treat Podman as a validated alternative, not an automatic drop-in replacement.
- **Eclipse Theia:** Theia is an extensible platform, and support for Dev Containers depends on the specific Theia distribution and extensions included by its provider. Confirm that the deployed Theia product supports the required parts of the specification and the selected container engine.
- **Hosted workspaces and other tools:** platforms may implement the specification with managed infrastructure. Users may not control the underlying engine or host. Verify which configuration fields, Features, lifecycle hooks, and Compose patterns are supported.

The [Development Containers supporting-tools directory](https://containers.dev/supporting) lists implementations and services. Use it as a starting point, then test the actual environment selected for the course.

## Curriculum-supported editor choices

### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a cross-platform source-code editor with an extension ecosystem, integrated terminal, source control interface, language services, debugging interfaces, and workspace features. It is suitable for introductory programming and multi-language projects where learners benefit from a consistent editor across Python, JavaScript, TypeScript, Java, C-family languages, and other supported languages.

VS Code is an editor platform rather than a compiler or runtime. A language extension can provide syntax-aware editing and communicate with a language server, but the relevant compiler, interpreter, SDK, debugger, or external service remains a separate toolchain dependency. Its Dev Containers extension can connect the editor to a project-defined development container.

Accessibility considerations include keyboard operation, editor accessibility support, screen-reader announcements, accessible integrated terminal interaction, and the ability to inspect diagnostics and source-control changes without relying on color or spatial layout. Accessibility is version-, extension-, operating-system-, and assistive-technology-dependent. Validate the complete edit, run, debug, and test workflow with the learner's actual screen reader or other access technology.

### Eclipse Theia

[Eclipse Theia](https://theia-ide.org/) is an extensible IDE framework and platform for building desktop or browser-based development environments. It shares some interaction conventions and extension concepts with VS Code, but it is a separate project with its own release, packaging, extension compatibility, and product distribution decisions.

Theia is relevant to hosted development environments, institution-managed workspaces, cloud development platforms, and organizations that need to tailor an IDE experience. Its browser-based form can reduce the need for learners to manage a full local toolchain, but it introduces dependence on network access, remote workspace availability, browser accessibility, and the accessibility of the particular Theia distribution.

Do not assume that every VS Code extension works in every Theia deployment. Do not assume that a hosted Theia environment supports the Dev Containers Specification or a particular engine. Evaluate the actual distribution used by the course or institution.

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
| Introductory multi-language coursework | VS Code or an institution-provided Theia environment with a course Dev Container | Consistent editor and toolchain across tracks |
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

When evaluating any editor, IDE, Dev Container, or container runtime, assess the complete workflow rather than the source editor alone:

1. Keyboard access to files, navigation, search, diagnostics, terminal, debugging, testing, and source control.
2. Screen-reader announcement of editor text, punctuation, indentation, completion lists, diagnostics, and status changes.
3. Stable focus order and predictable focus restoration when panels, dialogs, remote sessions, and tool windows open and close.
4. Ability to inspect errors and warnings as text, navigate between them, and understand their source locations.
5. Ability to run and debug a program without relying on unlabeled icons, color-only indicators, drag-and-drop, or inaccessible graphical output.
6. Compatibility with the learner's operating system, screen reader, braille display, magnification, and keyboard configuration.
7. Whether the workflow depends on a cloud account, persistent network connection, remote desktop, container VM, or institution-managed permissions.
8. Whether source files remain accessible on the host and whether container file permissions preserve the learner's ability to edit and submit work.
9. Whether the container runtime, image build output, lifecycle commands, and terminal can be operated and understood without visual-only controls.
10. Whether the organization can provide an equivalent accessible route when a specialized interface is not accessible.

A tool should not be mandated solely because it is popular or used by a professional team. The instructional objective is programming competence; an IDE and container are means of supporting that objective. Provide an equivalent accessible route when a product interface blocks participation.

## Course expectation

Students should learn to create and manage source files, understand project folders, run programs, interpret diagnostics, and use version control concepts. Those skills transfer between editors and runtimes. When a course supplies a Dev Container, students should also understand what the environment provides, how to run the documented project checks, and why the environment definition is version-controlled. They are not expected to become container administrators.

The course does not require learners to master every product described here, and it does not prescribe installation or configuration steps for third-party IDEs.

## Further reading

- [Development Containers Specification](https://containers.dev/)
- [Development Containers supporting tools and services](https://containers.dev/supporting)
- [VS Code Dev Containers documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [Create a development container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
- [Docker documentation](https://docs.docker.com/)
- [Podman documentation](https://docs.podman.io/)
- [Podman Desktop documentation](https://podman-desktop.io/docs)
- [Visual Studio Code documentation](https://code.visualstudio.com/docs)
- [Eclipse Theia documentation](https://theia-ide.org/docs/)
- [JetBrains product documentation](https://www.jetbrains.com/help/)
- [Databricks documentation](https://docs.databricks.com/)
- [Jupyter documentation](https://docs.jupyter.org/)
- [Posit documentation](https://docs.posit.co/)
- [Visual Studio documentation](https://learn.microsoft.com/visualstudio/)
- [Xcode documentation](https://developer.apple.com/documentation/xcode)
- [Eclipse documentation](https://help.eclipse.org/)
