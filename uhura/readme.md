to autostart uhura

sudo pip install paho-mqtt   (make sure this is installed as root otherwise startup will fail)
create symbolic link from /etc/systemd/system/uhura.service to /home/pi/uhura/uhura.service

sudo systemctl daemon-reload
sudo systemctl enable uhura.service

to start the service:
sudo systemctl start uhura.service


to stop the service:
sudo systemctl stop uhura.service

to check status:
sudo systemctl status uhura.service
