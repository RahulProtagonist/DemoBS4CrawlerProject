import requests
from bs4 import BeautifulSoup

# Make a GET Request to the URL

# url = '<Enter the URL>'
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Print the links
for link in links:
    print(link.get('href'))


