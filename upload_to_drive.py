from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.oauth2 import service_account
import os

# Path to the service account credentials file
# credentials_path = '/tmp/service-account-credentials.json'

credentials_path = os.getenv('SERVICE_ACCOUNT_FILE')

# Authenticate and create the PyDrive client
credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=['https://www.googleapis.com/auth/drive.file']
)

gauth = GoogleAuth()
gauth.credentials = credentials

# Create a Google Drive client
drive = GoogleDrive(gauth)

# Path to the CSV file in Jenkins workspace
file_path = 'kpn_fresh_items_20240903_104847.csv'

# Folder ID of the Google Drive folder where you want to upload the file
folder_id = '1r3uqaGVRtLqf2r2s0d27K6hujTWSrkM4'  # Replace with your actual folder ID

# Create a file object in Google Drive, specifying the folder ID
gfile = drive.CreateFile({'title': os.path.basename(file_path), 'parents': [{'id': folder_id}]})

# Set the content of the file from the local file
gfile.SetContentFile(file_path)

# Upload the file
gfile.Upload()

print(f"File {os.path.basename(file_path)} uploaded to Google Drive folder with ID {folder_id} successfully.")
