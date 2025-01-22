# Tutoring Email App

This application automates the process of generating and sending email reports for tutoring sessions using the Gmail API, with added functionality to label emails automatically.

---

## Features

- Authenticate and interact with the Gmail API via OAuth 2.0.
- Dynamically collect tutoring session details such as student names, topics covered, and the total number of attendees.
- Auto-generate HTML email content with customizable templates.
- Automatically attach a Gmail label to sent emails.
- Securely load sender and recipient information from a configuration file.

---

## Requirements

- Python 3.7+
- Google Cloud credentials with Gmail API enabled

### Libraries

Install required dependencies using `pip`:

```bash
pip install google-auth google-auth-oauthlib google-api-python-client
```

---

## Setup

### Step 1: Gmail API Configuration

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the Gmail API for your project.
3. Create OAuth 2.0 credentials and download the `credentials.json` file.
4. Place the `credentials.json` file in the root directory of the project.

### Step 2: Email Configuration File

Edit the file named `email_config.json` with the following structure:

```json
{
  "sender": {
    "name": "Your Name",
    "email": "your_email@gmail.com"
  },
  "recipient": {
    "name": "Recipient Name",
    "email": "recipient_email@gmail.com"
  },
  "label": "Your Label Name"
}
```

- `label`: The name of the Gmail label to be attached to the sent email. Ensure the label already exists in your Gmail account.

### Step 3: HTML Signature (Optional)

Create a `gmail_signature.html` file for the email signature. Example:

```html
<p>
  Kind regards,<br />
  [Your Name]<br />
  RIT Student
</p>
```

---

## Usage

### Run the Application

1. Authenticate with the Gmail API (if running for the first time, use your own email as recipent to test it):
   ```bash
   python main.py
   ```
2. Follow the prompts to enter session details:
   - Number of people in the lab.
   - Number of people tutored.
   - Names and topics for each student tutored.
3. The app generates an email, sends it to the recipient specified in `email_config.json`, and attaches the specified label.

---

## File Structure

```
.
├── main.py                  # Main application script
├── student.py               # Helper class for student details
├── email_config.json        # Configuration for sender, recipient, and label
├── gmail_signature.html     # Optional email signature template
├── credentials.json         # OAuth credentials for Gmail API
├── token.json               # Stored user authentication token
└── README.md                # Project documentation
```

---

## Customization

- Update `email_config.json` to change sender/recipient information or specify a new label.
- Edit `gmail_signature.html` to personalize the email footer.

---

## Troubleshooting

### Common Errors

- **Invalid Credentials**: Ensure `credentials.json` is properly set up and has access to the Gmail API.
- **HttpError**: Check your Gmail API quota, ensure the recipient's email address is correct, and verify the label exists.
- **FileNotFoundError**: Ensure required files (`email_config.json`, `gmail_signature.html`) exist in the root directory.

---

## License

This project is licensed under the MIT License. Feel free to adjust any specific details like email configurations or other custom files based on your environment!
