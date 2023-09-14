# Handling für Verbindungen
# Benutzung über das Modul -> Requests

import configparser
import requests

class ServerAPI():

    def __init__(self):
        self.configPath = "./Config/config.ini"
        self.config = configparser.ConfigParser()
        self.config.read_file(open(self.configPath, "r"))
        self.ip = self.config.get("server", "host")
        self.altip = self.config.get("server", "alternativeHost")
        self.port = self.config.get("server", "port")
        
    def checkConneection(self, UI_M):
        print("Pinging.. '" + self.ip+"'")

        try:
            UI_M.label_2.setText("Domain: "+self.ip)
            pingHost = requests.get("http://"+self.ip + "/ping", timeout=5)
            print("Host on ["+self.ip+"], sent an response.")
            return True
        except:
            pass

        try:
            UI_M.label_2.setText("Domain: "+self.altip)
            print("Host on ["+self.ip+"], no response.")
            print("Pinging Alternative Host.. '" + self.altip+"'")
            pingHost = requests.get("http://"+self.altip + "/ping", timeout=5)
            print("Host on ["+self.altip+"], sent an response.")
            self.ip = self.altip
            return True 
        except:
            print("Host on ["+self.altip+"], no response.")
            return False
        