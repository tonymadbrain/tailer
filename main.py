import sys
import os
import time
from pygtail import Pygtail
import requests
from requests.auth import HTTPBasicAuth
import json
import socket

tg_bot  = os.environ['TG_BOT']
tg_user = os.environ['TG_USER']
tg_pass = os.environ['TG_PASS']
tg_chat = os.environ['TG_CHAT']
tg_host = os.environ['TG_HOST']
tg_url  = 'https://{}/bot{}/sendMessage'.format(tg_host, tg_bot)

if len(sys.argv) != 2:
    print('no log file given, usage: tailer.py /var/log/myprogram.log')
    sys.exit()
else:
    logfile = sys.argv[1]
    pygt = Pygtail(logfile, read_from_end=True)
    while True:
        for line in pygt:
            if 'No such file or directory' in line:
                print('skipped due rule: {}'.format(line))
            else:
                text = 'On {}, nginx error:\n```{}```'.format(socket.gethostname(), line)
                data = {
                    'chat_id': tg_chat,
                    'disable_notification': True,
                    'parse_mode': 'Markdown',
                    'text': text
                    }
                #print(data)
                r = requests.post(url=tg_url, data=json.dumps(data), auth=HTTPBasicAuth(tg_user, tg_pass), headers={'Content-Type': 'application/json'})
                if r.status_code != 200:
                    print(r.text)
        #    "error" in line
        #    sys.stdout.write(line)
        time.sleep(1)
