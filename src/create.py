import os
from .utils import Artemis_UtilFunctionality

class Artemis_CreateProject:
    def __init__(self):
        self.__main_compiler: list[str] = []
        self.__compiler_max_name_width: int = 0
        self.__artemis_functions = Artemis_UtilFunctionality()

    '''
        This function is used to get user input for selecting compilers.
        It displays the available compilers and prompts the user to select one or more by number.
    '''
    def __user_compiler_selections(self, compiler_bin_path: list[str]):
        try:
            user_compiler_input: str | list[str] = input("\033[5;49;34mPlease Select Compiler or Compilers by Number [1 2 3 or <all>] : \033[0m").split(' ')
            integer_user_compiler_input: list[int] = list(map(int, user_compiler_input))

            if len(user_compiler_input) > 0:
                user_compiler_input = [compiler_bin_path[i - 1] for i in integer_user_compiler_input if i and 0 < i <= len(compiler_bin_path)]
                print(user_compiler_input)
                self.__main_compiler.extend(user_compiler_input)
            else:
                raise ValueError("Invalid compiler selection.")
        
        except ValueError as ve:
            self.__artemis_functions.show_error_message(f"\033[0;49;31mError ValueError : {ve}\nPlease enter Integer values only in Compiler Selection. \033[0m", self.__compiler_max_name_width)
        except Exception as e:
            self.__artemis_functions.show_error_message(f"\033[0;49;31mError ValueError : {e}\nPlease enter Integer values only in Compiler Selection. \033[0m", self.__compiler_max_name_width)


    '''
        This function print name of compilers and path with .
    '''
    def print_compilers(self, compilers_bin_path) -> None:
        space: int = len(str(len(compilers_bin_path))) - 1
        remainder: int = 10
        self.__compiler_max_name_width = max(len(os.path.split(c)[1]) for c in compilers_bin_path)

        print(f"\033[0;49;31m[Compiler Name] {(self.__compiler_max_name_width - 9) * ' '} \033[0;49;31m[Compiler Path]\n\n\033[7;49;97m{(self.__compiler_max_name_width + 
                self.__compiler_max_name_width) * '-'}\033[0m\n")

        for counter, compiler in enumerate(compilers_bin_path, start=1):
            if counter % remainder == 0:
                space -= 1
                remainder *= 10
            comp = os.path.split(compiler)
            comp_width = len(comp[1])
            print(f"\033[1;49;32m[{counter}]{space * ' '} -> {comp[1]} {' ' * (self.__compiler_max_name_width - comp_width)}\033[7;49;97m{comp[0]}\033[0m")

        print(f"\n\033[7;49;97m{(self.__compiler_max_name_width + self.__compiler_max_name_width) * '-'}\033[0m\n")
        self.__user_compiler_selections(compilers_bin_path)