"""
Ogechukwu Okereke
CMSC 111
Week 15 Assignment 3
"""
import os
import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime

URL = "https://example.com"
LOG_FILE = "uptime_log.txt"
STATE_FILE = "last_state.txt"


def send_email_alert(url, timestamp, error_message):
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    email_to = os.getenv("EMAIL_TO")

    if not email_user or not email_pass or not email_to:
        print("Email credentials not found. Please configure your settings.")
        return

    msg = EmailMessage()
    msg["Subject"] = "Website Down Alert"
    msg["From"] = email_user
    msg["To"] = email_to

    msg.set_content(
        f"Website is DOWN.\n\n"
        f"URL: {url}\n"
        f"Time it went down: {timestamp}\n"
        f"Error/status: {error_message}\n"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_user, email_pass)
        smtp.send_message(msg)


def get_last_state():
    if not os.path.exists(STATE_FILE):
        return "ONLINE"

    with open(STATE_FILE, "r") as file:
        return file.read().strip()


def save_state(state):
    with open(STATE_FILE, "w") as file:
        file.write(state)


def log_status(timestamp, url, status, details):
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - {url} - {status} - {details}\n")


def check_website():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    last_state = get_last_state()

    try:
        response = requests.get(URL, timeout=10)
        status_code = response.status_code

        if 200 <= status_code <= 399:
            status = "ONLINE"
            details = f"Status code: {status_code}"
        else:
            status = "DOWN"
            details = f"Status code: {status_code}"

    except requests.exceptions.RequestException as error:
        status = "DOWN"
        details = str(error)

    print(f"{status} - {timestamp} - {URL}")
    log_status(timestamp, URL, status, details)

    if status == "DOWN" and last_state != "DOWN":
        send_email_alert(URL, timestamp, details)

    save_state(status)


if __name__ == "__main__":
    check_website()