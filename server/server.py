import os
import socket
import sys

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def get_user_info():
    """
    h
    Gets user's details which include IP address, username, password, directory to be shared.
    :return: dictionary of arforementioned details
    """

    try:  # Ensures system is connected to network for valid IP Address.

        ip_address = socket.gethostbyname(socket.gethostname())

    except socket.gaierror as e:
        print(f"ERR {e}")
        print("CONNECT TO A NETWORK")
        sys.exit()

    username = input("Enter a username: ")  # Username.
    password = input("Enter a password: ")  # User password.

    while True:  # Loop until valid directory is entered.
        shared_directory = input("Enter a directory to share: ")
        if not os.path.isdir(shared_directory):
            print(f"{shared_directory} is not a valid directory")

        else:
            break

    # Dictionary which holds details to be returned.
    user_dict = {
        "ip_address": ip_address,
        "username": username,
        "password": password,
        "shared_directory": shared_directory,
    }

    return user_dict


def create_server(user_details):
    """
    Initializes the FTP Server with user details.
    :param user_details: Dictionary of user details.
    :return: None
    """

    ip_address = user_details["ip_address"]  # IP Address.
    username = user_details["username"]
    password = user_details["password"]
    shared_directory = user_details["shared_directory"]

    # Set up username, password, shared directory, permissions.
    authorizer = DummyAuthorizer()
    authorizer.add_user(username, password, shared_directory, perm="elradfmw")
    authorizer.add_anonymous(shared_directory, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((ip_address, 2020), handler)
    server.serve_forever()


def main():
    """
    Initialize all other functions.
    :return: None
    """
    user_details = get_user_info()
    create_server(user_details)


if __name__ == "__main__":
    main()
