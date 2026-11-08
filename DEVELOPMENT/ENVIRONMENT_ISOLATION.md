# Project Environments, Dependency Management, and Containers

## Purpose

A project environment is the collection of language runtimes, libraries, tools, configuration, and data assumptions needed to work on a project. Environment isolation keeps one project's dependencies from unintentionally changing another project's behavior.

This lesson explains the concepts and common professional patterns. It is not an installation guide. Commands shown in language-specific pages are examples for recognizing project workflows; use those pages for the supported toolchain and commands.

## Learning objectives

By the end of this lesson, learners should be able to:

1. Explain the difference between a language runtime, package manager, dependency, and project environment.
2. Describe why dependencies should be scoped to a project.
3. Identify common dependency manifests and lockfiles.
4. Explain the purpose of environment variables and secrets.
5. Distinguish virtual environments, containers, virtual machines, and hosted workspaces.
6. Describe how a reproducible environment supports testing and collaboration.

## Core vocabulary

- **Runtime:** software that executes a program, such as the Python interpreter, Node.js, Java Virtual Machine, .NET runtime, or Julia runtime.
- **Compiler:** software that translates source code into another representation, often machine code or bytecode.
- **Package:** a reusable unit of software distributed for use by other projects.
- **Dependency:** a package, runtime, tool, or service a project requires.
- **Package manager:** a tool that resolves, downloads, records, and sometimes executes dependencies.
- **Manifest:** a project file that declares metadata and direct dependencies.
- **Lockfile:** a generated record of resolved dependency versions and often integrity metadata, intended to make installations more repeatable.
- **Virtual environment:** an isolated language-level environment for a project, such as Python's .venv.
- **Container:** a packaged process environment that shares the host operating-system kernel while isolating filesystem, process, and network resources according to its configuration.
- **Virtual machine:** a virtualized computer with its own guest operating system.
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

## Environment variables and secrets

Environment variables provide configuration to a process without hard-coding machine-specific values into source code. Common uses include selecting a development mode, locating a service endpoint, or configuring a tool.

Secrets include passwords, access tokens, private keys, and database credentials. Do not commit secrets to source control, include them in screenshots, print them in logs, or paste them into public issue reports. Use institution-approved secret storage or local secret-injection mechanisms. A .env file is not automatically secure; it must be excluded from version control when it contains secrets, and the team must define how its values are distributed.

Configuration should distinguish non-secret defaults from sensitive values. Validate required settings at program startup and report missing configuration without revealing secret contents.

## Containers and virtual machines

Containers are useful when a project needs a predictable user-space environment, a specific system library, or a repeatable service topology. They are widely used in development, continuous integration, and deployment. Container images should be versioned deliberately, kept current, and built from trusted sources.

A virtual machine provides a more complete guest-operating-system boundary and is useful when the project requires a different operating system or kernel-level behavior. It generally consumes more resources than a container.

Neither technology removes the need to understand the underlying toolchain. Containers can introduce additional complexity involving filesystem mounts, networking, permissions, device access, and assistive technology. A container-based workflow should not be required for a beginner when a simpler project environment meets the learning objective.

## Hosted and cloud workspaces

Hosted workspaces can centralize toolchains and reduce local machine administration. They may be useful in classrooms, managed labs, and data platforms. They also introduce dependencies on network connectivity, account access, remote session stability, institutional policies, data location, and platform accessibility.

A cloud notebook or data platform is not identical to a local IDE. Notebook execution may retain state between cells, while a conventional program often starts in a fresh process. Learners should understand that distinction when reproducing results.

## Safe environment practices

- Work within the intended project directory.
- Read dependency names and versions before approving installation.
- Prefer trusted package registries and official project documentation.
- Review install scripts and build steps when working with unfamiliar projects.
- Avoid running commands with administrator or root privileges unless the task genuinely requires them.
- Do not disable security controls to make a development tool work.
- Keep secrets out of source code, terminal transcripts, and commits.
- Do not delete environment folders until you have confirmed they contain no source files or personal work.
- Use version control to preserve source and project configuration, not generated caches or private credentials.

## Practical activity

Inspect a language project supplied by the instructor. Identify its source files, manifest, lockfile, runtime requirement, test command, and run command. Explain which files should be committed and which files are generated or machine-specific. Do not install or update dependencies as part of this inspection.

## Mastery checklist

- [ ] I can explain why dependencies should be isolated by project.
- [ ] I can distinguish a manifest from a lockfile.
- [ ] I can identify the environment record used by a language track.
- [ ] I can explain the role of environment variables without exposing secrets.
- [ ] I can compare virtual environments, containers, virtual machines, and hosted workspaces.
- [ ] I can describe how environment isolation supports reproducible testing.
