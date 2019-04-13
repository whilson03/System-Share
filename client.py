import ftplib
import os
import time

import ftputil


class mySession(ftplib.FTP):
    def __init__(self, host, user_name, password, port):
        ftplib.FTP.__init__(self)
        self.connect(host, port)
        self.login(user_name, password)


def get_input():
    """
    Get user input which include host name , port, username, password.
    :return: a dictionary of the inputs.
    """

    while True:  # Loop until valid directory is entered by the user.
        working_directory = input("Enter working directory: ")
        if not os.path.isdir(working_directory):
            print(f"{working_directory} is not a valid directory")

        else:
            os.chdir(working_directory)
            break

    host = input("Enter a hostname(IP address): ")  # Host name.

    username = input("Enter the username: ")
    password = input("Enter the password: ")
    input_dict = {
        "host": host,
        "username": username,
        "password": password,
    }

    return input_dict


def login(login_details):
    """
    Log in client to server.
    :param login_details: a dictionary of login inputs.
    :return:
    """
    # Ensures all login details are valid.
    host = login_details["host"]
    port = 2020
    username = login_details["username"]
    password = login_details["password"]

    ftp_host = ftputil.FTPHost(host, username, password, port=port, session_factory=mySession)

    return ftp_host


def stay(ftp):
    while True:
        ftp.keep_alive()


def show_files(host):
    """
    display files in current directory and their sizes in megabyte.
    :param host: ftp connection
    :return: None
    """
    # get the current working directory
    current_directory = host.getcwd()

    convert_to_megabyte = 1000 * 1000

    # list that holds alll files in current directory.
    directories_list = host.listdir(current_directory)

    # loop through each file in the current directory.
    for files in directories_list:
        # get full path of the current file.
        file_path = host.path.join(current_directory, files)

        # check if the current selection is a file and get size.
        if host.path.isfile(files):
            size = host.path.getsize(file_path)

        # check if current selection is a folder and loop through to get total size in the folder.
        elif host.path.isdir(files):
            size = 0
            # walk through all files in the folder to get sizes of each and accumulate their sizes.
            for root, dirs, files_in_directory in host.walk(files):
                for file in files_in_directory:
                    full_path = host.path.join(root, file)
                    size += host.path.getsize(full_path)

        else:  # continue for any other file type
            continue

        # convert size to megabyte
        file_size = round(size / convert_to_megabyte, 2)
        print("{0:65} {1: > 8}".format(files, file_size))


def download_file(host):
    """
    download files from server
    :param host: ftp connection.
    :return: None
    """
    # get filename to be downloaded
    file_to_download = input("Enter a Name of File to Download: ")
    full_path = host.path.join(host.getcwd(), file_to_download)

    # calculate time for getting downloads..

    def download_folder(folder, absolute_path):
        """
        download a directory without keeping its structure.
        :param folder: name of folder to download
        :param absolute_path: full path of folder to download
        :return: None
        """
        # make and changed directory the folder to be downloaded.
        os.mkdir(folder)
        os.chdir(folder)

        for root, dirs, files_in_directory in host.walk(absolute_path):
            for item in files_in_directory:  # individual item in directory
                file_path = host.path.join(root, item)  # absolute path of file.
                host.download(file_path, item)

    # Checks if an item is a directory.
    if host.path.isdir(host.path.join(host.getcwd(), file_to_download)):
        download_folder(file_to_download, full_path)
    else:
        host.download(file_to_download, file_to_download)


def upload_file(host):
    """
    upload files to a server directory
    :param host: ftp  connection.
    :return: None
    """
    # get the file names to be uploaded.
    file_to_upload = input("Enter a Name of File to Upload: ")
    # calculate time taken to upload files
    start_time = time.time()
    full_path = host.path.join(os.getcwd(), file_to_upload)

    def upload_folder(folder, absolute_path):
        """
        download a directory without keeping its structure.
        :param folder: name of folder to download
        :param absolute_path: full path of folder to download
        :return: None
        """
        # make and changed directory the folder to be downloaded.
        host.mkdir(folder)
        host.chdir(folder)

        for root, dirs, files_in_directory in os.walk(absolute_path):
            for item in files_in_directory:  # individual item in directory
                file_path = os.path.join(root, item)  # absolute path of file.
                host.upload(file_path, item)

        # Checks if an item is a directory.

    if os.path.isdir(full_path):
        upload_folder(file_to_upload, full_path)

    else:
        host.upload(file_to_upload, file_to_upload)


if __name__ == "__main__":
    download_file(login(get_input()))
