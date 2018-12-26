import requests
import json
from HTMLParser import HTMLParser
import lxml.html as lh

colour = {'blue':'\033[94m',
        'green':'\033[92m',
        'warning':'\033[93m',
        'fail':'\033[91m'}

class HTB(object):
    def __init__(self, configfile="config"):
        self.configfile = configfile
        self.cfg = self.config()

    def init(self):
        self.s = self.login()

    def config(self):
        try:
            cfg = json.loads(open(self.configfile, "r").read())
            #USER config
            api = cfg['api']
            self.userid = int(api['userid'])
            self.username = str(api['username'])
            self.password = str(api['password'])
            self.email = str(api['email'])
            #URL config
            url = cfg['url']
            self.machineUrl = str(url['machines'])
            self.loginUrl = str(url['login'])
            self.profileUrl = str(url['profile'])
            print(colour['green'] + "[+] config loaded successfully")
            return cfg
        except:
            print(colour['fail'] + "[-] " + self.configfile + " not found")

    def login(self):
        s=requests.Session()
        r=s.get(self.loginUrl)
        csrftoken=r.content.split('"csrf-token" content="')[1].split('"')[0]
        data={'_token':csrftoken,'email':self.email,'password':self.password}
        r=s.post(self.loginUrl,data=data)
        if not r.status_code == 200:
            print(colour['fail'] + "[-] Login failed")
        else:
            print(colour['green'] + "[+] Login Successful")
            return s

    def get_machines(self):
        machines = []
        s = self.s
        r=s.get(self.machineUrl)
        doc = lh.fromstring(r.content)
        print(colour['blue'] + "[*] attempting to get machine list with ips")
        tr_elements = doc.xpath('//tr')
        col = []
        i = 0
        #Get name of rows
        for t in tr_elements[0]:
            i+=1
            name=t.text_content()
            col.append((name, []))
        #Get second row onwards for machines
        for j in range(1,len(tr_elements)):
            t=tr_elements[j]
            #If there aren't 13 rows then it is not a part of machines
            if len(t)!=13:
                break
            #itterate through each elemnt of row
            i = 0
            for T in t.iterchildren():
                data=T.text_content()
                col[i][1].append(data)
                i+=1

        return col
