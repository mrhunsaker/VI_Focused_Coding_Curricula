# Project Environments, Dependency Management, and Development Containers

## Purpose

A project environment is the collection of language runtimes, compilers, libraries, tools, configuration, and data assumptions needed to work on a project. Environment isolation keeps one project's dependencies from unintentionally changing another project's behavior.

This lesson explains the concepts and common professional patterns. It is not an installation guide. Commands shown in language-specific pages are examples for recognizing project workflows; use those pages for the supported toolchain and commands.

For this curriculum, a repository-defined **Development Container (Dev Container)** is the preferred model when learners must use a consistent compiler, linter, formatter, test runner, and supporting system libraries. See [Development Editors, IDEs, and Project Development Containers](IDE_SETUP.md) for the broader editor and container-runtime discussion.

## Learning objectives

By the end of this lesson, learners should be able to:

1. Explain the difference between a language runtime, compiler, package manager, dependency, and project environment.
2. Describe why dependencies should be scoped to a project.
3. Identify common dependency manifests and lockfiles.
4. Explain the purpose of environment variables and secrets.
5. Distinguish virtual environments, development containers, application containers, virtual machines, and hosted workspaces.
6. Explain the roles and differences of Docker and Podman.
7. Describe how reproducible environments support linting, compilation, testing, and collaboration.

## Core vocabulary

- **Runtime:** software that executes a program, such as the Python interpreter, Node.js, Java Virtual Machine, .NET runtime, or Julia runtime.
- **Compiler:** software that translates source code into another representation, often machine code or bytecode.
- **Package:** a reusable unit of software distributed for use by other projects.
- **Dependency:** a package, runtime, tool, or service a project requires.
- **Package manager:** a tool that resolves, downloads, records, and sometimes executes dependencies.
- **Manifest:** a project file that declares metadata and direct dependencies.
- **Lockfile:** a generated record of resolved dependency versions and often integrity metadata, intended to make installations more repeatable.
- **Virtual environment:** an isolated language-level environment for a project, such as Python's .venv.
- **Container image:** a versioned template containing a filesystem and metadata from which containers are created.
- **Container:** an isolated process environment that shares the host operating-system kernel while isolating filesystem, process, and network resources according to its configuration.
- **Development Container (Dev Container):** a containerized development workspace, described by project metadata such as devcontainer.json, containing the tools and services needed to work on a codebase.
- **Container engine/runtime:** software that builds, creates, starts, and manages containers and images, such as Docker Engine or Podman.
- **Virtual machine:** a virtualized computer with its own guest operating system and kernel.
- **Hosted workspace:** a development environment provided remotely by an institution or service.

## Why isolation matters

Suppose Project A requires version 1 of a library and Project B requires version 2. Installing both as global packages can cause one project to break when the shared installation changes. Project-scoped dependencies make each project's requirements explicit.

Isolation improves reproducibility, testing, security review, maintenance, and collaboration. It does not guarantee safety: a malicious dependency can still execute code, and a container can still be misconfigured or granted excessive access.

## Common project records

| Ecosystem | Common manifest or project record | Locking or reproducibility record |
|---|---|---|
| Python | pyproject.toml | uv.lock or another tool-specific lockfile |
| JavaScript / TypeScript | package.json | package-lock.json, pnpm-lock.yaml, or yarn.lock |
| Java | pom.xml or Gradle build files | Wrapper and pinned plugin/dependency versions |
| Kotlin/JVM | Gradle build files | Gradle wrapper and dependency locking where used |
| .NET | .csproj and solution files | Central package management and lock files where configured |
| Rust | Cargo.toml | Cargo.lock |
| Go | go.mod | go.sum |
| Julia | Project.toml | Manifest.toml |
| Lua | rockspec or project-specific records | Tool- and project-specific lock/metadata files |

A lockfile should be reviewed and committed when the ecosystem and project policy call for it. It is not a replacement for understanding the manifest or keeping dependencies maintained.

