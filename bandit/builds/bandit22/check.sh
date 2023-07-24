#!/bin/bash

FILE=/opt/seed
CURRENT_USER=$1
NEXT_USER=$2

if [ -f "$FILE" ]; then
  contents=$(<$FILE)
  if [ "$contents" = "This is my world. My world!" ]; then
    cat /etc/blacktuque/$NEXT_USER/password > /home/$CURRENT_USER/$NEXT_USER-password
  fi
else 
  exit
fi
