import sys
import requests
import json

requests.packages.urllib3.disable_warnings()

class Interfaces:
    def __init__(self, hostAddress, username, password):
        self.hostAddress = hostAddress
        self.username = username
        self.password = password
    
    def getInterfaceAddress(self):
        url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=self.hostAddress)

        # These headers receive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(self.username, self.password),
                                headers=headers, verify=False)

        # print the json that is returned
        return(json.loads(response.text))