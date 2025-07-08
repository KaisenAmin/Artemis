import os
from src.utils import Artemis_UtilFunctionality

class Artemis_CreateProject:
    def __init__(self):
        self.__main_compiler: list[str] = []
        self.__main_platform: list[str] = []
        self.__compiler_max_name_width: int = 0
        self.__artemis_functions = Artemis_UtilFunctionality()
        self.__plt_config: dict[str: str] = self.__artemis_functions.get_system_platform()
        self.__remainder: int = 10


    def __show_compilers_selected(self) -> None:
        if not self.__main_compiler:
            self.__artemis_functions.show_error_message("No Compiler Selected", self.__compiler_max_name_width)
            return 

        print(f"\n\033[1;47m {(self.__compiler_max_name_width - 10) * '-'}\033[0m \033[1;33mCompiler Selected\033[0m \033[1;47m{(self.__compiler_max_name_width - 10) * '-'}\033[0m\n")
        space: int = len(str(len(self.__main_compiler))) - 1

        for counter, comp in enumerate(self.__main_compiler, start=1):
            if counter % self.__remainder == 0:
                space -= 1
                self.__remainder *= 10
            print(f"\033[1;32m[{counter}]{space * ' '}\033[0m \033[1m-> \033[0m\033[1m{comp}\033[0m")

        # print(f"\n\033[1;47m{(self.__compiler_max_name_width * 2) * '-'}\033[0m")
        # print("\033[0m")
    

    def __show_platform_selected(self):
        if not self.__main_platform:
            self.__artemis_functions.show_error_message("No compiler Selected", self.__compiler_max_name_width)
            return 
        
        print(f"\n\033[1;47m {(self.__compiler_max_name_width - 10) * '-'}\033[0m \033[1;33mPlatform Selected\033[0m \033[1;47m{(self.__compiler_max_name_width - 10) * '-'}\033[0m\n")

        for counter, plt in enumerate(self.__main_platform, start=1):
            print(f"\033[1;32m[{counter}] \033[0m \033[1m-> \033[0m\033[1m{plt}\033[0m")
    
    '''
        This function is used to get user input for selecting compilers.
        It displays the available compilers and prompts the user to select one or more by number.
    '''
    def __user_compiler_selections(self, compiler_bin_path: list[str]) -> None:
        try:
            user_compiler_input: str | list[str] = input("\033[1;49;34mPlease Select Compiler or Compilers by Number [1 2 3 or <all>] : \033[0m").split(' ')
            integer_user_compiler_input: list[int] = list(map(int, user_compiler_input))

            if len(user_compiler_input) > 0:
                user_compiler_input = [compiler_bin_path[i - 1] for i in integer_user_compiler_input if i and 0 < i <= len(compiler_bin_path)]
                self.__main_compiler.extend(user_compiler_input)
                self.__show_compilers_selected()
            else:
                raise ValueError("Invalid compiler selection.")
        
        except ValueError as ve:
            self.__artemis_functions.show_error_message(f"\033[0;49;37mError ValueError : {ve}\nPlease enter Integer values only in Compiler Selection. \033[0m", self.__compiler_max_name_width)
        except Exception as e:
            self.__artemis_functions.show_error_message(f"\033[0;49;37mError ValueError : {e}\nPlease enter Integer values only in Compiler Selection. \033[0m", self.__compiler_max_name_width)


    '''
        Prompts the user to select a target platform architecture for compilation, allowing the choice of one or more architectures
        from a provided list or defaulting to the preconfigured platform if no selection is made.
    '''
    def __user_platform_selection(self):
        plt_ans: str = input("\033[1;49;34mDo You Want to Enter other Arch for Compiler ? [Y|N] : \033[0m").lower()
        
        if plt_ans == 'y':
            print(f"\n\033[1;47m{(self.__compiler_max_name_width - 7) * '-'}\033[0m \033[1;33mPlatform List\033[0m \033[1;47m{(self.__compiler_max_name_width -8) * '-'}\033[0m\n")
            len_arch_list = len(self.__artemis_functions.get_list_of_architecture())
            for counter, plt in enumerate(self.__artemis_functions.get_list_of_architecture(), start=1):
                print(f"\033[1;32m[{counter}]\033[0m \033[1m-> \033[0m\033[1m{plt.upper()}\033[0m")
            print(f"\n\033[1m{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}\033[0m\n")
            try:
                user_platform_selection: list[str] = input("\033[1;49;34mPlease Select Platform or platforms [1,2, or ..] : \033[0m").split(' ')
                integer_user_platform_selection: list[int] = list(map(int, user_platform_selection))
                if len(integer_user_platform_selection) > 0 and len(integer_user_platform_selection) <= len(self.__artemis_functions.get_list_of_architecture()):
                    user_platform_selection = [self.__artemis_functions.get_list_of_architecture()[plt - 1] for plt in integer_user_platform_selection if plt >= 1 and plt <= len_arch_list]
                    self.__main_platform.extend(user_platform_selection)
                    self.__show_platform_selected()
            except ValueError as ve:
                self.__artemis_functions.show_error_message(f"\033[0;49;37mError ValueError : {ve}\nPlease enter Integer values only in Platform Selection. \033[0m", self.__compiler_max_name_width)
            except Exception as e:
                self.__artemis_functions.show_error_message(f"\033[0;49;37mError ValueError : {e}\nPlease enter Integer values only in Compiler Selection. \033[0m", self.__compiler_max_name_width)
        else:
            print(f"\n\033[1m{self.__compiler_max_name_width * 2 * '-'}\033[0m\n")
            print(f"\033[1;32m[Info]\033[0m \033[1m->\033[0m \033[1m The project is \033[1;49;31mconfigured\033[0m to use the default platform \033[1;49;31m{self.__plt_config['machine_type']}\033[0m and the corresponding \033[1;49;31mcompiler\033[0m for this architecture.")


    '''
        This function print name of compilers and path with .
    '''
    def print_compilers(self, compilers_bin_path) -> None:
        space: int = len(str(len(compilers_bin_path))) - 1
        self.__compiler_max_name_width = max(len(os.path.split(c)[1]) for c in compilers_bin_path)

        print(f"\033[1;49;31m[Compiler Name] {(self.__compiler_max_name_width - 9) * ' '} \033[1;49;31m [Compiler Path]\033[0m\n\n\033[1;47m{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}\033[0m\n")

        for counter, compiler in enumerate(compilers_bin_path, start=1):
            if counter % self.__remainder == 0:
                space -= 1
                self.__remainder *= 10
            comp = os.path.split(compiler)
            comp_width = len(comp[1])
            print(f"\033[1;32m[{counter}]\033[0m{space * ' '} \033[1m->\033[0m \033[1;33m{comp[1]}\033[0m{' ' * (self.__compiler_max_name_width - comp_width)}\033[1m {comp[0]}\033[0m")

        print(f"\n\033[1m{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}\033[0m\n")
        self.__user_compiler_selections(compilers_bin_path)


    '''
        This function is used to get the user-selected compilers.
    '''
    def get_compilers_user_selection(self) -> list[str]:
        return self.__main_compiler
    

    def platform_configuration(self):
        print(f"\n\033[1;47m{(self.__compiler_max_name_width - 14) * '-'}\033[0m \033[1;33mPlatform (Cpu Arch) Config\033[0m \033[1;47m{(self.__compiler_max_name_width - 14) * '-'}\033[0m\n")
        
        if self.__plt_config['machine_type'].lower() in self.__artemis_functions.get_list_of_architecture():
            print(f"\033[1;32m[Info]\033[0m \033[1m-> \033[0m \033[1mYour current \033[1;49;31mMachine Type\033[0m or [\033[1;49;31mCpu Architecture\033[0m] is \033[1;49;31m{self.__plt_config['machine_type']}\033[0m \033[0m")
            print(f"\n\033[1m{self.__compiler_max_name_width * 2 * '-'}\033[0m\n")
            self.__user_platform_selection()