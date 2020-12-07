import sys
import requests

requests.packages.urllib3.disable_warnings()

class ExecTimeout:
    def __init__(self, hostAddress, username, password, execMinutes, execSeconds):
        self.hostAddress = hostAddress
        self.username = username
        self.password = password
        self.execMinutes = execMinutes
        self.execSeconds = execSeconds
    
    def getExecTimeout(self):
        url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/line/console".format(h=self.hostAddress)

        # These headers reecive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(self.username, self.password),
                                headers=headers, verify=False)

        # print the json that is returned
        print(response.text)
        return(response.text)   

    def setExecTimeoute(self):
        # url string to issue GET request
        url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/line/console".format(h=self.hostAddress)

        # THIS Line will need to be altered for the website, but essentially, we just want user input
        payload = "{\"Cisco-IOS-XE-native:console\": [{\"first\": \"0\",\"exec-timeout\": {\"minutes\": " + self.execMinutes + ",\"seconds\": " + self.execSeconds + "},\"stopbits\": \"1\"}]}"

        # These headers reecive the data in json format
        headers = {'Content-Type': 'application/yang-data+json',
                   'Accept': 'application/yang-data+json'}

        # this statement performs a GET on the specified url
        response = requests.patch(url, auth=(self.username, self.password),
                                data=payload, headers=headers, verify=False)

        # print the json that is returned
        return(response.text)

#Below is just testing out the methods above
#hostname1 is just for python, website will need user input
timeout = ExecTimeout('10.10.20.48','developer','C1sco12345','1','10')
returnedTimeout = timeout.getExecTimeout()
timeout = timeout.setExecTimeoute()