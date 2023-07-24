#!/bin/bash

export <ARG_NEXT_USER_USERNAME>_password=<ARG_NEXT_USER_PASSWORD>

su -c 'while true; do echo "$<ARG_NEXT_USER_USERNAME>_password" > /tmp/password.txt; sleep 10; done &' <ARG_CURR_USER_USERNAME>
/usr/sbin/sshd -D
