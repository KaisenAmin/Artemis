import os

from src.utils import Artemis_UtilFunctionality, SystemPlatform
from src.color import Artemis_Color 


class Artemis_CreateProject:
    def __init__(self):
        self.__main_compiler: list[str] = []
        self.__main_platform: list[str] = []
        self.__project_name: str = ""
        self.__compiler_max_name_width: int = 0
        self.__artemis_functions = Artemis_UtilFunctionality()
        self.__plt_config: SystemPlatform = self.__artemis_functions.get_system_platform()
        self.__remainder: int = 10


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

                if len(integer_user_compiler_input) < len(compiler_bin_path):
                    flag = False 
                    for i in integer_user_compiler_input:
                        if i > len(compiler_bin_path) or i < 0:
                            self.__artemis_functions.show_error_message("Please Select True Number from Compiler Tables", self.__compiler_max_name_width)
                            flag = True 
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
        
        print(f"{Artemis_Color.RED.value}[Compiler Name] {(self.__compiler_max_name_width - 9) * ' '} {Artemis_Color.RED.value} [Compiler Path]{Artemis_Color.END_LINE.value}\n\n{Artemis_Color.DASH_WHITE_BACKGROUND.value}{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}{Artemis_Color.END_LINE.value}\n")

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

        candidate = name
        while True:
            if candidate and self.check_project_name(candidate):
                break
            candidate = input(f"{Artemis_Color.BLUE.value}Enter project name (letters/digits/_, no leading digit): {Artemis_Color.END_LINE.value}").strip()
            if not candidate:
                self.__artemis_functions.show_error_message("Please Enter name for the project.", self.__compiler_max_name_width)
        # print(f"{Artemis_Color.WHITE.value}{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}{Artemis_Color.END_LINE.value}\n")

        print(f"\n{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value} {Artemis_Color.WHITE.value}->{Artemis_Color.WHITE.value} Your Project Name is [{Artemis_Color.RED.value}{self.get_project_name()}{Artemis_Color.END_LINE.value}]")
            
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
    def create_project_structure(self) -> None:
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


    """
        Full create workflow:
        1. Determine base path
        2. Determine project name
        3. Create project root directory named after project_name under base path
        4. Scaffold structure inside that directory
        5. Print summary
    """
    def run_create(self, base_path: str | None = None, name: str | None = None) -> None:
        base = self.set_project_path(base_path)
        project_name = self.set_project_name(name)
        project_dir = os.path.join(base, project_name)

        try:
            os.makedirs(project_dir, exist_ok=True)
            os.chdir(project_dir)
        except Exception as e:
            print(f"Error: could not create project directory '{project_dir}': {e}")
            return
      
        self.create_project_structure()

        cwd = os.getcwd()
        print(f"{Artemis_Color.GREEN.value}[Info]{Artemis_Color.END_LINE.value}{Artemis_Color.WHITE.value} ->{Artemis_Color.END_LINE.value} Project '{Artemis_Color.RED.value}{project_name}{Artemis_Color.END_LINE.value}' created at {Artemis_Color.RED.value}{cwd}{Artemis_Color.END_LINE.value}")
