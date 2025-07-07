import argparse
import os 

from .utils import Artemis_UtilFunctionality
from .create import Artemis_CreateProject

class Artemis_ArgParser:
    def __init__(self) -> None:
        self.__artemis_functions = Artemis_UtilFunctionality()
        self.__artemis_create_project = Artemis_CreateProject()
        self.__parser: argparse.ArgumentParser = argparse.ArgumentParser("This is Artemis Argument Parser")
        self.__add_arguments()
        self.parser = self.__parser.parse_args()


        os.system("clear") if self.__artemis_functions.get_system_platform()['os_name'] == "Linux" else os.system("cls")

    '''
        The reason for using this private function is that we can add the arguments we want for the program.
        Example -> python main.py -name test -projectpath .. -compiler .. --description "prompt"
    '''
    def __add_arguments(self) -> None:
        self.__parser.add_argument("-name", help="This flag set project name", type=str)
        self.__parser.add_argument("-projectpath", help="This flag set project creation path [you can use also . .. ]", type=str)
        self.__parser.add_argument("-compiler", help="This flag set compiler that is wich exists in path of system", type=str)
        self.__parser.add_argument("-description", help="This flag set your general descriptions about the project", type=str)
        self.__parser.add_argument("-compilerbinpath", help="This flag set compiler path if there is no default compiler in environ variables.", type=str)
        self.__parser.add_argument("-compilerincludepath", help="This flag set compiler include path.", type=str)
        self.__parser.add_argument("-compilerlibpath", help="This flag set compiler lib or dll path")
        self.__parser.add_argument("-create", action="store_true", help="This flag, which defaults to true, is used to create the project.")
        self.__parser.add_argument("-run", action="store_true", help="This flag, which defaults to true, is used to compile and run the project.")
        self.__parser.add_argument("-build", action="store_true", help="This flag, which defaults to true, is used to compile the project.")
        self.__parser.add_argument("-lib", nargs="+", help="With this flag you can add the library or libraries you need.", type=str)
        self.__parser.add_argument("-platform", nargs="+", help="This flag set platform that you want to compile on it", type=str)


    def run(self) -> None:
        if self.parser.create:
            compilers_bin_path: list[str] = sorted(list(set(self.__artemis_functions.get_compilers_bin_path_list())))
            self.__artemis_create_project.print_compilers(compilers_bin_path)
        else:
            pass
        
