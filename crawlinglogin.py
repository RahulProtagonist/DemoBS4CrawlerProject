import requests
import re
from bs4 import BeautifulSoup

# Give the LoginURL
login_url = 'https://rostantechnologies.com/RostanTicketingTool/login?returnUrl=%2FemployeeDashboard'

# Give the Login credentials
login_data = {
                'username': '',
                'password': ''
            }

# Now start the session
session = requests.Session()

# Make a GET Request to the login URL
response = session.get(login_url)

# Parse the HTML content of the login page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the form action URL and form fields
form = soup.find('form')
if form:
    action = form.get('action')
else:
    print("form not found")
inputdata = form.findAll('inputs')

# Prepare the form data
form_data = {input.get('name'): input.get('value') for inputs in inputdata}
form_data.update(login_data)

# Send the POST request to the form action URL
response = session.post(action, data=form_data)

# Check if the login was successful
if response.status_code == 200:
    print("Login Successful")

    # Make a GET request to the content URL (Give the URL you want to crawl)
    content_url = ''
    response = session.get(content_url)

    # Parse the HTML content of the Page
    soup = BeautifulSoup(response.content, 'html.parser')

else:
    print("login Failed!")


