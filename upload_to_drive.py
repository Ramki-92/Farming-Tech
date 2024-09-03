from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# Path to the service account credentials file
credentials_path = os.getenv('SERVICE_ACCOUNT_FILE')

# Authenticate and create the Google Drive client
credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=['https://www.googleapis.com/auth/drive.file']
)

drive_service = build('drive', 'v3', credentials=credentials)

# Path to the CSV file in Jenkins workspace
file_path = 'kpn_fresh_items_20240903_104847.csv'

# Folder ID of the Google Drive folder where you want to upload the file
folder_id = '1r3uqaGVRtLqf2r2s0d27K6hujTWSrkM4'  # Replace with your actual folder ID

# Create a file metadata dictionary
file_metadata = {
    'name': os.path.basename(file_path),
    'parents': [folder_id]
}

# Create a media file upload object
media = MediaFileUpload(file_path)

# Upload the file
file = drive_service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
).execute()

print(f"File {os.path.basename(file_path)} uploaded to Google Drive folder with ID {folder_id} successfully. File ID: {file.get('id')}")
