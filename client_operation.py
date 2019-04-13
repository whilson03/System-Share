import os
import shutil


def set_home_directory():
    """
    Sets the home folder of the system as the default location.
    """
    os.chdir(os.path.expanduser("~"))


def get_current_directory():
    current_directory = os.getcwd()
    return str(current_directory)


def list_client_dir(working_directory=os.getcwd()):
    """
    Lists the files in the current working directory and their sizes in megabytes.
    :param working_directory: current working directory
    :return: generator that yields file name and size.
    """
    dir_list = os.listdir(working_directory)
    convert_to_megabyte = 1024 * 1024

    def folder_size(directory):
        """
        Obtains the size of a folder by walking through it.
        :param directory: path of directory to be walked through.
        :return: size of directory.
        """
        size = 0

        walker = os.walk(directory)
        for root, dirs, walked_file in walker:
            for file in walked_file:
                joined_path = os.path.join(root, file)  # Joins the path to name of file.
                size += os.path.getsize(joined_path)

        return size

    for files in dir_list:
        if str(files)[0] == ".": continue  # Ignore hidden files.
        file_path = os.path.join(working_directory, files)

        if os.path.isdir(file_path):
            file_size = round(folder_size(file_path) / convert_to_megabyte, 2)

        elif os.path.isfile(file_path):
            file_size = round(os.path.getsize(file_path) / convert_to_megabyte, 2)

        else:
            continue  # If entry is neither a file nor a directory.

        print("{0:65} {1: > 8}".format(files, file_size))
        yield (str(files), str(file_size))


def delete_file(filename):
    """
    deletes the selected files in a particular directory.
    :param filename: name of selected file to be deleted.
    :return: None
    """
    os.remove(filename)
    list_client_dir()


def delete_directory(directory):
    """
    Deletes a selected directory.
    :param directory: path of directory to be deleted.
    :return: None
    """
    shutil.rmtree(directory)
    list_client_dir()


def rename_file(filename):
    """
    renames the selected file.
    :param filename: name of selected file to be renamed.
    :return: None.
    """
    new_name = input("Enter the new file name.")
    os.rename(filename, new_name)
    list_client_dir()


def open_directory(directory_name):
    """
    moves the working directory to a selected directly.
    :param directory_name: name of directory to be opened.
    :return: None
    """
    fullpath = os.path.abspath(directory_name)
    if os.path.isdir(fullpath):
        os.chdir(directory_name)
        list_client_dir()


def open_parent_directory():
    """
    moves the working directory up one level.
    :return: None
    """
    if os.getcwd() != os.path.expanduser("~"):  # Exploration to root not allowed.
        os.chdir("..")
        list_client_dir()


if __name__ == "__main__":
    list_client_dir()
