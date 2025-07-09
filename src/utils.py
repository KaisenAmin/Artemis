import os 
import platform

from src.color import Artemis_Color

class Artemis_UtilFunctionality:
    def __init__(self):
        self.__compilers_bin_paths: list[str] = [] 
        self.__compilers_absolute_path: list[str] = []
        self.__env_path: list[str] = os.environ.get("PATH", '').split(os.pathsep)
        self.__default_compiler_names: list[str] = [
            'c89',                       # POSIX C compiler (Linux)
            'c99',                       # POSIX C compiler (Linux)
            'c89-gcc',                   # GCC with C89 standard (Linux)
            'c99-gcc',                   # GCC with C99 standard (Linux)
            'cc',                        # C compiler, often symlink to gcc or clang (Linux)
            'c++',                       # C++ compiler, often symlink to g++ or clang++ (Linux)
            'gcc',                       # GNU C compiler (Linux)
            'g++',                       # GNU C++ compiler (Linux)
            'gcc-13',                    # GNU C compiler, version 13 (Linux)
            'g++-13',                    # GNU C++ compiler, version 13 (Linux)
            'clang',                     # LLVM C/C++ compiler (Linux)
            'clang++',                   # LLVM C++ compiler (Linux)
            'clang-18',                  # LLVM C/C++ compiler, version 18 (Linux)
            'clang++-18',                # LLVM C++ compiler, version 18 (Linux)
            'x86_64-linux-gnu-gcc',      # GNU C compiler for x86_64 (Linux)
            'x86_64-linux-gnu-g++',      # GNU C++ compiler for x86_64 (Linux)
            'x86_64-linux-gnu-gcc-13',   # GNU C compiler for x86_64, version 13 (Linux)
            'x86_64-linux-gnu-g++-13',   # GNU C++ compiler for x86_64, version 13 (Linux)
            'cl',                        # Microsoft C/C++ compiler (Windows)
            'x86_64-w64-mingw32-gcc',    # MinGW C compiler (Windows)
            'x86_64-w64-mingw32-g++',    # MinGW C++ compiler (Windows)
            'x86_64-w64-mingw32-clang',  # MinGW Clang C compiler (Windows)
            'x86_64-w64-mingw32-clang++',# MinGW Clang C++ compiler (Windows)
            'x86_64-w64-mingw32-cc',     # MinGW C compiler, alias (Windows)
            'x86_64-w64-mingw32-c++',    # MinGW C++ compiler, alias (Windows)
        ]
        self.__architecture: list[str] = ['x86_64', 'x86', 'arm64', 'arm', 'amd64', 'amd']


    def __find_compilers_path(self) -> list[str]:
        for path in self.__env_path:
            if any(value in path for value in self.__default_compiler_names) and path.endswith('bin'):
                if os.path.exists(path):
                    self.__compilers_bin_paths.append(path)

        for path in self.__compilers_bin_paths:
            list_of_compiler_names: list[str] = os.listdir(path)

            for bin_name in list_of_compiler_names:
                os_extension: bool = bin_name.endswith('.exe')
                if any(name + ".exe" == bin_name if os_extension else name == bin_name for name in self.__default_compiler_names):
                    self.__compilers_absolute_path.append(os.path.join(path, bin_name))
        
        return self.__compilers_absolute_path


    def __find_compilers_linux(self) -> list[str]:
        for file in os.listdir('/usr/bin'):
            if any(value in file for value in self.__default_compiler_names) and os.access(file, os.X_OK):
                self.__compilers_absolute_path.append(os.path.join("/usr/bin", file))
        
        print(self.__compilers_bin_paths)

        return self.__compilers_absolute_path

    '''
        This function returns a list of absolute paths to the compiler binaries.
    '''
    def get_compilers_bin_path_list(self) -> list[str]:
        plt: dict[str : str] = self.get_system_platform()

        if plt['os_name'] == 'Linux':
            return self.__find_compilers_linux()
        else:
            return self.__find_compilers_path()
    

    '''
        This function return a dictionary of three values os_name, system_architecture and machine_type(AMD ... Intel ..)
    '''
    def get_system_platform(self) -> dict[str:str]:
        os_name: str = platform.system()
        system_arch: tuple[str, str] = platform.architecture()
        machine_type: str = platform.machine()

        return {"os_name": os_name, "system_arch": system_arch, "machine_type": machine_type}
    

    '''
        This function returns a list of supported CPU architectures.
    '''
    def get_list_of_architecture(self) -> list[str]:
        return self.__architecture


    '''
        This function is used to show error messages in colorized format.
    '''
    def show_error_message(self, message: str, width: int) -> None:
        print(f"\n{Artemis_Color.DASH_WHITE_BACKGROUND.value} {(width -6) * '-'}{Artemis_Color.END_LINE.value} {Artemis_Color.RED.value}Exception{Artemis_Color.END_LINE.value} {Artemis_Color.DASH_WHITE_BACKGROUND.value}{(width -6) * '-'}{Artemis_Color.END_LINE.value}")
        
        print(f"{Artemis_Color.WHITE.value}{message}{Artemis_Color.END_LINE.value}")
        print(f"{Artemis_Color.DASH_WHITE_BACKGROUND.value}{width * 2 * '-'}{Artemis_Color.END_LINE.value}\n")