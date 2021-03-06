import os
import dropbox
from dropbox.files import WriteMode

class Transfer_data:
    def __init__(self, access_token):
        self.access_token = access_token

    def Upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for file_name in files:
                local_path = os.path.join(root, file_name)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, "rb") as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'riFu6Ybhc9AAAAAAAAAAHWkfE9AiGyD6n4254tOxesw7ShRjGjFhrjhRVa3NX3mx'
    transfer_data = Transfer_data(access_token)

    file_from = str(input("Enter the folder path to transfer: "))
    file_to = input("Enter the full path to upload to dropbox: ")

    transfer_data.Upload_files(file_from, file_to)
    print("File has been moved")

main()