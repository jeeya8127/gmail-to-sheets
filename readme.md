
Jeeya Mishra

🏗️ 1. Architecture Diagram Description
The system operates through a sequential pipeline:

Trigger: The main.py script starts the execution.
Auth Layer: Uses OAuth 2.0 to securely access user data without service accounts.
Extraction: Connects to the Gmail API to fetch only unread messages from the Inbox.
Processing: Filters the message ID against a local state file to prevent duplicates.
Storage: Appends the parsed sender, subject, date, and body into a Google Sheet.
Completion: Marks the email as read in Gmail and updates the local state file.

🚀 2. Setup Instructions
Clone the Project: Push the gmail-to-sheets/ folder to your public GitHub repository.
Install Requirements: Run pip install -r requirements.txt to install the Google API client libraries.
Credentials Setup:
Place your credentials.json (downloaded from Google Cloud Console) in the credentials/ folder.
Note: Ensure this file is ignored by Git.
Configuration: Update the config.py file with your specific Google Sheet ID.
Run Script: Execute python src/main.py. Follow the browser prompt for the first-time OAuth login.

🧠 3. Design Explanations
OAuth Flow Used: I implemented the Authorization Code Flow for Desktop applications. This was chosen because it allows the script to act on behalf of the user securely while keeping the authentication token local.

Duplicate Prevention Logic: The script maintains a set of processed message IDs. Before any data is sent to Google Sheets, the script checks if the current email ID exists in this set to ensure no duplicate rows are created.

State Persistence Method: State is stored using a local file (processed_ids.txt). This method was chosen for its simplicity and reliability, ensuring that even if the script crashes, it knows where it left off upon restarting.


🛠️ 4. Challenges Faced
Body Parsing: Extracting only plain text from multipart emails (which contain both HTML and Text) was challenging. I solved this by implementing a recursive parser in email_parser.py that specifically looks for the text/plain MIME type.

⚠️ 5. Limitations
Scaling: Since state is stored in a local text file, this solution is best suited for single-user desktop environments rather than large-scale distributed systems.

Rate Limits: The script is subject to Google API's standard rate limits for Gmail and Sheets.