import os
from .utils import Artemis_UtilFunctionality

class Artemis_CreateProject:
    def __init__(self):
        self.__main_compiler: list[str] = []
        self.__compiler_max_name_width: int = 0
        self.__artemis_functions = Artemis_UtilFunctionality()
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

        print(f"\n\033[1;47m{(self.__compiler_max_name_width * 2) * '-'}\033[0m")
        print("\033[0m")
    

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
        This function print name of compilers and path with .
    '''
    def print_compilers(self, compilers_bin_path) -> None:
        space: int = len(str(len(compilers_bin_path))) - 1
        self.__compiler_max_name_width = max(len(os.path.split(c)[1]) for c in compilers_bin_path)

        print(f"\033[1;49;31m[Compiler Name] {(self.__compiler_max_name_width - 9) * ' '} \033[1;49;31m [Compiler Path]\033[0m\n\n\033[1;47m{(self.__compiler_max_name_width + 
                self.__compiler_max_name_width) * '-'}\033[0m\n")

        for counter, compiler in enumerate(compilers_bin_path, start=1):
            if counter % self.__remainder == 0:
                space -= 1
                self.__remainder *= 10
            comp = os.path.split(compiler)
            comp_width = len(comp[1])
            print(f"\033[1;32m[{counter}]\033[0m{space * ' '} \033[1m->\033[0m \033[1;33m{comp[1]}\033[0m{' ' * (self.__compiler_max_name_width - comp_width)}\033[1m {comp[0]}\033[0m")

        print(f"\n\033[1;47m{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}\033[0m\n")
        self.__user_compiler_selections(compilers_bin_path)


    '''
        This function is used to get the user-selected compilers.
    '''
    def get_compilers_user_selection(self) -> list[str]:
        return self.__main_compiler