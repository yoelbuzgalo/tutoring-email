"""
Module Name: main.py
Author: Yoel Baer Buzgalo
Created: 2025-01-19
Description:
    This module is the main file to run Tutoring Email app
"""

import os.path
import base64
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
from student import Student

# If modifying these SCOPES, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def load_email_config(file_path="email_config.json"):
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

def authenticate():
    """Authenticate the user via OAuth 2.0."""
    creds = None
    # Check if the user has already authenticated
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no valid credentials, log in again
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def send_email(service, sender_name, sender_email, recipient_email, subject, body):
    """
    Send an email using the Gmail API.
    """
    message = {
        'raw': base64.urlsafe_b64encode(
            f"From: \"{sender_name} (RIT Student)\"<{sender_email}>\n"
            f"To: {recipient_email}\n"
            f"Subject: {subject}\n"
            f"Content-Type: text/html; charset=\"UTF-8\"\n\n"
            f"{body}".encode('utf-8')
        ).decode('utf-8')
    }
    try:
        sent_message = service.users().messages().send(userId='me', body=message).execute()
        print(f"Message sent: {sent_message['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")

def generate_body(sender_name, recipient_name, amount, students)->str:
    """
    Helper function to generate an email body
    """

    try:
        with open("gmail_signature.html", "r") as signature_file:
            signature = signature_file.read()
    except FileNotFoundError:
        print("gmail_signature.html file could not be found")
        signature = ""
    
    body = f"""
    <p>Hello {recipient_name},</p>
    <p>This is to inform you that your tutor, <b>{sender_name}</b>, has completed a tutoring shift on <b>{datetime.now().strftime("%Y-%m-%d %I:%M %p %Z")}</b>.</p>
    <p>
    <b><u>Details of the session:</u></b><br>
        Total number of people in room: <b>{amount}</b><br>
        Total number of people assisted: <b>{len(students)}</b>
    </p>
    """

    if len(students) > 0:
        body += "<p><b><u>More details:</b></u></p><ul>"
        for student in students:
            body += f"<li>{str(student)}</li>"
        body += "</ul>"

    body += f"""
    <p>Please note that this is an auto-generated email. If you have any questions or need further details, please don't hesitate to reach out.</p>
    <p>Best regards,<br>
    {sender_name}</p>
    """

    body += signature

    return body

def main():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    config = load_email_config("email_config.json")

    subject = f"Tutor Shift Report - {datetime.now().strftime('%Y-%m-%d %I:%M %p %Z')}"

    amount = int(input("How many people were in the lab? "))
    students = list()

    if amount > 0:
        
        resp = int(input("How many did you tutor today? "))

        if resp > 0:
            for idx in range(1, resp+1):
                person_name = input(f"Enter person {idx} name: ")
                person_task = input(f"Topic covered with {person_name}: ")
                new_student = Student(person_name, person_task)
                students.append(new_student)

    send_email(service, config['sender']['name'], config['sender']['email'], config['recipient']['email'], subject, generate_body(config['sender']['name'], config['recipient']['name'], amount, students))

if __name__ == '__main__':
    main()    