import argparse
import os 

from src.utils import Artemis_UtilFunctionality
from src.create import Artemis_CreateProject
from src.color import Artemis_Color

class Artemis_ArgParser:
    def __init__(self) -> None:
        self.__artemis_functions = Artemis_UtilFunctionality()
        self.__artemis_create_project = Artemis_CreateProject()
        self.__parser: argparse.ArgumentParser = argparse.ArgumentParser("This is Artemis Argument Parser")
        self.__add_arguments()
        self.args = self.__parser.parse_args()


        os.system("clear") if self.__artemis_functions.get_system_platform()['os_name'] == "Linux" else os.system("cls")

    '''
        The reason for using this private function is that we can add the arguments we want for the program.
        Example -> python main.py -name test -projectpath .. -compiler .. --description "prompt"
    '''
    def __add_arguments(self) -> None:
        # Core project settings
        self.__parser.add_argument("-name", help="Set project name (must start with letter/underscore, no spaces).", type=str)
        self.__parser.add_argument("-projectpath", help="Directory in which to create or operate on the project", type=str)
        self.__parser.add_argument("-description", help="Human-readable description for the project.", type=str)

        # Compiler & platform selection
        self.__parser.add_argument("-compiler", help="Compiler executable to use (e.g. gcc-14, clang, cl, aarch64-linux-gnu-gcc).", type=str)
        self.__parser.add_argument("-compilerbinpath", help="Explicit path to a compiler bin/ directory if not on PATH.", type=str)
        self.__parser.add_argument("-compilerincludepath", help="Extra include (-I) directories for compiler.", type=str)
        self.__parser.add_argument("-compilerlibpath", help="Extra library (-L) directories for compiler.", type=str)
        self.__parser.add_argument("-platform", nargs="+", help="Target architecture(s), e.g. x86_64, arm64, riscv64.", type=str)
        self.__parser.add_argument("-lib", nargs="+", help="Libraries to link against, e.g. pthread, stdc++.", type=str)

        # Primary actions
        self.__parser.add_argument("-create", action="store_true", help="Scaffold a new Artemis project.")
        self.__parser.add_argument("-build", action="store_true", help="Compile the project.")
        self.__parser.add_argument("-run", action="store_true", help="Compile (if needed) and run the project.")

        # Advanced build options
        self.__parser.add_argument("-jobs", help="Number of parallel compilation jobs (like make -jN).", type=int, default=1)
        self.__parser.add_argument("--use-cmake", action="store_true", help="Generate and use a CMakeLists.txt instead of hand-rolled commands.")
        self.__parser.add_argument("--use-meson", action="store_true", help="Generate and use a meson.build instead of hand-rolled commands.")
        self.__parser.add_argument("--matrix-build", nargs="*", help="Build for multiple compiler/platform combos in one go (specify as list or via config).", type=str)

        # Code quality & testing
        self.__parser.add_argument("--analyze", action="store_true", help="Run static analysis (clang-tidy, cppcheck) after build.")
        self.__parser.add_argument("--format", action="store_true", help="Auto-format source tree with clang-format or astyle.")
        self.__parser.add_argument("--create-test", metavar="TEST_NAME", help="Scaffold a unit-test stub (Google Test, Catch2, etc.).", type=str)

        # Docs, packaging & CI
        self.__parser.add_argument("--doc", action="store_true", help="Generate documentation (Doxygen/Sphinx) for the current project.")
        self.__parser.add_argument("--package", action="store_true", help="Package the build output (zip/tar, or DEB/RPM).")
        self.__parser.add_argument("--version-major", help="Major version to stamp in packages or binary metadata.", type=int)
        self.__parser.add_argument("--version-minor", help="Minor version to stamp in packages or binary metadata.", type=int)

        # Containerization & reproducible builds
        self.__parser.add_argument("--dockerize", action="store_true", help="Build inside a Docker container with the selected toolchain.")

        # Miscellaneous
        self.__parser.add_argument("--interactive", action="store_true", help="Launch an interactive TUI (using rich/prompt_toolkit) for choosing options.")
        self.__parser.add_argument("--watch", action="store_true", help="Watch source files and re-build on changes.")
        self.__parser.add_argument("--ai-init", metavar="PROMPT", help="Use AI to generate boilerplate code from a natural-language prompt.", type=str)


    """
        Handle the project creation workflow:
        - Detect available compilers
        - Prompt for compiler selection
        - Configure platform if none provided
        - Validate or prompt for project name
        - Print final project name
    """
    def __check_project_creation(self):
        if not self.args.create:
            return

        try:
            # Detect available compilers
            compilers = sorted(set(self.__artemis_functions.get_compilers_bin_path_list()))
            if not self.__artemis_create_project.print_compilers(compilers):
                return

            # Platform configuration
            if not self.args.platform:
                self.__artemis_create_project.platform_configuration()

            base_path = self.args.projectpath if self.args.projectpath else None
            name = self.args.name if self.args.name else None
            description = self.args.description if self.args.description else None
            self.__artemis_create_project.run_create(base_path=base_path, name=name, description=description)

        except Exception as err:
            print(f"Error during project creation: {err}")


    """
        Entry point: handle create, build, run in sequence.
    """
    def run(self) -> None:
        self.__check_project_creation()

        if self.args.build:
            pass
        if self.args.run:
            pass
