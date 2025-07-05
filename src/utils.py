import os 
import platform


class Artemis_UtilFunctionality:
    def __init__(self):
        self.__compilers_bin_paths: list[str] = [] 
        self.__compilers_absolute_path: list[str] = []
        self.__env_path: list[str] = os.environ.get("PATH", '').split(os.pathsep)
        self.__default_compiler_names: list[str] = ['g++', 'gcc', 'cl', 'clang', 'x86_64-w64-mingw32', 'llvm', 'x86_64-w64-mingw32-clang++','cc', 'c++', 
            'x86_64-w64-mingw32-cc', 'x86_64-w64-mingw32-clang', 'x86_64-w64-mingw32-c++', 'mingw64', 'mingw32', 'x86_64-w64-mingw32-g++', 'x86_64-w64-mingw32-gcc', 'x86_64-w64-mingw32-gcc-ar', 'x86_64-w64-mingw32-gcc-nm', 'clang++']


    def __find_compilers_path(self) -> list[str]:
        for path in self.__env_path:
            if any(value in path for value in self.__default_compiler_names) and path.endswith('bin'):
                self.__compilers_bin_paths.append(path)

        for path in self.__compilers_bin_paths:
            list_of_compiler_names: list[str] = os.listdir(path)

            for bin_name in list_of_compiler_names:
                os_extension: bool = bin_name.endswith('.exe')
                if any(name + ".exe" == bin_name if os_extension else name == bin_name for name in self.__default_compiler_names):
                    self.__compilers_absolute_path.append(os.path.join(path, bin_name))
        
        return self.__compilers_absolute_path
    

    '''
        This function returns a list of absolute paths to the compiler binaries.
    '''
    def get_compilers_bin_path_list(self) -> list[str]:
        return self.__find_compilers_path()
    
    
    '''
        This function return a dictionary of three values os_name, system_architecture and machine_type(AMD ... Intel ..)
    '''
    def get_system_platform(self) -> dict[str:str]:
        os_name: str = platform.system()
        system_arch: tuple[str, str] = platform.architecture()
        machine_type: str = platform.machine()

        return {"os_name": os_name, "system_arch": system_arch, "machine_type": machine_type}
    

    def show_error_message(self, message: str, width: int) -> None:
        print(f"\n\033[1;47m {(width -6) * '-'}\033[0m \033[1;31mException\033[0m \033[1;47m{(width -6) * '-'}\033[0m")
        print(message)
        print(f"\033[1;47m{width * 2 * '-'}\033[0m\n")