#!/bin/bash

chattr +i /opt/seed
cron
/usr/sbin/sshd -D
