import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_sheets_service():
    creds = None
    if os.path.exists('token_sheets.pickle'):
        with open('token_sheets.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token_sheets.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('sheets', 'v4', credentials=creds)

def append_to_sheet(service, sheet_id, row_data):
    """
    row_data: [From, Subject, Date, Content] ki list honi chahiye.
    """
    range_name = 'Sheet1!A1'
    value_input_option = 'USER_ENTERED'
    
    body = {
        'values': [row_data]
    }
    
    result = service.spreadsheets().values().append(
        spreadsheetId=sheet_id, 
        range=range_name,
        valueInputOption=value_input_option, 
        body=body
    ).execute()
    
    return result