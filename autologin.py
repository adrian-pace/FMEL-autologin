import requests
import os
import credentials

USERNAME = credentials.USERNAME
PASSWORD = credentials.PASSWORD

# testing internet connection

r=requests.get("http://google.com")
if 'world-connect' not in r.text:
    print('connected to the internet')
    exit()


headers = {"Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "DNT": "1",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "en-US,en;q=0.9,fr;q=0.8"}

r = requests.get("http://google.com", headers=headers)
PHPSESSID = r.cookies['PHPSESSID']
NYInit = r.cookies['NYInit']
NYmac = r.cookies['NYmac']
NYip = r.cookies['NYip']
NYTag = r.cookies['NYTag']
NYFromItf = r.cookies['NYFromItf']

headers['Cookie'] = "PHPSESSID={}; NYInit={}; NYmac={}; NYINITURL=http%3A%2F%2Fgoogle.com%2F; NYip={}; NYTag={}; " \
                    "NYFromItf={}".format(PHPSESSID, NYInit, NYmac, NYip, NYTag, NYFromItf)
headers['Referer'] = 'http://google.com/'
r = requests.get("https://login.world-connect.ch/portail.php3?nyretries=2&zone=-1&INITURL=http://google.com/",
                 headers=headers)

headers['Referer'] = "https://login.world-connect.ch/portail.php3?nyretries=2&zone=-1&INITURL=http://google.com/"
headers['Content-Type'] = 'application/x-www-form-urlencoded'
payload = {"cgu": "1",
           "connect": "connecter",
           "connect.x": "47",
           "connect.y": "16",
           "login": USERNAME,
           "passwd": PASSWORD}

p = requests.post("https://login.world-connect.ch/authinprocess.php3", headers=headers, data=payload)

payload['PopupFlag'] = '0'
payload['TheUrlFailed'] = 'https://login.world-connect.ch/portail.php3?lang=&INITURL=http%3A%2F%2Fgoogle.com%2F'
payload['TheUrlSuccess'] = 'http://google.com/'
payload['ZoneId'] = ""

p = requests.post('https://login.world-connect.ch/connector.php', headers=headers, data=payload)

print('Connected to the Internet')

# COMMENT THIS IF NOT ON MAC
# $ [sudo] gem install terminal-notifier
# os.system("terminal-notifier -title 'FMEL Auto Login' "
#           "-subtitle 'Connected to Internet' "
#           "-message 'You are now connected to the internet'")
