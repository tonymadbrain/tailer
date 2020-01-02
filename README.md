apt install python-setuptools
pip install wheel
pip install -r requirements.txt
#pip install --upgrade -r requirements.txt

fill tailer-environment, look example tailer-environment.example

cp tailer.service /etc/systemd/system/
systemctl daemon-reload
systemctl start tailer

journalctl -u tailer -f
