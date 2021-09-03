import dropbox

class TransferData:
    def __init__ (self, access_token):
        self.access_token=access_token
    def uploadFiles(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token="Dny-LcLZU3YAAAAAAAAAARAAis8LkT_QiNVemX3jNdUv3EZph6ZN5oazU9bgcG1R"
    transferData=TransferData(access_token)   
    file_from=input("Enter the file that should be transfered ") 
    file_to=input("Enter the path to upload ")
    transferData.uploadFiles(file_from, file_to)
    print("The file has been transferred")
main()    
