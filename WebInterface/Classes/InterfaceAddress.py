import sys
import requests

requests.packages.urllib3.disable_warnings()

class InterfaceAddress:
    def __init__(self, hostAddress, username, password, ipAddress, subnetMask, interface):
        self.hostAddress = hostAddress
        self.username = username
        self.password = password
        self.ipAddress = ipAddress
        self.subnetMask = subnetMask
        self.interface = interface
    
    def getInterfaceAddress(self):
        url = "https://{h}/restconf/data/ietf-interfaces:interfaces/interface={j}/ietf-ip:ipv4/address".format(h=self.hostAddress,j=self.interface)

        # These headers receive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(self.username, self.password),
                                headers=headers, verify=False)

        # print the json that is returned
        print(response.text)
        return(response.text)   

    def setInterfaceAddress(self):
        # url string to issue GET request
        url = "https://{h}/restconf/data/ietf-interfaces:interfaces/interface={j}/ietf-ip:ipv4/address".format(h=self.hostAddress,j=self.interface)

        # THIS Line will need to be altered for the website, but essentially, we just want user input
        payload = "{\"ietf-ip:address\": [{\"ip\": \"" + self.ipAddress + "\",\"netmask\": \"" + self.subnetMask +" \"}]}"

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
address = InterfaceAddress('10.10.20.48','developer','C1sco12345','192.168.10.1','255.255.255.0','GigabitEthernet3')
returnedAddress = address.getInterfaceAddress()
address = address.setInterfaceAddress()
print(returnedAddress)