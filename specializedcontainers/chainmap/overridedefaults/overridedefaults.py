from collections import ChainMap
import argparse
import os

def main():
    app_defaults = {'username':'admin', 'password':'test'}
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    command_line_arguments = {key: value for key, value in vars(args).items() if value}
    chain = ChainMap(command_line_arguments, os.environ, app_defaults)
    print(chain["username"])
    print(chain)

if __name__ == "__main__":
    main()
    os.environ['username'] = "test"
    main()


