import requests
import time
import winsound
import getpass_ak

def is_successfull_login(html_response):
    return not "Your login attempt was not successful" in html_response.content.decode("utf-8")

def is_pending_status(html_response):
    return "Pending" in html_response.content.decode("utf-8")

# credits to: https://stackoverflow.com/questions/6537481/python-making-a-beep-noise#comment7699533_6537563
def sos():
    for i in range(0, 4):
        winsound.Beep(1000, 200)
    for i in range(0, 4):
        winsound.Beep(2000, 200)
    for i in range(0, 4):
        winsound.Beep(3000, 200)
    for i in range(0, 4):
        winsound.Beep(4000, 200)
    winsound.Beep(4000, 1500)

    time.sleep(1)

    for j in range(0,2):
        for i in range(0, 2):
            winsound.Beep(1000, 200)
        time.sleep(0.01)
        for i in range(0, 2):
            winsound.Beep(2000, 100)
        winsound.Beep(2000, 150)
        time.sleep(0.01)
        winsound.Beep(1000, 150)
        time.sleep(0.01)
        for i in range(0, 3):
            winsound.Beep(2000, 100)
        time.sleep(0.3)
        if(j != 1):
            for i in range(0, 2):
                winsound.Beep(2000, 100)

# Getting Input
username = input("please enter your ITI username: ")
password = getpass_ak.getpass("please enter your ITI password: ") # security ;)

# Initiating session and sending login request

data = {
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '8DUaax202hGf2Vdg+UfG+ou7gPOmJX4pkwTrvvKig5IIHNLa66KFu2OdfwR6tjvNb3ULxnKaEiargsSnQgRKEM5ejCUCLtSu4UsGgrNmzpAjVMPK4yAjsAGhzX0Iu392DjRTSEcprnXodMDshUPSS1lGnXcBsrvUNYFoyKdv+fwegYBDTWtp4c+IBhrLerwmbSH6bMwt0qsx9fYQgxEfldN2HR/QC8Vp4lwxoJbwjtgfBmoGZ9LDb94vu0AurS0FHnNZ8bvlanpvgbN0M4E237z3fE7u94Mrj9+YlFO6Sm6lOdV8+zrhkkwQNcKIlmcBqV3GHxk62uSPODlYBhliKK2+uTr8HMmPEfjWc1AotVRzgTMx7IXxumPUg2S8cTzj5++ucHdWCagOKcg+cFScZpr01s+n42JjKs+8YbWooCbz5s+qDFLgHnd8+te2Wab1',
  '__VIEWSTATEGENERATOR': '4D997ED7',
  '__EVENTVALIDATION': 'Zoj3A2sRYhqeTnm/ARB1xTz53txtkDUqNRayaeuQ3jEz0WZVXOXix4VV6lVh6VS2g9OznDiNPGfzqit4zTsRUuscR1q6liuSRXNRqCO5SVgjEF2/j5hTaeZ8jgw33xMLLKfXqWky8gbZnUQ1UFJ0guc1wZZc+PiinXGyHvRpS25HX8MywGIeiWCoGI6fGU27',
  'ctl00$Main$ctrl_Login$Login1$UserName': username,
  'ctl00$Main$ctrl_Login$Login1$Password': password,
  'ctl00$Main$ctrl_Login$Login1$LoginButton': 'Login'
}

session = requests.session()

login_response = session.post('http://www.iti.gov.eg/Site/Login', data=data, verify=False)

if is_successfull_login(login_response):
    print("Logged in sucessfully!")

    # Infitie loop to check for changes in website
    while True:
        status_response = session.get('http://www.iti.gov.eg/Admission/PTPprogram/intake41/ApplicationStatus', verify=False)
        if is_pending_status(status_response):
            print("pending")
        else:
            sos() # make some noise
            print("WAAAAAT")
        time.sleep(2*60) # Check every 2 minuites

else:
  print("Please enter correct username and password")
  sos()
  time.sleep(2*60)
  exit

