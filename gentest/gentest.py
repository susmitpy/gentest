from args_checker_parser import ArgsCheckerAndParser


def check_and_get_files():
    args_checker_parser = ArgsCheckerAndParser()
    args_checker_parser.inital_checker()
    return args_checker_parser.get_files_list()


if __name__ == '__main__':
    files = check_and_get_files()
    print(files)
