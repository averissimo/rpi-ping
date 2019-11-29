import os
import sys
import time
import yaml
import subprocess

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

def ping_me(hostname):
    response = subprocess.run(['ping', '-q', '-c 1', '172.17.2.1'], stdout=subprocess.DEVNULL)
    return response.returncode

for x in range(0, cfg['retry'] - 1):
    if ping_me(cfg['hostname']) == 0:
        print('Sucess!! We have connection to Telekom_FON')
        sys.exit()
    print('No ping.. retrying ', cfg['retry'] - x - 1, ' more times')
    time.sleep(3)

os.system("wpa_cli -i wlan1 disconnect && wpa_cli -i wlan1 reconnect")
