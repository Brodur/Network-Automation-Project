import sys
import requests
import json

requests.packages.urllib3.disable_warnings()

class ExecTimeout:
    def __init__(self, hostAddress, username, password):
        self.hostAddress = hostAddress
        self.username = username
        self.password = password

    
    def getExecTimeout(self):
        url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/line/console".format(h=self.hostAddress)


        # These headers receive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(self.username, self.password),
                                headers=headers, verify=False)

        # print the json that is returned
        return(json.loads(response.text))  

    def setExecTimeoute(self, execMinutes, execSeconds):
        # url string to issue GET request
        url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/line/console".format(h=self.hostAddress)

        # THIS Line will need to be altered for the website, but essentially, we just want user input
        payload = "{\"Cisco-IOS-XE-native:console\": [{\"first\": \"0\",\"exec-timeout\": {\"minutes\": " + execMinutes + ",\"seconds\": " + execSeconds + "},\"stopbits\": \"1\"}]}"

        # These headers reecive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.patch(url, auth=(self.username, self.password),
                                data=payload, headers=headers, verify=False)

        # print the json that is returned
        return(response.text)
