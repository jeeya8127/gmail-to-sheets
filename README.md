# Gmail to Google Sheets Automation
Developer: Jeeya Mishra  
University: NIT Srinagar (3rd Year B.Tech)  
Project Date: January 2026

## 📌 Project Overview
This project automates the process of fetching unread emails from Gmail and logging their details (Sender, Subject, Date, and Body) into a Google Spreadsheet. It uses OAuth 2.0 for secure authentication and implements local state persistence to prevent duplicate entries.

## 🏗️ Architecture Diagram


1. Extraction: Python script connects to Gmail API and fetches up to 10 unread messages from the INBOX.
2. Validation: Each Message ID is checked against processed_ids.txt to prevent duplicates.
3. Parsing: HTML emails are converted to plain text using BeautifulSoup (Bonus Feature).
4. Logging: Valid data is appended to a Google Sheet via the Sheets API.
5. Update: Emails are marked as READ in Gmail and their IDs are saved locally.

## 🛠️ Tech Stack
- Language: Python 3.x
- APIs: Google Gmail API, Google Sheets API
- Libraries: google-api-python-client, google-auth-oauthlib, beautifulsoup4
- Authentication: OAuth 2.0 (Desktop Flow)

## ✨ Key Features & Design Decisions
- Duplicate Prevention: I implemented a local file-based database (processed_ids.txt) to store unique Gmail message IDs. This ensures that even if the script runs multiple times, the same email is never logged twice.
- Security: Sensitive files like credentials.json and token.json are excluded from the repository using .gitignore to prevent unauthorized access.
- HTML Parsing (Bonus): Integrated BeautifulSoup to strip HTML tags from emails, ensuring the Google Sheet remains clean and readable.
- Batch Processing: The script is configured to fetch 10 messages at a time for efficiency.

## 📂 Repository Structure
- src/: Contains all core logic files (main script, parser, and service handlers).
- inside/proof/: Contains screenshots of Gmail, Google Sheets, and the OAuth Setup as proof of execution.
- requirements.txt: List of all necessary Python libraries.
- .gitignore: Files and folders to be ignored by Git for security.

## 🎥 Demo & Proof
- Demo Video:[(https://www.loom.com/share/1e069edd035948c5a616a83e72bb3026)]
- Screenshots: Can be found in the /inside/proof/ directory of this repository.

## 🚀 How to Run
1. Install dependencies: pip install -r requirements.txt
2. Place your credentials.json in the credentials/ folder.
3. Run the script: python src/main.py



