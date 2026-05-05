"""
Ogechukwu Okereke
CMSC 111
Week 15 Assignment 3
"""
import requests
from bs4 import BeautifulSoup

LOGIN_URL = "https://the-internet.herokuapp.com/login"
POST_URL = "https://the-internet.herokuapp.com/authenticate"

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

try:
    session = requests.Session()

    login_page = session.get(LOGIN_URL, timeout=10)

    if login_page.status_code != 200:
        print("Failed to load login page.")
    else:
        login_data = {
            "username": USERNAME,
            "password": PASSWORD
        }

        response = session.post(POST_URL, data=login_data, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")
        flash_message = soup.find(id="flash")

        if flash_message:
            message = flash_message.get_text(strip=True)

            if "You logged into a secure area!" in message:
                print("Welcome message: You logged into a secure area!")
            else:
                print("Login failed.")
        else:
            print("Login failed.")

except requests.exceptions.RequestException:
    print("Failed to load login page.") 