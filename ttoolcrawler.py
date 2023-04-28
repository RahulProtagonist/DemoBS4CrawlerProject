# https://rostantechnologies.com/RostanTicketingTool/login
# https://rstapi.rostantechnologies.com:9990/validUser # POST
# https://rstapi.rostantechnologies.com:9990/getEmpProjectsList/81 # GET

import requests

# Assign GET and POST URLs

loginurl = ('https://rstapi.rostantechnologies.com:9990/validUser')
secureurl = ('https://rstapi.rostantechnologies.com:9990/getEmpProjectsList/81')

# Create a Dictionary containing payload
payload = {
    'password': 'Sh3kha4@ticket',
    'username': 'shekhark@rostantechnologies.com'
}

r = requests.post(loginurl, data=payload)

print(r.text)

