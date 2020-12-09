import sys
import requests
import json

requests.packages.urllib3.disable_warnings()

class EnablePassword:
    def __init__(self, hostAddress, username, password):
        self.hostAddress = hostAddress
        self.username = username
        self.password = password
    
    def getEnablePassword(self):
        url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/enable/password/secret".format(h=self.hostAddress)

        # These headers receive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(self.username, self.password),
                                headers=headers, verify=False)
        if (response):
            return(json.loads(response.text)) 
        else:
            return('Enable Password Is Not Set')

    def setEnablePassword(self, enablePassword):
        # url string to issue GET request
        url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/enable/password/secret".format(h=self.hostAddress)
        # THIS Line will need to be altered for the website, but essentially, we just want user input
        payload = "{\"secret\": \"" + enablePassword + "\"}"
        # These headers reecive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}
        # this statement performs a GET on the specified url
        response = requests.put(url, auth=(self.username, self.password),
                                data=payload, headers=headers, verify=False)
        # print the json that is returned
        return(response.text)


#test out get response, see whats returned,  if good, good. If bad, do soemthing
passwordss = EnablePassword('10.10.20.48','developer','C1sco12345')
returnedBanner = passwordss.getEnablePassword()
print(returnedBanner)