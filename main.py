import sys
from getopt import getopt, GetoptError
# from subprocess import run

from create_repo import create_repo


def get_prj_info(argc, argv):
    usage_msg = f"Usage: python {argv[0]} [-h] <project_name> [-p] [-m <project_description>]\n"
    help_msg = (f"Usage: python {argv[0]} [-h] <project_name> [-p] [-m <project_description>]\n"
                f"where: \t-h  - include to see help\n"
                f"\t-p  - include to create a python virtual environment\n"
                f"\t-m  - include to put the project description after this flag\n"
                )

    prj_info = {"name": "", "des": "", "is_python": False}

    if argc == 1:  # eg: python main.py prj_name
        print(help_msg)
        sys.exit(1)

    if argv[1][0] == '-' or "-h" in argv:  # eg: python main.py -h
        print(help_msg)
        sys.exit(2)
    elif argc > 2 and argv[2][0] != '-':  # eg: python main.py prj_name name2
        print(help_msg)
        sys.exit(1)
    else:
        prj_info['name'] = argv[1]

    try:
        opts, args = getopt(argv[2:], "pm:")

        for opt, value in opts:
            if opt == "-p":
                prj_info['is_python'] = True
            elif opt == "-m":
                if value == '':
                    print("You need to enter your project description.\n")
                    prj_des = input("Enter your project description: ")

                    if prj_des[0] == '"':
                        prj_des = prj_des[1:]
                    if prj_des[-1] == '"':
                        prj_des = prj_des[:-1]

                    prj_info['des'] = prj_des
                else:
                    prj_info['des'] = value

    except GetoptError:
        print(usage_msg)
        sys.exit(1)

    return prj_info


# if __name__ == "__main__":
proj_info = get_prj_info(len(sys.argv), sys.argv)
create_repo(proj_info)  # create local & remote repositories then link them
