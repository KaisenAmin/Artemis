import os 
import platform
from typing import TypedDict

from src.color import Artemis_Color

class SystemPlatform(TypedDict):
    os_name: str
    system_arch: tuple[str, str]
    machine_type: str

class Artemis_UtilFunctionality:
    def __init__(self):
        self.__compilers_bin_paths: list[str] = [] 
        self.__compilers_absolute_path: list[str] = []
        self.__env_path: list[str] = os.environ.get("PATH", '').split(os.pathsep)
        
        self.__default_compiler_names: list[str] = [
            # Native GCC/G++ compilers
            'gcc', 'g++',
            'gcc-9', 'g++-9',
            'gcc-10', 'g++-10',
            'gcc-11', 'g++-11',
            'gcc-12', 'g++-12',
            'gcc-13', 'g++-13',
            'gcc-14', 'g++-14',
            'mingw64', 'mingw32',
            'ucrt64',
            # POSIX-compliant and generic C compilers
            'c89', 'c99', 'c89-gcc', 'c99-gcc', 'cc', 'c++',
            # Clang compilers (from /usr/bin)
            'clang', 'clang++', 'clang-18', 'clang++-18',
            # Cross-compilers for key architectures (GCC/G++ versions 9–14)
            'aarch64-linux-gnu-gcc', 'aarch64-linux-gnu-g++',
            'aarch64-linux-gnu-gcc-9', 'aarch64-linux-gnu-g++-9',
            'aarch64-linux-gnu-gcc-10', 'aarch64-linux-gnu-g++-10',
            'aarch64-linux-gnu-gcc-11', 'aarch64-linux-gnu-g++-11',
            'aarch64-linux-gnu-gcc-12', 'aarch64-linux-gnu-g++-12',
            'aarch64-linux-gnu-gcc-13', 'aarch64-linux-gnu-g++-13',
            'aarch64-linux-gnu-gcc-14', 'aarch64-linux-gnu-g++-14',
            'arm-linux-gnueabihf-gcc', 'arm-linux-gnueabihf-g++',
            'arm-linux-gnueabihf-gcc-9', 'arm-linux-gnueabihf-g++-9',
            'arm-linux-gnueabihf-gcc-10', 'arm-linux-gnueabihf-g++-10',
            'arm-linux-gnueabihf-gcc-11', 'arm-linux-gnueabihf-g++-11',
            'arm-linux-gnueabihf-gcc-12', 'arm-linux-gnueabihf-g++-12',
            'arm-linux-gnueabihf-gcc-13', 'arm-linux-gnueabihf-g++-13',
            'arm-linux-gnueabihf-gcc-14', 'arm-linux-gnueabihf-g++-14',
            'i686-linux-gnu-gcc', 'i686-linux-gnu-g++',
            'i686-linux-gnu-gcc-9', 'i686-linux-gnu-g++-9',
            'i686-linux-gnu-gcc-10', 'i686-linux-gnu-g++-10',
            'i686-linux-gnu-gcc-11', 'i686-linux-gnu-g++-11',
            'i686-linux-gnu-gcc-12', 'i686-linux-gnu-g++-12',
            'i686-linux-gnu-gcc-13', 'i686-linux-gnu-g++-13',
            'i686-linux-gnu-gcc-14', 'i686-linux-gnu-g++-14',
            'x86-64-linux-gnu-gcc', 'x86-64-linux-gnu-g++',
            'x86-64-linux-gnu-gcc-9', 'x86-64-linux-gnu-g++-9',
            'x86-64-linux-gnu-gcc-10', 'x86-64-linux-gnu-g++-10',
            'x86-64-linux-gnu-gcc-11', 'x86-64-linux-gnu-g++-11',
            'x86-64-linux-gnu-gcc-12', 'x86-64-linux-gnu-g++-12',
            'x86-64-linux-gnu-gcc-13', 'x86-64-linux-gnu-g++-13',
            'x86-64-linux-gnu-gcc-14', 'x86-64-linux-gnu-g++-14',
            'mips64el-linux-gnuabi64-gcc', 'mips64el-linux-gnuabi64-g++',
            'mips64el-linux-gnuabi64-gcc-9', 'mips64el-linux-gnuabi64-g++-9',
            'mips64el-linux-gnuabi64-gcc-10', 'mips64el-linux-gnuabi64-g++-10',
            'mips64el-linux-gnuabi64-gcc-11', 'mips64el-linux-gnuabi64-g++-11',
            'mips64el-linux-gnuabi64-gcc-12', 'mips64el-linux-gnuabi64-g++-12',
            'mips64el-linux-gnuabi64-gcc-13', 'mips64el-linux-gnuabi64-g++-13',
            'mips64el-linux-gnuabi64-gcc-14', 'mips64el-linux-gnuabi64-g++-14',
            'riscv64-linux-gnu-gcc', 'riscv64-linux-gnu-g++',
            'riscv64-linux-gnu-gcc-9', 'riscv64-linux-gnu-g++-9',
            'riscv64-linux-gnu-gcc-10', 'riscv64-linux-gnu-g++-10',
            'riscv64-linux-gnu-gcc-11', 'riscv64-linux-gnu-g++-11',
            'riscv64-linux-gnu-gcc-12', 'riscv64-linux-gnu-g++-12',
            'riscv64-linux-gnu-gcc-13', 'riscv64-linux-gnu-g++-13',
            'riscv64-linux-gnu-gcc-14', 'riscv64-linux-gnu-g++-14',
            # Multilib compilers
            'gcc-multilib', 'g++-multilib',
            'gcc-9-multilib', 'g++-9-multilib',
            'gcc-10-multilib', 'g++-10-multilib',
            'gcc-11-multilib', 'g++-11-multilib',
            'gcc-12-multilib', 'g++-12-multilib',
            'gcc-13-multilib', 'g++-13-multilib',
            'gcc-14-multilib', 'g++-14-multilib',
            # Windows compilers (MinGW and MSVC)
            'cl',
            'x86_64-w64-mingw32-gcc',
            'x86_64-w64-mingw32-g++',
            'x86_64-w64-mingw32-clang',
            'x86_64-w64-mingw32-clang++',
            'x86_64-w64-mingw32-cc',
            'x86_64-w64-mingw32-c++',
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
                os_extension: bool = os.access(os.path.join(path, bin_name), os.X_OK)
                if any(name + ".exe" == bin_name if os_extension else name == bin_name for name in self.__default_compiler_names):
                    self.__compilers_absolute_path.append(os.path.join(path, bin_name))
            
        return self.__compilers_absolute_path


    def __find_compilers_linux(self) -> list[str]:
        for file in os.listdir('/usr/bin'):
            if any(value == file for value in self.__default_compiler_names) and os.access(f"/usr/bin/{file}", os.X_OK):
                self.__compilers_absolute_path.append(os.path.join("/usr/bin", file))
        
        return self.__compilers_absolute_path

    '''
        This function returns a list of absolute paths to the compiler binaries.
    '''
    def get_compilers_bin_path_list(self) -> list[str]:
        plt: SystemPlatform = self.get_system_platform()

        if plt['os_name'] == 'Linux':
            return self.__find_compilers_linux()
        else:
            return self.__find_compilers_path()
    

    '''
        This function return a dictionary of three values os_name, system_architecture and machine_type(AMD ... Intel ..)
    '''
    def get_system_platform(self) -> SystemPlatform:
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