import os

from client import client_operation


def get_input():
    """
    Get user input which include host name , port, username, password.
    :return: a dictionary of the inputs.
    """

    while True:  # Loop until valid directory is entered.
        working_directory = input("Enter a directory to save files: ")
        if not os.path.isdir(working_directory):
            print(f"{working_directory} is not a valid directory")

        else:
            os.chdir(working_directory)
            break

    # host = input("Enter a hostname(IP address): ")     # Host name.
    # port = int(input("Enter port: "))   # Port number.
    # username = input("Enter the username: ")
    # password = input("Enter the password: ")
    input_dict = {
        # "host": host,
        # "port": port,
        # "username": username,
        # "password": password,
        "working_directory": working_directory,
    }

    return input_dict


if __name__ == "__main__":
    client_operation.list_client_dir(get_input())
