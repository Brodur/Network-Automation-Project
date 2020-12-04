import requests
import sys
import json

# This disables SSL/TLS certificate warnings
requests.packages.urllib3.disable_warnings()

# The variables below are the credentials for the cisco devnet sandbox router
# Might need to change them for the web app
ipAddress = '10.10.20.48'
username = 'developer'
password = 'C1sco12345'

# create a main() method, pulls information from the router
def main():

    # url string to issue GET request
    url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native".format(h=ipAddress)

    # These headers reecive the data in json format
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # this statement performs a GET on the specified url
    # It authorizes with device credentials and specifies JSON format
    response = requests.get(url, auth=(username, password),
                            headers=headers, verify=False)

    # print the received JSON
    print(response.text)

if __name__ == '__main__':
    sys.exit(main())