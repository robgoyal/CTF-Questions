#!/usr/bin/bash

/usr/sbin/vsftpd

sed -i 's/IPV6=yes/IPV6=no/g' /etc/default/ufw
ufw enable
ufw default reject incoming
ufw allow 20
ufw allow 21
ufw allow 64821
ufw allow 57492
ufw allow 26356
ufw allow 65500:65515/tcp

knockd &
(cd BabyShark && python3 app.py)
