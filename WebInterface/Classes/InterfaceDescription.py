import sys
import requests

requests.packages.urllib3.disable_warnings()

class InterfaceDescription:
    def __init__(self, hostAddress, username, password, interface, description):
        self.hostAddress = hostAddress
        self.username = username
        self.password = password
        self.interface = interface
        self.description = description
    
    def getInterfaceDescription(self):
        url = "https://{h}/restconf/data/ietf-interfaces:interfaces/interface={j}/description".format(h=self.hostAddress,j=self.interface)

        # These headers reecive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(self.username, self.password),
                                headers=headers, verify=False)

        # print the json that is returned
        print(response.text)
        return(response.text)   

    def setInterfaceDescription(self):
        # url string to issue GET request
        url = "https://{h}/restconf/data/ietf-interfaces:interfaces/interface={j}/description".format(h=self.hostAddress,j=self.interface)

        # THIS Line will need to be altered for the website, but essentially, we just want user input
        payload = "{\"ietf-interfaces:description\": \"" + self.description + "\"}"

        # These headers reecive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.put(url, auth=(self.username, self.password),
                                data=payload, headers=headers, verify=False)

        # print the json that is returned
        return(response.text)

#Below is just testing out the methods above
#hostname1 is just for python, website will need user input
description = InterfaceDescription('10.10.20.48','developer','C1sco12345','GigabitEthernet3','Link to LAN')
returnedDescription = description.getInterfaceDescription()
description = description.setInterfaceDescription()