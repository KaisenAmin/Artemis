# Artemis Feature Backlog & Roadmap

## 1. Build System Integrations
- **CMake / Meson**: Auto-generate `CMakeLists.txt` or `meson.build`.
- **Custom Plugins**: Allow Python hooks for codegen, protobuf, etc.

## 2. Dependency Management
- **Conan / vcpkg**: `–add-dep zlib@1.2.11` to fetch and link libraries.
- **Version Constraints**: Semantic versioning support in dependencies.

## 3. Quality & Analysis
- **Static Analysis**: Integrate `clang-tidy`, `cppcheck`.
- **Formatting**: `--format` with `clang-format` presets.
- **Unit Testing**: Scaffold Google Test / Catch2; `–create-test`.

## 4. Performance & Coverage
- **Coverage Reports**: `–coverage` to run `gcov`/`lcov` and open HTML.
- **Profiling**: `–profile` to instrument with `gprof` or `perf`.

## 5. Containers & Reproducibility
- **Docker Mode**: `–dockerize` to build inside preconfigured images.
- **Nix / Bazel**: Experimental support for purely functional builds.

## 6. User Experience
- **TUI / Interactive CLI**: Use `rich` or `prompt_toolkit` for menu-driven flows.
- **Live-Reload**: Watch sources and rebuild on save.

## 7. CI/CD & IDE
- **GitHub Actions / GitLab CI**: Auto-generate YAML that runs Artemis.
- **VSCode / CLion**: Emit `.vscode/tasks.json`, launch configs, CMake profiles.

## 8. Embedded & Bare-Metal
- **Linker Scripts**: Prebuilt configs for common MCUs (Cortex-M, RISC-V).
- **OpenOCD Integration**: Flash and debug firmware.

## 9. Packaging & Distribution
- **RPM / DEB Generation**: `–package` to build system installers.
- **Cross-Platform Archives**: `.zip`, `.tar.gz` bundles.

## 10. AI-Assisted Workflows
- **LLM‐Based Boilerplate**: `–ai-init "parse JSON"` to stub code.
- **Intelligent Suggestions**: Warn about missing headers, libraries.

