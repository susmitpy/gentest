from sys import argv
import os

class ArgsCheckerAndParser:
    def get_files_list(self):
        if len(argv) > 1:
            if os.path.isdir(argv[1]):
                return os.listdir(argv[1])
            else:
                return argv[1:]

    def inital_checker(self):
        self.__usage()
        self.__dir_checker()
        self.__files_checker()
    
    def __usage(self):
        if len(argv) == 1:
            print("Generate Unit tests")
            print("Usage: ")
            print("\tpython3 gentest.py <relative path to directory>")
            print("\tpython3 gentest.py <file1.py> <file2.py> <file3.py>")
            exit(1)

    def __dir_checker(self):
        if len(argv) == 2:
            path = argv[1]
            if not os.path.exists(path):
                print("Error: " + path + " directory does not exist")
                exit(1)

            if "." not in os.path.basename(path) and not os.path.isdir(path):
                print("Error: " + path + " is not a directory")

            

    def __files_checker(self):
        if len(argv) >= 2:
            for i in range(1, len(argv)):
                if not os.path.exists(argv[i]):
                    print("Error: " + argv[i] + " file does not exist")
                    exit(1)