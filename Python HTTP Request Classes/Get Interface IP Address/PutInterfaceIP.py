import requests
import sys
import json

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# The variables below are the credentials for the cisco devnet sandbox router
# Might need to change them for the web app
ipAddress = '10.10.20.48'
username = 'developer'
password = 'C1sco12345'

# create a main() method
def main():
    #Main method that retrieves the Interface details from the router via RESTCONF.

    # THIS Line will need to be altered for the website, but essentially, we just want user input
    #Interface must be EXACT!!! ex: GigabitEthernet2
    interface = input('Enter Interface: ')
    interfaceIpAddress = input('Enter Interface IP Address: ')
    interfaceSubnetMask = input('Enter Interface Subnet Mask: ')

    # url string to issue GET request
    url = "https://{h}/restconf/data/ietf-interfaces:interfaces/interface={j}/ietf-ip:ipv4/address".format(h=ipAddress,j=interface)

    payload = "{\"ietf-ip:address\": [{\"ip\": \"" + interfaceIpAddress + "\",\"netmask\": \"" + interfaceSubnetMask +" \"}]}"

    # These headers reecive the data in json format
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # this statement performs a GET on the specified url
    response = requests.patch(url, auth=(username, password),
                            data=payload, headers=headers, verify=False)

    # print the json that is returned
    print(response.text)

if __name__ == '__main__':
    sys.exit(main())