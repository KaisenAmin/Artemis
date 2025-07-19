import os

from src.utils import Artemis_UtilFunctionality, SystemPlatform
from src.color import Artemis_Color 


class Artemis_CreateProject:
    def __init__(self):
        self.__main_compiler: list[str] = []
        self.__main_platform: list[str] = []
        self.__project_name: str = ""
        self.__compiler_max_name_width: int = 60  # Set minimum width
        self.__artemis_functions = Artemis_UtilFunctionality()
        self.__plt_config: SystemPlatform = self.__artemis_functions.get_system_platform()
        self.__remainder: int = 10
        self.__compiler_config: dict = {}  # Store compiler configuration
        self.__build_config: dict = {}  # Store build system configuration


    def __show_compilers_selected(self) -> None:
        if not self.__main_compiler:
            self.__artemis_functions.show_error_message("No Compiler Selected", self.__compiler_max_name_width)
            return 

        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value} {(self.__compiler_max_name_width - 10) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Compiler Selected{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 10) * '-'}{Artemis_Color.END_LINE.value}\n")
        
        space: int = len(str(len(self.__main_compiler))) - 1

        for counter, comp in enumerate(self.__main_compiler, start=1):
            if counter % self.__remainder == 0:
                space -= 1
                self.__remainder *= 10
            print(f"{Artemis_Color.GREEN.value}[{counter}]{space * ' '}{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}-> {comp}{Artemis_Color.END_LINE.value}")

        # print(f"\n\033[1;47m{(self.__compiler_max_name_width * 2) * '-'}\033[0m")
        # print("\033[0m")
    

    def __show_platform_selected(self) -> None:
        if not self.__main_platform:
            self.__artemis_functions.show_error_message("No compiler Selected", self.__compiler_max_name_width)
            return

        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value} {(self.__compiler_max_name_width - 10) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Platform Selected{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 10) * '-'}{Artemis_Color.END_LINE.value}\n")

        for counter, plt in enumerate(self.__main_platform, start=1):
            print(f"{Artemis_Color.GREEN.value}[{counter}]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}-> {plt}{Artemis_Color.END_LINE.value}")

    '''
        This function is used to get user input for selecting compilers.
        It displays the available compilers and prompts the user to select one or more by number.
    '''
    def __user_compiler_selections(self, compiler_bin_path: list[str]) -> bool:
        try:
            while True:
                user_compiler_input: str | list[str] = input(f"\n[{Artemis_Color.RED.value}User Input{Artemis_Color.END_LINE.value}]{Artemis_Color.WHITE.value} -> {Artemis_Color.END_LINE.value}{Artemis_Color.BLUE.value}Please Select Compiler or Compilers by Number [1 2 3 or <all>] : {Artemis_Color.END_LINE.value}").split(' ')
                integer_user_compiler_input: list[int] = list(map(int, user_compiler_input))

                # Check if all selected numbers are valid
                flag = False 
                for i in integer_user_compiler_input:
                    if i > len(compiler_bin_path) or i <= 0:
                        self.__artemis_functions.show_error_message("Please Select True Number from Compiler Tables", self.__compiler_max_name_width)
                        flag = True 
                        break
                if not flag:
                    break                 

            # print(compiler_bin_path)
            # print(integer_user_compiler_input)

            if len(user_compiler_input) > 0:
                user_compiler_input = [compiler_bin_path[i - 1] for i in integer_user_compiler_input if i and 0 < i <= len(compiler_bin_path)]
                self.__main_compiler.extend(user_compiler_input)
                self.__show_compilers_selected()
            else:
                raise ValueError("Invalid compiler selection.")
        
        except ValueError as ve:
            self.__artemis_functions.show_error_message(f"Error ValueError : {ve}\nPlease enter Integer values only in Compiler Selection.", self.__compiler_max_name_width)
        except Exception as e:
            self.__artemis_functions.show_error_message(f"Error ValueError : {e}\nPlease enter Integer values only in Compiler Selection.", self.__compiler_max_name_width)
        else:
            return True
        return False


    '''
        Prompts the user to select a target platform architecture for compilation, allowing the choice of one or more architectures
        from a provided list or defaulting to the preconfigured platform if no selection is made.
    '''
    def __user_platform_selection(self) -> None:
        plt_ans: str = input(f"[{Artemis_Color.RED.value}User Input{Artemis_Color.END_LINE.value}]{Artemis_Color.WHITE.value} -> {Artemis_Color.END_LINE.value}{Artemis_Color.BLUE.value}Do You Want to Enter other Arch for Compiler ? [Y|N] : {Artemis_Color.END_LINE.value}").lower()
        
        if plt_ans == 'y':
            # print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 7) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Platform List{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width -8) * '-'}{Artemis_Color.END_LINE.value}\n")
            # print("\n")
            print(f"\n{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}-> {Artemis_Color.WHITE.value} Your current {Artemis_Color.RED.value}Machine Type{Artemis_Color.END_LINE.value} or [{Artemis_Color.RED.value}Cpu Architecture{Artemis_Color.END_LINE.value}] is {Artemis_Color.RED.value}{self.__plt_config['machine_type']}{Artemis_Color.END_LINE.value} {Artemis_Color.END_LINE.value}")
            len_arch_list = len(self.__artemis_functions.get_list_of_architecture())
            for counter, plt in enumerate(self.__artemis_functions.get_list_of_architecture(), start=1):
                print(f"{Artemis_Color.GREEN.value}[{counter}]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}-> {plt.upper()}{Artemis_Color.END_LINE.value}")

           
            # print(f"\n{Artemis_Color.WHITE.value}{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}{Artemis_Color.END_LINE.value}\n")
            
            try:
                user_platform_selection: list[str] = input(f"\n[{Artemis_Color.RED.value}User Input{Artemis_Color.END_LINE.value}]{Artemis_Color.WHITE.value} -> {Artemis_Color.END_LINE.value}{Artemis_Color.BLUE.value}Please Select Platform or platforms [1,2, or ..] : {Artemis_Color.END_LINE.value}").split(' ')
                integer_user_platform_selection: list[int] = list(map(int, user_platform_selection))

                if len(integer_user_platform_selection) > 0 and len(integer_user_platform_selection) <= len(self.__artemis_functions.get_list_of_architecture()):
                    user_platform_selection = [self.__artemis_functions.get_list_of_architecture()[plt - 1] for plt in integer_user_platform_selection if plt >= 1 and plt <= len_arch_list]
                    self.__main_platform.extend(user_platform_selection)
                    self.__show_platform_selected()

            except ValueError as ve:
                self.__artemis_functions.show_error_message(f"Error ValueError : {ve}\nPlease enter Integer values only in Platform Selection.", self.__compiler_max_name_width)
            except Exception as e:
                self.__artemis_functions.show_error_message(f"Error ValueError : {e}\nPlease enter Integer values only in Compiler Selection.", self.__compiler_max_name_width)
        else:
            # print(f"\n{Artemis_Color.WHITE.value}{self.__compiler_max_name_width * 2 * '-'}{Artemis_Color.END_LINE.value}\n")
            
            print(f"\n{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.WHITE.value} The project is {Artemis_Color.RED.value}configured{Artemis_Color.END_LINE.value} to use the default platform {Artemis_Color.RED.value}{self.__plt_config['machine_type']}{Artemis_Color.END_LINE.value}\n{10 * ' '}and the corresponding {Artemis_Color.RED.value}compiler{Artemis_Color.END_LINE.value} for this architecture.")


    '''
        This function print name of compilers and path with .
    '''
    def print_compilers(self, compilers_bin_path) -> bool:
        space: int = len(str(len(compilers_bin_path))) - 1
        self.__compiler_max_name_width = max(len(os.path.split(c)[1]) for c in compilers_bin_path)
        
        # Set minimum width for better formatting
        min_width = 60
        self.__compiler_max_name_width = max(self.__compiler_max_name_width, min_width)
        
        # Calculate the actual display width needed for the dash line
        # Account for: [Compiler Name] + spaces + [Compiler Path] + some padding
        display_width = max(
            len("[Compiler Name]") + self.__compiler_max_name_width + len("[Compiler Path]") + 20,  # Header width
            max(len(f"[{i}] -> {os.path.split(c)[1]} {c.split(os.sep)[-2] if len(c.split(os.sep)) > 1 else ''}") for i, c in enumerate(compilers_bin_path, 1)),  # Max row width
            min_width * 2  # Minimum display width
        )
        
        print(f"{Artemis_Color.RED.value}[Compiler Name] {(self.__compiler_max_name_width - 9) * ' '} {Artemis_Color.RED.value} [Compiler Path]{Artemis_Color.END_LINE.value}\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{display_width * '-'}{Artemis_Color.END_LINE.value}\n")

        for counter, compiler in enumerate(compilers_bin_path, start=1):
            if counter % self.__remainder == 0:
                space -= 1
                self.__remainder *= 10
            comp = os.path.split(compiler)
            comp_width = len(comp[1])
            
            print(f"{Artemis_Color.GREEN.value}[{counter}]{Artemis_Color.END_LINE.value}{space * ' '} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}{comp[1]}{Artemis_Color.END_LINE.value}{' ' * (self.__compiler_max_name_width - comp_width)}{Artemis_Color.WHITE.value} {comp[0]}\033[0m")

        # print(f"\n{Artemis_Color.WHITE.value}{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}{Artemis_Color.END_LINE.value}\n")
        return self.__user_compiler_selections(compilers_bin_path)


    '''
        This function is used to get the user-selected compilers.
    '''
    def get_compilers_user_selection(self) -> list[str]:
        return self.__main_compiler
    

    '''
        This function is used to get the user-selected platforms.
    '''
    def get_platforms_user_selection(self) -> list[str]:
        return self.__main_platform
    

    '''
        This function is used to get project name
    '''
    def get_project_name(self) -> str:
        return self.__project_name
    

    '''
        This function return compiler path max character width
    '''
    def get_compiler_max_name_width(self) -> int:
        return self.__compiler_max_name_width
    

    '''
        This function returns the display width for consistent formatting
    '''
    def get_display_width(self, compilers_bin_path: list[str]) -> int:
        if not compilers_bin_path:
            return 120  # Default width if no compilers
        
        min_width = 60
        compiler_max_width = max(len(os.path.split(c)[1]) for c in compilers_bin_path)
        compiler_max_width = max(compiler_max_width, min_width)
        
        # Calculate the actual display width needed for the dash line
        display_width = max(
            len("[Compiler Name]") + compiler_max_width + len("[Compiler Path]") + 20,  # Header width
            max(len(f"[{i}] -> {os.path.split(c)[1]} {c.split(os.sep)[-2] if len(c.split(os.sep)) > 1 else ''}") for i, c in enumerate(compilers_bin_path, 1)),  # Max row width
            min_width * 2  # Minimum display width
        )
        return display_width
    

    '''
        Set compiler configuration for build process
    '''
    def set_compiler_config(self, config: dict) -> None:
        self.__compiler_config = config
    

    '''
        Get compiler configuration for build process
    '''
    def get_compiler_config(self) -> dict:
        return self.__compiler_config
    

    '''
        Set build configuration for build process
    '''
    def set_build_config(self, config: dict) -> None:
        self.__build_config = config
    

    '''
        Get build configuration for build process
    '''
    def get_build_config(self) -> dict:
        return self.__build_config
    

    '''
        set platform configuration for project
    '''
    def platform_configuration(self):
        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 14) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Platform (Cpu Arch) Config{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 14) * '-'}{Artemis_Color.END_LINE.value}\n")

        if self.__plt_config['machine_type'].lower() in self.__artemis_functions.get_list_of_architecture():
            # print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}-> {Artemis_Color.WHITE.value} Your current {Artemis_Color.RED.value}Machine Type{Artemis_Color.END_LINE.value} or [{Artemis_Color.RED.value}Cpu Architecture{Artemis_Color.END_LINE.value}] is {Artemis_Color.RED.value}{self.__plt_config['machine_type']}{Artemis_Color.END_LINE.value} {Artemis_Color.END_LINE.value}")
            
            # print(f"\n{Artemis_Color.WHITE.value}{self.__compiler_max_name_width * 2 * '-'}{Artemis_Color.END_LINE.value}\n")
            self.__user_platform_selection()


    '''
        Validate a project name to ensure it doesn't start with a digit and is a valid identifier. 
    '''
    def check_project_name(self, project_name: str) -> bool:
        # print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 10) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Check Project Name{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width -10) * '-'}{Artemis_Color.END_LINE.value}\n")
        try:
            if not project_name:
                self.__artemis_functions.show_error_message("Project name cannot be empty.", self.__compiler_max_name_width)
                return False
            if project_name[0].isdigit():
                self.__artemis_functions.show_error_message("Project name cannot start with a digit. Invalid project name\nprovided. Please provide a valid name.", self.__compiler_max_name_width)
                return False 
            if not project_name.isidentifier():
                self.__artemis_functions.show_error_message("Project name must be a valid identifier (letters, digits, underscores; no spaces or special characters).",
                    self.__compiler_max_name_width
                )
                return False 
            
            self.__project_name = project_name
            
            return True 

        except Exception as e:
            self.__artemis_functions.show_error_message(str(e), self.__compiler_max_name_width)
            return False
   
    """
        Prompt the user to input a project name and validate it.
        Continues prompting until a valid project name is provided.
    """
    def set_project_name(self, name: str | None = None) -> str:
        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 9) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Set Project Name{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 9) * '-'}{Artemis_Color.END_LINE.value}\n")

        while True:
            # Show suggestion if provided
            if name:
                print(f"{Artemis_Color.YELLOW.value}[Suggestion]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Suggested name: {Artemis_Color.RED.value}{name}{Artemis_Color.END_LINE.value}")
            
            candidate = input(f"{Artemis_Color.BLUE.value}Enter project name (letters/digits/_, no leading digit): {Artemis_Color.END_LINE.value}").strip()
        
            # If user presses Enter and there's a suggestion, use the suggestion
            if not candidate and name:
                candidate = name
                print(f"\n{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Using suggested name: {Artemis_Color.RED.value}{candidate}{Artemis_Color.END_LINE.value}")
            elif not candidate:
                self.__artemis_functions.show_error_message("Please Enter name for the project.", self.__compiler_max_name_width)
                continue
                
            if self.check_project_name(candidate):
                break

        print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.WHITE.value} Your Project Name is [{Artemis_Color.RED.value}{candidate}{Artemis_Color.END_LINE.value}]")
            
        self.__project_name = candidate
        return candidate

                    
    """
        Determine base directory for project creation.
        If base_path is provided, ensure it exists; otherwise prompt the user.
        Returns the absolute base path.
    """ 
    def set_project_path(self, base_path: str | None = None) -> str:
        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 9) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Set Project Path{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 9) * '-'}{Artemis_Color.END_LINE.value}\n")

        target = base_path
        while True:
            if target and os.path.isdir(target):
                print(f"\n{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Your Project Path is [{Artemis_Color.RED.value}{os.path.abspath(target)}{Artemis_Color.END_LINE.value}]")
                return os.path.abspath(target)

            if target:
                try:
                    os.makedirs(target, exist_ok=True)
                    print(f"\n{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Your Project Path is [{Artemis_Color.RED.value}{os.path.abspath(target)}{Artemis_Color.END_LINE.value}]")
                    return os.path.abspath(target)
                except Exception as e:
                    self.__artemis_functions.show_error_message(f"Failed to create path '{target}': {e}",self.__compiler_max_name_width)

            target = input(f"{Artemis_Color.BLUE.value}Enter base path for project (will be created if needed):{Artemis_Color.END_LINE.value}").strip()

            if not target:
                self.__artemis_functions.show_error_message("Project base path cannot be empty.", self.__compiler_max_name_width)
                target = None
                continue

    """
        Scaffold the directory layout inside current working directory:
        src/, include/, lib/, bin/, build/, tests/, docs/, third_party/{include,lib,bin}.
    """
    def create_project_structure(self, description: str | None = None) -> None:
        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 11) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Project Path Details{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 11) * '-'}{Artemis_Color.END_LINE.value}\n")
        dirs = [
            'src', 'include', 'lib', 'bin', 'build',
            'tests', 'docs',
            os.path.join('third_party', 'include'),
            os.path.join('third_party', 'lib'),
            os.path.join('third_party', 'bin')
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)

        main_cpp = os.path.join('src', 'main.cpp')
        if not os.path.exists(main_cpp):
            with open(main_cpp, 'w') as f:
                f.write("""#include <iostream>

int main() {
    std::cout << \"Hello, Artemis!\" << std::endl;
    return 0;
}
""")
        print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Project structure {Artemis_Color.RED.value}created{Artemis_Color.END_LINE.value}.")

        # Generate build configuration files if compiler config exists
        if self.__compiler_config:
            build_config = self.get_build_config()
            
            if build_config.get('use_cmake'):
                self.generate_cmake_lists()
            elif build_config.get('use_meson'):
                self.generate_meson_build()
                self.generate_src_meson_build()  # Generate src/meson.build
            else:
                # Default to Makefile
                self.generate_makefile()

        # Generate README.md with description
        readme_content = f"""# {self.__project_name}

{description or f"A C++ project created with Artemis."}

## Project Structure
- `src/` - Source files
- `include/` - Header files  
- `lib/` - Library files
- `bin/` - Executables
- `build/` - Build artifacts
- `tests/` - Test files
- `docs/` - Documentation
- `third_party/` - External dependencies

## Building
```bash
# Add build instructions here
```
"""
        
        with open('README.md', 'w') as f:
            f.write(readme_content)


    """
        Full create workflow:
        1. Determine base path
        2. Determine project name
        3. Create project root directory named after project_name under base path
        4. Scaffold structure inside that directory
        5. Print summary
    """
    def run_create(self, base_path: str | None = None, name: str | None = None, description: str | None = None) -> None:
        base = self.set_project_path(base_path)
        project_name = self.set_project_name(name)
        project_dir = os.path.join(base, project_name)

        try:
            os.makedirs(project_dir, exist_ok=True)
            os.chdir(project_dir)
        except Exception as e:
            print(f"Error: could not create project directory '{project_dir}': {e}")
            return
      
        self.create_project_structure(description=description)

        cwd = os.getcwd()
        print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value}{Artemis_Color.WHITE.value} ->{Artemis_Color.END_LINE.value} Project '{Artemis_Color.RED.value}{project_name}{Artemis_Color.END_LINE.value}' created at {Artemis_Color.RED.value}{cwd}{Artemis_Color.END_LINE.value}")


    """
        Generate a Makefile with the current compiler configuration
    """
    def generate_makefile(self) -> None:
        config = self.get_compiler_config()
        compilers = self.get_compilers_user_selection()
        
        if not compilers:
            return
        
        # Get the first selected compiler and its path
        selected_compiler = compilers[0]
        compiler_path = os.path.dirname(selected_compiler)
        compiler_name = os.path.basename(selected_compiler)
        
        # Determine C++ compiler based on selected compiler
        if 'gcc' in compiler_name and not 'g++' in compiler_name:
            cxx_compiler = selected_compiler.replace('gcc', 'g++')
        elif 'clang' in compiler_name and not 'clang++' in compiler_name:
            cxx_compiler = selected_compiler.replace('clang', 'clang++')
        else:
            # If it's already a C++ compiler or we can't determine, use the same
            cxx_compiler = selected_compiler
        
        makefile_content = f"""# Makefile generated by Artemis
# Project: {self.__project_name}

# Compilers (based on user selection)
CC = {selected_compiler}
CXX = {cxx_compiler}

# Compiler flags
CFLAGS = -Wall -Wextra -std=c99
CXXFLAGS = -Wall -Wextra -std=c++17

# Include directories
INCLUDES = {' '.join(f'-I{path}' for path in config.get('include_paths', []))}

# Library directories
LDFLAGS = {' '.join(f'-L{path}' for path in config.get('lib_paths', []))}

# Libraries
LIBS = {' '.join(f'-l{lib}' for lib in config.get('libraries', []))}

# Source files
SRC_DIR = src
BUILD_DIR = build
BIN_DIR = bin

# Find all source files
C_SOURCES = $(wildcard $(SRC_DIR)/*.c)
CXX_SOURCES = $(wildcard $(SRC_DIR)/*.cpp)
OBJECTS = $(C_SOURCES:$(SRC_DIR)/%.c=$(BUILD_DIR)/%.o) $(CXX_SOURCES:$(SRC_DIR)/%.cpp=$(BUILD_DIR)/%.o)

# Target executable
TARGET = $(BIN_DIR)/{self.__project_name}

# Default target
all: $(TARGET)

# Create directories
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

# Compile C files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

# Compile C++ files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp | $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Link executable
$(TARGET): $(OBJECTS) | $(BIN_DIR)
	$(CXX) $(OBJECTS) $(LDFLAGS) $(LIBS) -o $@

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR) $(BIN_DIR)

# Install (optional)
install: $(TARGET)
	cp $(TARGET) /usr/local/bin/

.PHONY: all clean install
"""
        
        with open('Makefile', 'w') as f:
            f.write(makefile_content)
        
        print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Generated {Artemis_Color.RED.value}Makefile{Artemis_Color.END_LINE.value} using {Artemis_Color.RED.value}{compiler_name}{Artemis_Color.END_LINE.value} from {Artemis_Color.RED.value}{compiler_path}{Artemis_Color.END_LINE.value}")


    """
        Generate CMakeLists.txt with the current compiler configuration
    """
    def generate_cmake_lists(self) -> None:
        config = self.get_compiler_config()
        compilers = self.get_compilers_user_selection()
        
        if not compilers:
            return
        
        # Get the first selected compiler and its path
        selected_compiler = compilers[0]
        compiler_path = os.path.dirname(selected_compiler)
        compiler_name = os.path.basename(selected_compiler)
        
        # Determine C++ compiler based on selected compiler
        if 'gcc' in compiler_name and not 'g++' in compiler_name:
            cxx_compiler = selected_compiler.replace('gcc', 'g++')
        elif 'clang' in compiler_name and not 'clang++' in compiler_name:
            cxx_compiler = selected_compiler.replace('clang', 'clang++')
        else:
            # If it's already a C++ compiler or we can't determine, use the same
            cxx_compiler = selected_compiler
        
        cmake_content = f"""# CMakeLists.txt generated by Artemis
# Project: {self.__project_name}

cmake_minimum_required(VERSION 3.10)
project({self.__project_name})

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set compiler based on user selection
set(CMAKE_C_COMPILER {selected_compiler})
set(CMAKE_CXX_COMPILER {cxx_compiler})

# Include directories
{chr(10).join(f'include_directories({path})' for path in config.get('include_paths', []))}

# Library directories
{chr(10).join(f'link_directories({path})' for path in config.get('lib_paths', []))}

# Find source files
file(GLOB_RECURSE SOURCES "src/*.cpp" "src/*.c")

# Create executable
add_executable({self.__project_name} ${{SOURCES}})

# Link libraries
{chr(10).join(f'target_link_libraries({self.__project_name} {lib})' for lib in config.get('libraries', []))}

# Set compiler flags
target_compile_options({self.__project_name} PRIVATE -Wall -Wextra)

# Install target
install(TARGETS {self.__project_name} DESTINATION bin)
"""
        
        with open('CMakeLists.txt', 'w') as f:
            f.write(cmake_content)
        
        print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Generated {Artemis_Color.RED.value}CMakeLists.txt{Artemis_Color.END_LINE.value} using {Artemis_Color.RED.value}{compiler_name}{Artemis_Color.END_LINE.value} from {Artemis_Color.RED.value}{compiler_path}{Artemis_Color.END_LINE.value}")
        
        # Validate CMake configuration
        self.__validate_cmake_configuration(selected_compiler, cxx_compiler, config)


    """
        Generate meson.build with the current compiler configuration
    """
    def generate_meson_build(self) -> None:
        config = self.get_compiler_config()
        compilers = self.get_compilers_user_selection()
        
        if not compilers:
            return
        
        # Get the first selected compiler and its path
        selected_compiler = compilers[0]
        compiler_path = os.path.dirname(selected_compiler)
        compiler_name = os.path.basename(selected_compiler)
        
        # Determine C++ compiler based on selected compiler
        if 'gcc' in compiler_name and not 'g++' in compiler_name:
            cxx_compiler = selected_compiler.replace('gcc', 'g++')
        elif 'clang' in compiler_name and not 'clang++' in compiler_name:
            cxx_compiler = selected_compiler.replace('clang', 'clang++')
        else:
            # If it's already a C++ compiler or we can't determine, use the same
            cxx_compiler = selected_compiler
        
        meson_content = f"""# meson.build generated by Artemis
# Project: {self.__project_name}

project('{self.__project_name}', 'cpp',
  version : '1.0.0',
  default_options : ['warning_level=3'])

# Set C++ standard
cpp = meson.get_compiler('cpp')
cpp_std = cpp.get_id() == 'msvc' ? 'c++17' : 'c++17'
add_project_arguments(cpp.get_supported_arguments(['-std=' + cpp_std]), language : 'cpp')

# Set compiler based on user selection
# Note: Meson will automatically detect the compiler from PATH
# You may need to set CC and CXX environment variables if using custom paths

# Include directories
{chr(10).join(f"incdir{i} = include_directories('{path}')" for i, path in enumerate(config.get('include_paths', [])))}

# Library dependencies
{chr(10).join(f"dep{i} = dependency('{lib}', required: true)" for i, lib in enumerate(config.get('libraries', [])))}

# Find source files
sources = []
subdir('src')

# Create executable
exe = executable('{self.__project_name}', sources,
  include_directories : {f"[{', '.join(f'incdir{i}' for i in range(len(config.get('include_paths', []))))}]" if config.get('include_paths') else "[]"},
  dependencies : {f"[{', '.join(f'dep{i}' for i in range(len(config.get('libraries', []))))}]" if config.get('libraries') else "[]"},
  link_args : {f"['-L{path}' for path in ['{chr(10).join(config.get('lib_paths', []))}']]" if config.get('lib_paths') else "[]"})

# Install
install(exe)
"""
        
        with open('meson.build', 'w') as f:
            f.write(meson_content)
        
        print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Generated {Artemis_Color.RED.value}meson.build{Artemis_Color.END_LINE.value} using {Artemis_Color.RED.value}{compiler_name}{Artemis_Color.END_LINE.value} from {Artemis_Color.RED.value}{compiler_path}{Artemis_Color.END_LINE.value}")
        
        # Validate Meson configuration
        self.__validate_meson_configuration(selected_compiler, cxx_compiler, config)

    """
        Generate src/meson.build with the current compiler configuration
    """
    def generate_src_meson_build(self) -> None:
        config = self.get_compiler_config()
        compilers = self.get_compilers_user_selection()
        
        if not compilers:
            return
        
        # Get the first selected compiler and its path
        selected_compiler = compilers[0]
        compiler_path = os.path.dirname(selected_compiler)
        compiler_name = os.path.basename(selected_compiler)
        
        src_meson_content = f"""# src/meson.build generated by Artemis
# Project: {self.__project_name}

# Find all source files in this directory
sources = [
  'main.cpp',
  # Add more source files here as needed
]

# Add sources to the parent project
sources += sources
"""
        
        with open('src/meson.build', 'w') as f:
            f.write(src_meson_content)
        
        print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.END_LINE.value} Generated {Artemis_Color.RED.value}src/meson.build{Artemis_Color.END_LINE.value} using {Artemis_Color.RED.value}{compiler_name}{Artemis_Color.END_LINE.value} from {Artemis_Color.RED.value}{compiler_path}{Artemis_Color.END_LINE.value}")


    """
        Validate CMake configuration and provide feedback
    """
    def __validate_cmake_configuration(self, c_compiler: str, cxx_compiler: str, config: dict) -> None:
        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 8) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}CMake Validation{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 8) * '-'}{Artemis_Color.END_LINE.value}")
        
        # Check if compilers exist
        c_compiler_exists = os.path.exists(c_compiler)
        cxx_compiler_exists = os.path.exists(cxx_compiler)
        
        if c_compiler_exists:
            print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} C compiler found: {Artemis_Color.WHITE.value}{c_compiler}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} C compiler not found: {Artemis_Color.WHITE.value}{c_compiler}{Artemis_Color.END_LINE.value}")
        
        if cxx_compiler_exists:
            print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} C++ compiler found: {Artemis_Color.WHITE.value}{cxx_compiler}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} C++ compiler not found: {Artemis_Color.WHITE.value}{cxx_compiler}{Artemis_Color.END_LINE.value}")
        
        # Check include paths
        include_paths = config.get('include_paths', [])
        if include_paths:
            print(f"\n{Artemis_Color.YELLOW.value}[Include Paths]{Artemis_Color.END_LINE.value}")
            for path in include_paths:
                if os.path.exists(path):
                    print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} Include path exists: {Artemis_Color.WHITE.value}{path}{Artemis_Color.END_LINE.value}")
                else:
                    print(f"{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} Include path not found: {Artemis_Color.WHITE.value}{path}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.YELLOW.value}[Info]{Artemis_Color.END_LINE.value} No include paths specified")
        
        # Check library paths
        lib_paths = config.get('lib_paths', [])
        if lib_paths:
            print(f"\n{Artemis_Color.YELLOW.value}[Library Paths]{Artemis_Color.END_LINE.value}")
            for path in lib_paths:
                if os.path.exists(path):
                    print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} Library path exists: {Artemis_Color.WHITE.value}{path}{Artemis_Color.END_LINE.value}")
                else:
                    print(f"{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} Library path not found: {Artemis_Color.WHITE.value}{path}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.YELLOW.value}[Info]{Artemis_Color.END_LINE.value} No library paths specified")
        
        # Check libraries
        libraries = config.get('libraries', [])
        if libraries:
            print(f"\n{Artemis_Color.YELLOW.value}[Libraries]{Artemis_Color.END_LINE.value}")
            for lib in libraries:
                print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} Library to link: {Artemis_Color.WHITE.value}{lib}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.YELLOW.value}[Info]{Artemis_Color.END_LINE.value} No libraries specified")
        
        # Provide build commands
        print(f"\n{Artemis_Color.YELLOW.value}[Build Commands]{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.WHITE.value}To build your project, run:{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.BLUE.value}mkdir build{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.BLUE.value}cd build{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.BLUE.value}cmake ..{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.BLUE.value}cmake --build .{Artemis_Color.END_LINE.value}")
        
        # Overall status
        if c_compiler_exists and cxx_compiler_exists:
            print(f"\n{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}CMake configuration is ready for building!{Artemis_Color.END_LINE.value}")
        else:
            print(f"\n{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}CMake configuration has issues. Please check compiler paths.{Artemis_Color.END_LINE.value}")
        
        print(f"{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 10) * 2 * '-'}{Artemis_Color.DASH_WHITE_BACKGROUND_END.value}\n")


    """
        Validate Meson configuration and provide feedback
    """
    def __validate_meson_configuration(self, c_compiler: str, cxx_compiler: str, config: dict) -> None:
        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 8) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.YELLOW.value}Meson Validation{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 8) * '-'}{Artemis_Color.END_LINE.value}")
        
        # Check if compilers exist
        c_compiler_exists = os.path.exists(c_compiler)
        cxx_compiler_exists = os.path.exists(cxx_compiler)
        
        if c_compiler_exists:
            print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} C compiler found: {Artemis_Color.WHITE.value}{c_compiler}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} C compiler not found: {Artemis_Color.WHITE.value}{c_compiler}{Artemis_Color.END_LINE.value}")
        
        if cxx_compiler_exists:
            print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} C++ compiler found: {Artemis_Color.WHITE.value}{cxx_compiler}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} C++ compiler not found: {Artemis_Color.WHITE.value}{cxx_compiler}{Artemis_Color.END_LINE.value}")
        
        # Check include paths
        include_paths = config.get('include_paths', [])
        if include_paths:
            print(f"\n{Artemis_Color.YELLOW.value}[Include Paths]{Artemis_Color.END_LINE.value}")
            for path in include_paths:
                if os.path.exists(path):
                    print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} Include path exists: {Artemis_Color.WHITE.value}{path}{Artemis_Color.END_LINE.value}")
                else:
                    print(f"{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} Include path not found: {Artemis_Color.WHITE.value}{path}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.YELLOW.value}[Info]{Artemis_Color.END_LINE.value} No include paths specified")
        
        # Check library paths
        lib_paths = config.get('lib_paths', [])
        if lib_paths:
            print(f"\n{Artemis_Color.YELLOW.value}[Library Paths]{Artemis_Color.END_LINE.value}")
            for path in lib_paths:
                if os.path.exists(path):
                    print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} Library path exists: {Artemis_Color.WHITE.value}{path}{Artemis_Color.END_LINE.value}")
                else:
                    print(f"{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} Library path not found: {Artemis_Color.WHITE.value}{path}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.YELLOW.value}[Info]{Artemis_Color.END_LINE.value} No library paths specified")
        
        # Check libraries
        libraries = config.get('libraries', [])
        if libraries:
            print(f"\n{Artemis_Color.YELLOW.value}[Libraries]{Artemis_Color.END_LINE.value}")
            for lib in libraries:
                print(f"{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} Library to link: {Artemis_Color.WHITE.value}{lib}{Artemis_Color.END_LINE.value}")
        else:
            print(f"{Artemis_Color.YELLOW.value}[Info]{Artemis_Color.END_LINE.value} No libraries specified")
        
        # Provide build commands
        print(f"\n{Artemis_Color.YELLOW.value}[Build Commands]{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.WHITE.value}To build your project, run:{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.BLUE.value}mkdir build{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.BLUE.value}cd build{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.BLUE.value}meson setup build{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.BLUE.value}meson compile -C build{Artemis_Color.END_LINE.value}")
        
        # Overall status
        if c_compiler_exists and cxx_compiler_exists:
            print(f"\n{Artemis_Color.GREEN.value}[✓]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}Meson configuration is ready for building!{Artemis_Color.END_LINE.value}")
        else:
            print(f"\n{Artemis_Color.RED.value}[✗]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}Meson configuration has issues. Please check compiler paths.{Artemis_Color.END_LINE.value}")
        
        print(f"{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width - 10) * 2 * '-'}{Artemis_Color.DASH_WHITE_BACKGROUND_END.value}\n")

