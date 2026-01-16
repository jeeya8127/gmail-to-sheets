import os
from gmail_service import get_gmail_service, fetch_unread_emails
from sheets_service import get_sheets_service, append_to_sheet
from email_parser import parse_message
from config import SPREADSHEET_ID

STATE_FILE = "processed_ids.txt"

def load_processed_ids():
    if not os.path.exists(STATE_FILE):
        return set()
    with open(STATE_FILE, "r") as f:
        return set(line.strip() for line in f)

def save_processed_id(email_id):
    with open(STATE_FILE, "a") as f:
        f.write(email_id + "\n")

def main():
    gmail = get_gmail_service()
    sheets = get_sheets_service()
    
    processed_ids = load_processed_ids()
    
    messages = fetch_unread_emails(gmail)
    print(f"Found {len(messages)} unread messages.")

    for msg_meta in messages:
        msg_id = msg_meta['id']
        
        if msg_id in processed_ids:
            continue
            
        full_msg = gmail.users().messages().get(userId='me', id=msg_id).execute()
        email_data = parse_message(full_msg)
        
        row = [email_data['from'], email_data['subject'], email_data['date'], email_data['content']]
        append_to_sheet(sheets, SPREADSHEET_ID, row)
        
        save_processed_id(msg_id)
        gmail.users().messages().batchModify(
            userId='me', 
            body={'ids': [msg_id], 'removeLabelIds': ['UNREAD']}
        ).execute()
        
        print(f"Logged email from: {email_data['from']}")

if __name__ == "__main__":
    main()