## Project-level versus global installation

Global tools can be appropriate for shared command-line utilities or centrally managed machines. Application dependencies should normally be declared at project scope. Avoid installing libraries globally merely to make one lesson run.

A project should make its execution assumptions discoverable. A collaborator should be able to determine the required language version, dependencies, tests, and run command from the repository rather than private notes.

## Development Containers

A Dev Container is a project-scoped, reproducible environment for developing, building, linting, and testing software. It is different from a production container: a development image may include compilers, language servers, debuggers, test frameworks, formatters, linters, documentation tools, and shell utilities that should not be shipped in the final application image.

The [Development Containers Specification](https://containers.dev/) defines metadata that compatible editors and services can use. A project commonly stores the configuration in `.devcontainer/devcontainer.json`, with an optional Dockerfile and Compose file. The metadata identifies the image or build definition, workspace, development user, Features, editor customizations, environment variables, forwarded ports, and lifecycle commands.

### Why the course should prefer this model

A common learning environment prevents a large class of avoidable toolchain problems. For example, the instructor's linter and the learner's linter may otherwise use different rules or versions; the compiler may be newer or older; a native library may be missing; or a test runner may behave differently on different host systems.

A well-maintained course Dev Container can provide:

- The documented language runtime and compiler version.
- The exact linter, formatter, static analyzer, and test runner expected by the course.
- System libraries and headers required by compilation.
- Project build scripts and test dependencies.
- Common command-line utilities and documentation tools.
- A consistent shell and workspace layout.
- Optional supporting services such as a database when required by a project.

This is particularly valuable when the curriculum assesses compilation, linting, static analysis, and tests. The learner and instructor can run the same repository-defined checks in a known user-space environment. A container can also reduce host-specific installation requirements, though the host still needs a supported container engine and compatible editor or service.

### Example repository layout

```text
project/
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
│   └── compose.yaml          # optional
├── src/
├── tests/
├── scripts/
├── README.md
└── language-specific project and lock files
```

Not every project needs all these files. A simple project may reference a maintained development image. A project with additional system dependencies may use a Dockerfile. A project that requires multiple services may use Compose.

### Example responsibilities

| File or mechanism | Responsibility |
|---|---|
| devcontainer.json | Declares how a compatible tool should create or connect to the development environment |
| Dockerfile | Describes how a development image is built, including base image and system packages |
| Compose file | Describes multiple related containers and their networks, volumes, and service dependencies |
| Dev Container Features | Reusable configuration units that add common tools or capabilities |
| Project manifest | Declares language-level dependencies |
| Lockfile | Records resolved dependency versions for repeatable dependency resolution |
| scripts/ | Provides named, repeatable project commands for linting, building, testing, and other checks |

### Make project checks explicit

The project should expose stable, documented commands for formatting checks, linting, static analysis, compilation/build, unit and integration tests, expected-output checks, and documentation validation when relevant. Prefer scripts or task targets with clear names over undocumented sequences of terminal commands.

A useful quality workflow separates checks by purpose:

1. **Format check:** determines whether source formatting matches project policy; it should not silently rewrite submitted work when used as a check.
2. **Lint/static analysis:** identifies likely defects, unsafe patterns, and style violations.
3. **Compile/build:** checks syntax, types, linking, and build dependencies.
4. **Unit tests:** checks individual functions and components.
5. **Integration tests:** checks interactions between modules and services.
6. **Expected-output checks:** verifies examples against documented behavior.
7. **Clean-checkout verification:** ensures the project does not depend on untracked files or persistent state.

A Dev Container is not a substitute for continuous integration. CI should independently build and test a clean checkout using the documented toolchain. This prevents a learner's persistent container state from concealing missing dependencies or undeclared files.

### Reproducibility and maintenance

Avoid floating image tags such as latest when a tool update could alter compiler diagnostics or test behavior unexpectedly. Prefer explicit supported versions or immutable digests for controlled course environments. Pin language versions, Dev Container Features, and relevant system dependencies where reproducibility matters.

Changes to a base image, compiler, linter, or formatter are curriculum changes. Review them, run the validation suite, and record the toolchain baseline. Prebuilt images can reduce startup time for large classes, but they must be rebuilt and published when the course environment changes.

### Limitations

A container shares the host kernel; it is not a full virtual machine. Host operating system, CPU architecture, filesystem behavior, permissions, networking, and virtualization support can still affect the workflow. A container also does not guarantee that all graphical editor features or assistive technologies will work.

Use a Dev Container when it meaningfully improves consistency. Do not impose container administration on a beginner if a simpler environment meets the learning objectives. The course should provide an accessible fallback or institution-managed hosted workspace where local container support is unavailable.

## Docker and Podman

Docker and Podman are container engines and associated tooling. They build and manage images and containers; they are not themselves the Dev Container specification. A Dev Container is a development-environment description that a compatible tool uses with a container engine or service.

### Docker

[Docker](https://www.docker.com/) is a widely used container platform. Its ecosystem includes Docker Engine, Docker CLI, Docker Desktop, registries, image-building tools, and Docker Compose. Docker Engine commonly uses a long-running daemon to manage images, containers, networks, and volumes. Docker Desktop provides a managed experience on macOS and Windows, where Linux containers run within a lightweight Linux virtual machine.

Docker has broad adoption, extensive documentation, mature Compose workflows, and wide integration with developer tools. VS Code's Dev Containers documentation primarily describes Docker-based workflows, making Docker the most straightforward baseline when a course standardizes on the default VS Code Dev Containers experience.

Docker Desktop licensing and organizational use are subject to Docker's current terms. Institutions should review current licensing, administration, and data-handling requirements.

### Podman

[Podman](https://podman.io/) is an open-source container engine designed to manage OCI containers and images. On Linux it can operate without a central daemon and supports rootless containers, allowing many operations to run as an ordinary user. Podman provides a command-line interface familiar to Docker users and supports pods, image builds, registries, and Compose-oriented workflows through associated tooling.

On macOS and Windows, Linux containers require a Linux environment; Podman commonly uses a managed virtual machine called a Podman machine. On Linux, rootless operation can reduce the need for a privileged daemon, but it does not eliminate the need to understand user namespaces, storage, networking, and host permissions.

Podman can be attractive for Linux-based teaching labs, organizations prioritizing daemonless and rootless workflows, and teams that prefer open-source container tooling. It supports Docker-compatible interfaces for many common operations, but compatibility is not absolute. Compose behavior, networking, volume permissions, socket/API behavior, build features, and IDE integrations should be tested against the exact versions in use.

### Comparison

| Concern | Docker | Podman |
|---|---|---|
| Core model | Engine commonly managed by a daemon | Daemonless architecture on Linux; API service can be exposed when needed |
| Rootless use | Supported in specific configurations | A major design capability on Linux |
| macOS / Windows | Docker Desktop provides a managed Linux-container environment | Podman machine provides a managed Linux environment |
| CLI familiarity | Native Docker CLI | Docker-like CLI for many operations |
| Image format | OCI-compatible images and Docker ecosystem formats | OCI-compatible images |
| Multi-container workflows | Docker Compose is widely used | Compose-compatible workflows are available; verify compatibility |
| Dev Container integration | Common baseline for VS Code documentation and workflows | Possible through compatible interfaces/tooling; validate the exact combination |
| Common selection rationale | Broad adoption, mature ecosystem, straightforward editor support | Rootless/daemonless model, open-source preference, Linux host integration |

Neither engine is universally better. Selection depends on host operating system, institutional policy, editor integration, desired security model, and the exact features used by the project.

### Compatibility is not guaranteed

A project may conform to the Development Containers Specification while still depending on implementation-specific behavior. The specification describes metadata; it does not guarantee every editor, service, and container engine supports every property or lifecycle feature identically.

- **VS Code:** the Dev Containers extension is a mature implementation and its official documentation uses Docker as the standard engine workflow. Podman compatibility can depend on the Docker-compatible API endpoint and extension/runtime versions. Treat Podman as a validated alternative, not an automatic drop-in replacement.
- **Eclipse Theia:** Dev Container support depends on the specific Theia distribution and extensions included by its provider. Confirm that the deployed product supports the required specification features and selected engine.
- **Hosted workspaces:** a provider may implement the specification using managed infrastructure. Learners may not control the underlying engine or host.

Consult the [Development Containers supporting-tools directory](https://containers.dev/supporting/) and test the actual environment selected for the course.

## Environment variables and secrets

Environment variables provide configuration to a process without hard-coding machine-specific values into source code. Common uses include selecting a development mode, locating a service endpoint, or configuring a tool.

Secrets include passwords, access tokens, private keys, and database credentials. Do not commit secrets to source control, include them in screenshots, print them in logs, or paste them into public issue reports. Use institution-approved secret storage or local secret-injection mechanisms. A .env file is not automatically secure; it must be excluded from version control when it contains secrets, and the team must define how its values are distributed.

Do not bake credentials into container images, Dockerfiles, build arguments, or committed Dev Container metadata. Treat mounted credentials and forwarded agent sockets as sensitive host access. Validate required settings without revealing secret contents.

## Virtual machines and hosted workspaces

A virtual machine provides a more complete guest-operating-system boundary and is useful when a project requires a different operating system or kernel-level behavior. It generally consumes more resources than a container. Some desktop container products use a VM internally to provide a Linux kernel on macOS or Windows; this does not make each application container a separate VM.

Hosted workspaces can centralize toolchains and reduce local machine administration. They may be useful in classrooms, managed labs, and data platforms. They also introduce dependencies on network connectivity, account access, remote session stability, institutional policies, data location, and platform accessibility.

A cloud notebook or data platform is not identical to a local IDE. Notebook execution may retain state between cells, while a conventional program often starts in a fresh process. Learners should understand that distinction when reproducing results.

## Safe environment practices

- Work within the intended project directory.
- Read dependency names and versions before approving installation.
- Prefer trusted package registries and official project documentation.
- Review install scripts, image sources, build steps, and Dev Container Features when working with unfamiliar projects.
- Prefer a non-root user in the development container.
- Avoid running commands with administrator or root privileges unless the task genuinely requires them.
- Do not enable privileged mode or broad host mounts without a reviewed need.
- Do not mount the Docker or Podman control socket into a learner container unless the task explicitly requires it and the security implications have been reviewed.
- Do not disable security controls to make a development tool work.
- Keep secrets out of source code, terminal transcripts, image layers, and commits.
- Use synthetic data for coursework unless a governed data environment is explicitly approved.
- Do not delete environment folders until you have confirmed they contain no source files or personal work.
- Use version control to preserve source and project configuration, not generated caches or private credentials.

## Practical activity

Inspect a language project supplied by the instructor. Identify its source files, Dev Container metadata, image or Dockerfile, manifest, lockfile, runtime requirement, lint command, build command, and test command. Explain which files should be committed and which files are generated or machine-specific. Do not install or update dependencies as part of this inspection.

## Mastery checklist

- [ ] I can explain why dependencies should be isolated by project.
- [ ] I can distinguish a manifest from a lockfile.
- [ ] I can explain what a Dev Container provides and how it differs from a production container.
- [ ] I can identify where Dev Container metadata and image-build instructions are stored.
- [ ] I can explain how a project Dev Container can standardize compiler, linter, formatter, and test versions.
- [ ] I can distinguish Docker from Podman and describe a situation where each may be selected.
- [ ] I understand that Dev Container specification support and engine compatibility must be verified for the chosen editor.
- [ ] I can explain the roles of environment variables without exposing secrets.
- [ ] I can compare containers, virtual machines, and hosted workspaces.
- [ ] I can describe how CI independently verifies a clean project build and test run.
