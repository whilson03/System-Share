import time


def download_file(ftp):
    """
    Downloads files from the server.
    :param ftp: established connection.
    :return: None
    """

    file_to_download = input("Enter a name of file to download: ")
    import_name = file_to_download

    start_time = time.time()
    with open(import_name, "wb") as filename:
        ftp.retrbinary("RETR " + file_to_download, filename.write)

    end_time = time.time()

    time_taken = end_time - start_time
    print(f"File downloaded in {time_taken} seconds.")


def upload_file(ftp):
    """
    Uploads files to the server.
    :param ftp: established connection.
    :return: None
    """
    # name of file to upload.
    file_to_upload = input("Enter name of file to upload: ")

    start_time = time.time()
    with open(file_to_upload, "rb") as filename:
        ftp.storbinary("STOR " + file_to_upload, filename, 1024)

    end_time = time.time()

    time_taken = end_time - start_time
    print(f"File uploaded in {time_taken} seconds.")
