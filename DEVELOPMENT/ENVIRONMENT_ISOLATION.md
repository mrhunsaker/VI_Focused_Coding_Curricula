# Project Environments, Dependency Management, and Containers

## Why environment isolation matters

A development environment combines language runtimes, compilers, libraries, command-line tools, editor extensions, configuration, and operating-system dependencies. Projects often require incompatible versions of the same dependency. Installing everything globally makes projects interfere with one another and makes it difficult to reproduce a working setup elsewhere.

Keep project dependencies local and explicit where possible. Record versions and dependencies in project manifests, commit lockfiles where the ecosystem recommends them, and document the commands needed to create, verify, test, and update the environment. Avoid administrator privileges and system-wide package directories for ordinary project dependencies.

Isolation improves reproducibility, dependency compatibility, safer upgrades, system cleanliness, reviewability, and project-specific editor/tool configuration. It is not a substitute for security: review packages, update tools, avoid untrusted install scripts, and never commit credentials.

## Different tools isolate different things

| Tool type | Primary purpose | Does not do |
|---|---|---|
| Language environment (Python \`venv\`) | Isolates project packages | Does not isolate the operating system |
| Version manager (\`pyenv\`, rustup, Node version managers) | Selects runtime/compiler versions | Does not lock all project dependencies |
| Dependency manager and lockfile | Declares and resolves libraries | Does not necessarily isolate the runtime |
| Application installer (\`pipx\`) | Installs command-line apps in separate environments | Is not the project's importable-library environment |
| Container (Docker/Podman) | Packages user-space runtime, libraries, and tools | Does not automatically isolate host accessibility settings |
| Editor profile/workspace settings | Separates editor preferences and extensions | Does not isolate compilers or libraries |

A project can combine layers: a version manager selects the runtime, a project environment holds dependencies, and an editor workspace or container defines repeatable development behavior.

## Python tools

### \`venv\` and \`virtualenv\`

Python's built-in \`venv\` module is the recommended starting point for simple projects:

\`\`\`bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
\`\`\`

Windows PowerShell:

\`\`\`powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
\`\`\`

Install project dependencies after activation. Name the directory \`.venv\`, add it to \`.gitignore\`, and do not commit it. Run \`deactivate\` to leave the environment. Activation is a shell convenience; the environment's Python executable can also be invoked directly.

**virtualenv** is a third-party tool that predates \`venv\` and offers additional features and compatibility. It remains useful in some established workflows, but beginners should normally start with built-in \`venv\` unless a project specifies otherwise.

### \`pip\`

\`pip\` installs Python packages. Invoke it through the intended interpreter:

\`\`\`bash
python -m pip install requests
python -m pip show requests
python -m pip freeze
\`\`\`

Using \`python -m pip\` helps ensure the installer belongs to the intended interpreter. Avoid privileged global installs into an operating-system-managed Python. A project can list dependencies in \`requirements.txt\` and install them with \`python -m pip install -r requirements.txt\`; a plain requirements file is not automatically a complete lockfile.

### \`pip-tools\`

\`pip-tools\` supplies \`pip-compile\` and \`pip-sync\`. A project can maintain direct dependencies in \`requirements.in\`, compile pinned resolutions into \`requirements.txt\`, and synchronize the environment:

\`\`\`bash
python -m pip install pip-tools
pip-compile requirements.in
pip-sync requirements.txt
\`\`\`

This suits projects that want a transparent requirements-file workflow without a larger project manager. Review compiled dependency changes.

### \`pipx\`

\`pipx\` installs Python command-line applications into separate isolated environments. Use it for standalone tools such as formatters or documentation generators. Do not use it as a replacement for the active project's dependency environment.

### \`pyenv\`

\`pyenv\` selects and installs multiple Python interpreter versions, commonly on macOS and Linux. It manages the interpreter version, not the project's complete dependency set; combine it with \`venv\`, \`pip\`, or a project manager. **pyenv-win** is a separate Windows implementation; Unix installation instructions do not automatically apply. Windows users can also use the Python Install Manager or another supported runtime manager.

### Poetry

**Poetry** manages Python project metadata, dependency resolution, virtual environments, lockfiles, and package building/publishing workflows. \`pyproject.toml\` declares metadata and dependencies; \`poetry.lock\` records resolved versions. Poetry is useful when a project wants one integrated workflow, but it introduces conventions that are unnecessary for every beginner exercise. Follow the project's chosen commands rather than mixing unrelated install methods.

### uv

**uv** is a fast Python package and project tool. Depending on the workflow, it can manage Python versions, create project environments, resolve and lock dependencies, install packages, and run tools. A uv project commonly has \`pyproject.toml\`, \`uv.lock\`, and a local \`.venv\`. Use the project's documented \`uv sync\` and \`uv run\` commands.

Do not confuse uv with npm. uv is primarily a Python tool; there is no standard combined package manager called “uv-npm,” and uv does not replace Node.js package management.

### \`twine\`

\`twine\` uploads already-built Python distribution files to package indexes such as PyPI. It is a publishing utility, not an environment manager and is not normally needed to run beginner projects. Publishing requires release review and account credentials; never commit PyPI tokens or passwords.

### Conda

Conda is both an environment manager and package manager. It can create environments containing Python or other runtimes, Python packages, and compiled native libraries. It is common in scientific computing, data science, and numerical projects.

\`\`\`bash
conda create --name course-data python=3.12
conda activate course-data
conda install numpy pandas
conda env export --from-history
\`\`\`

**Advantages:** manages compiled/native dependencies alongside Python packages; environment definitions can describe more than Python libraries; prebuilt binaries can avoid local compilation; supports multiple named environments and runtime versions.

**Disadvantages:** adds another ecosystem, solver, and command set; environments can consume significant disk space; mixing Conda and pip can complicate resolution; channel configuration can confuse beginners; it is unnecessary for simple scripts with few dependencies.

Use Conda when the project specifies it or depends on scientific/native packages it manages well. When mixing package sources, prefer installing available Conda packages first and use pip only for packages unavailable through the selected Conda channels. Do not create both a Conda environment and a separate \`.venv\` for one project unless its documentation explains why.

## JavaScript/TypeScript: npm and npx

Node.js supplies the runtime. **npm** installs and manages project dependencies; \`package.json\` declares them and \`package-lock.json\` records resolved versions. **npx** runs package executables, often from local project dependencies; inspect unfamiliar package names and scripts before running them. Use \`npm install package-name\` for local dependencies and \`npm ci\` for clean automated installs when a committed lockfile is present.

pnpm and Yarn are alternatives with their own conventions and lockfiles. Use the manager selected by the repository; do not casually mix npm, pnpm, and Yarn lockfiles. Node version managers select runtime versions but do not replace dependency manifests and lockfiles.

## Rust: Cargo and rustup

**Cargo** is Rust's standard build system and package manager. It creates projects, resolves dependencies, builds, tests, and runs programs. \`Cargo.toml\` declares metadata and dependencies; application projects should normally commit \`Cargo.lock\` for reproducible builds. **rustup** manages Rust toolchains and targets and can select project-specific compiler versions through \`rust-toolchain.toml\`. Cargo manages project dependencies/builds; rustup selects the toolchain.

## Other language ecosystems

Use each language's normal project mechanism: Gradle/Maven for Java and Kotlin; NuGet and the .NET SDK for C#; Swift Package Manager for Swift; Julia's \`Project.toml\` and \`Manifest.toml\`; Go modules (\`go.mod\`, \`go.sum\`); LuaRocks for Lua; and appropriate system packages/build tools such as CMake, vcpkg, or Conan for C/C++. Do not add a dependency manager merely for its own sake. First identify whether a dependency is in the standard library, supplied by the operating system, or third-party, then follow the project's documented workflow.

## Containers: Docker and Podman

A container packages an application or development environment with its user-space filesystem, runtime, libraries, tools, and configuration. Containers share the host operating-system kernel; they are not full virtual machines. They are useful when projects require conflicting system libraries, compilers, SDKs, or command-line tools.

### Docker

**Docker is the required documented container format for this curriculum's VS Code instructions.** VS Code's Dev Containers workflow uses a Docker-compatible runtime and a \`.devcontainer/devcontainer.json\` configuration, commonly paired with a \`Dockerfile\` or Docker Compose file.

**Advantages:** the Dev Containers extension and VS Code documentation use Docker as the standard documented path; broad ecosystem support; project-specific operating-system packages and language toolchains can be declared; containers can be rebuilt or discarded; projects can use different system libraries without installing them all on the host.

**Disadvantages:** requires installing and maintaining Docker Engine or Docker Desktop; images and caches consume disk and download/build time; networking, file permissions, volume mounts, and host integration add complexity; containers share the host kernel and are not a complete security boundary; host screen readers and accessibility services do not automatically run inside or become isolated by a container.

### Podman

**Podman** is a container engine supporting many Docker-compatible command patterns and OCI images. It can run without a central daemon and supports rootless operation on supported systems.

**Advantages:** daemonless architecture; rootless workflows can reduce privileged-service requirements; familiar commands and image formats; useful on Linux systems preferring its service/security model.

**Disadvantages:** Docker-specific integrations, sockets, networking, volume semantics, and desktop tooling are not guaranteed to behave identically; VS Code Dev Containers may require a compatible socket and additional configuration; most beginner troubleshooting guides assume Docker; rootless operation can require adjustments.

**Curriculum rule:** use Docker in required VS Code Dev Containers instructions. Podman is an optional alternative for experienced users, only after verifying the operating system, Podman version, socket configuration, and VS Code extension compatibility.

## Optional VS Code container setup

Containers are optional; learners can complete the curriculum with local toolchains and project-local environments.

1. Install Docker using the official instructions for the host OS.
2. Verify \`docker --version\` and \`docker info\` in a terminal.
3. Install VS Code and the Microsoft **Dev Containers** extension.
4. Open the project folder and create \`.devcontainer/\`.
5. Add a project-specific \`Dockerfile\` and \`devcontainer.json\`.
6. Use the Command Palette command **Dev Containers: Reopen in Container**.
7. Verify the runtime/compiler version and run the project's tests in the integrated terminal.
8. Keep source files in the mounted workspace; ignore generated artifacts as appropriate.
9. Update the Dockerfile/configuration and rebuild when the toolchain changes.

Minimal illustrative Python example (replace versions and commands with the actual project's requirements):

\`Dockerfile\`:

\`\`\`dockerfile
FROM python:3.12-slim
WORKDIR /workspace
RUN python --version
\`\`\`

\`.devcontainer/devcontainer.json\`:

\`\`\`json
{
  "name": "Course Python Project",
  "build": { "dockerfile": "../Dockerfile" },
  "workspaceFolder": "/workspace",
  "customizations": { "vscode": { "extensions": [] } }
}
\`\`\`

For production course projects, pin a suitable base-image version and consider pinning its digest. Add only required, accessibility-reviewed extensions. Never bake secrets into an image or Dockerfile. Docker Compose can define projects that need multiple services.

### Theia IDE

Theia can be deployed as a hosted or local application and used in container-based development setups, but the workflow depends on the distribution and installed extensions. Do not assume that VS Code's Dev Containers extension or its commands exist in every Theia installation.

One optional pattern is to run the project container separately, mount the project directory, and use the container shell/build tools from Theia's terminal or task runner. Verify socket access, file permissions, terminal accessibility, and the exact Theia distribution. For hosted Theia, follow the administrator's approved container workflow rather than exposing a host Docker socket to an untrusted web application.

## Accessibility settings and project isolation

Containers isolate project software dependencies; **they do not automatically isolate host screen-reader, braille, keyboard, display, or operating-system accessibility settings**. A screen reader running on the host remains a host service. A container does not create a separate screen-reader session or guarantee that an editor extension is accessible.

To prevent one project's editor preferences or extensions from disrupting another project's workflow:

- Use separate VS Code **Profiles** when projects need different extension sets or editor preferences.
- Use project \`.vscode/settings.json\` only for settings that genuinely belong to that workspace and have been tested with the learner's access technology.
- Keep global accessibility preferences at user level unless a tested workspace-specific override is necessary.
- Use Dev Container configuration for project tools and approved extensions, not to force a screen-reader setting that may be wrong for another learner.
- In Theia, use separate workspaces or supported workspace-specific preferences where available, and verify the distribution's behavior.
- Record the tested OS, editor, screen reader, braille display, extensions, and relevant settings.

Editor profiles/workspace settings and containers provide different kinds of isolation: profiles separate editor behavior, while containers separate runtimes and system dependencies. Containers alone do not isolate accessibility preferences.

## Repeatable project checklist

Before beginning a project, record: (1) required runtime/compiler and version; (2) dependency manager and manifest; (3) lockfile/reproducibility mechanism; (4) project-local environment or container strategy; (5) install/sync, build, run, and test commands; (6) IDE and extensions; (7) global versus workspace accessibility settings; (8) safe dependency-update/rebuild procedure; (9) generated directories to ignore; and (10) how to recreate the environment without deleting source files.

A clean environment is part of reliable software engineering: it makes a project understandable, testable, maintainable, and reproducible by someone other than its original author.
