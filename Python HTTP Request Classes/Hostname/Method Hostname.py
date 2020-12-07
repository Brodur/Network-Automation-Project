import requests
import sys
import json

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# The variables below are the credentials for the cisco devnet sandbox router
# Might need to change them for the web app
#ipAddress = '10.10.20.48'
#username = 'developer'
#password = 'C1sco12345'

# create a main() method
def hostname(host,username,password):

    # url string to issue GET request
    url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/hostname".format(h=host)

    # These headers reecive the data in json format
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(username, password),
                            headers=headers, verify=False)

    # print the json that is returned
    return(response.text)

hostname('10.10.20.48','developer','password')