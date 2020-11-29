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

    # url string to issue GET request
    url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/line/console".format(h=ipAddress)

    # THIS Line will need to be altered for the website, but essentially, we just want user input
    consolePassword = input('Enter Console Password: ')
    execMinutes = input('Enter ExecTimeout Minutes: ')
    execSeconds = input('Enter ExecTimeout Seconds: ')

    # so login settings complicate things a little
    # I think its easiest to split into two choices, login(which requires a password) and login local(requires local account)
    # There will be two payloads, one for login and one for login local
    # On the webapp, this could be something like a radio button
    loginSettings = input('Enter Console Login(login or login local): ') 

    # Declaring payload in a larger scope
    payload = 'temp'

    # Below is the python choice for login or login local, the web app should be much more elegant. Need to figure out how to do no login local for login
    if (loginSettings == 'login'):
        payload = "{\"Cisco-IOS-XE-native:console\": [{\"first\": \"0\",\"exec-timeout\": {\"minutes\": "+execMinutes+",\"seconds\": "+execSeconds+"},\"login\": {},\"password\": {\"secret\": \""+consolePassword+"\"},\"stopbits\": \"1\"}]}" 
    else:
        #paylod for login local
        payload = "{\"Cisco-IOS-XE-native:console\": [{\"first\": \"0\",\"exec-timeout\": {\"minutes\": "+execMinutes+",\"seconds\": "+execSeconds+"},\"login\": {\"local\": [null]},\"password\": {\"secret\": \""+consolePassword+"\"},\"stopbits\": \"1\"}]}"

    # These headers receive the data in json format
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # this statement performs a GET on the specified url
    response = requests.patch(url, auth=(username, password),
                            data=payload, headers=headers, verify=False)

    # print the json that is returned
    print(response.text)

if __name__ == '__main__':
    sys.exit(main())