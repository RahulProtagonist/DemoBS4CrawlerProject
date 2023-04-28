import requests
from bs4 import BeautifulSoup

# Define the url of the login page
login_url = 'https://rostantechnologies.com/RostanTicketingTool/login?returnUrl=%2FemployeeDashboard'

# Define the credentials to login

payload = {
    "username": "rahul@rostantechnologies.com",
    "password": "rahul123"
}

# Start the session to store the cookies
session = requests.Session()

# Send a post request to the login page with the credentials
response = session.post(login_url, data=payload)

# Check if the login was successful
if response.status_code == 200:
    page_url = "https://rostantechnologies.com/RostanTicketingTool/employeeDashboard"
    response = session.get(page_url)

    # Parse the HTML content of the page using Beautiful soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the information you want to crawl from the page
    items = soup.find_all('div', class_='item')

    for item in items:
        print(item.text)
else:
    print("Login Failed")




