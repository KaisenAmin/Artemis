# Artemis

A Python-based tool for managing C/C++ projects, providing a unified interface for building, running, dependency management, and project creation with support for multiple compilers and architectures.

## Features
- **C/C++ Compiler Management**: Supports a wide range of compilers, including:
  - Native: `gcc`, `g++`, `clang`, `clang++`, and versions (e.g., `gcc-9` to `gcc-14`).
  - Cross-compilers: `aarch64-linux-gnu-gcc`, `arm-linux-gnueabihf-g++`, `riscv64-linux-gnu-gcc`, etc.
  - Windows: `cl` (MSVC), `x86_64-w64-mingw32-gcc`, and more.
  - Multilib: `gcc-multilib`, `g++-14-multilib`, etc.
- **Project Creation**: Validates and sets project names with a user-friendly CLI.
- **Platform Support**: Configures projects for architectures like `x86_64`, `arm64`, `arm`, `mips64`, `riscv64`.
- **Build and Run**: Compiles and executes C/C++ projects with selected compilers and platforms.
- **Dependency Management**: Planned support for resolving C/C++ libraries (future enhancement).
- **Cross-Platform**: Works on Linux (e.g., Kaisen Linux) and Windows, with Git integration.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/artemis.git
   cd artemis
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install C/C++ compilers (e.g., on Debian-based systems):
   ```bash
   sudo apt update
   sudo apt install gcc g++ clang gcc-14-aarch64-linux-gnu g++-14-riscv64-linux-gnu
   ```

## Usage
Run Artemis with command-line arguments to create, build, or run projects:
```bash
python main.py -name my_project -compiler gcc-14 -platform x86_64 -create
```
- **Flags**:
  - `-name`: Set project name (e.g., `my_project`).
  - `-compiler`: Specify compiler (e.g., `gcc-14`, `clang`).
  - `-platform`: Target architecture (e.g., `x86_64`, `arm64`).
  - `-create`: Create a new project.
  - `-build`: Compile the project.
  - `-run`: Compile and run the project.
  - `-lib`: Add libraries (e.g., `-lib pthread stdc++`).
  - `-projectpath`: Set project directory (e.g., `.` or `..`).

Example:
```bash
python main.py -name test_project -compiler aarch64-linux-gnu-gcc-14 -platform arm64 -create
```
This creates a project named `test_project` for the `arm64` architecture using `aarch64-linux-gnu-gcc-14`.

## Requirements
- Python 3.6+
- C/C++ compilers (e.g., GCC, Clang, MinGW for Windows)
- Linux (e.g., Debian Linux ...) or Windows x86_64

## Future Enhancements
- Dependency solver for C/C++ libraries.
- Virtual environment support for isolated builds.
- GUI for easier project management.

## License
MIT License