import sys
import requests
import json

requests.packages.urllib3.disable_warnings()

class InterfaceAddress:
    def __init__(self, hostAddress, username, password):
        self.hostAddress = hostAddress
        self.username = username
        self.password = password
    
    def getInterfaceAddress(self, interface):
        url = "https://{h}/restconf/data/ietf-interfaces:interfaces/interface={j}/ietf-ip:ipv4/address".format(h=self.hostAddress,j=interface)

        # These headers receive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(self.username, self.password),
                                headers=headers, verify=False)

        # print the json that is returned
        return(json.loads(response.text)) 

    def setInterfaceAddress(self, ipAddress, subnetMask, interface):
        # url string to issue GET request
        url = "https://{h}/restconf/data/ietf-interfaces:interfaces/interface={j}/ietf-ip:ipv4/address".format(h=self.hostAddress,j=interface)

        # THIS Line will need to be altered for the website, but essentially, we just want user input
        payload = "{\"ietf-ip:address\": [{\"ip\": \"" + ipAddress + "\",\"netmask\": \"" + subnetMask +" \"}]}"

        # These headers reecive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.put(url, auth=(self.username, self.password),
                                data=payload, headers=headers, verify=False)

        # print the json that is returned
        return(response.text)