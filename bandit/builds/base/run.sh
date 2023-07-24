#!/bin/bash

# Create a directory for the passwords
mkdir /etc/blacktuque

# Source the passwords file to load variables
source ./passwords.txt

for ((user_num = 0; user_num <= $1; user_num++));
do
  # Create group and user
  username=bandit$user_num
  groupadd -g $((1000 + $user_num)) $username
  useradd -rm -s /bin/bash -u $((1000 + $user_num)) -g $username $username

  # Update the password for the user
  PASSWORD_VAR="BANDIT$user_num"
  echo "$username:${!PASSWORD_VAR}" | chpasswd

  # Hush login output, tmatrix and motd configuration in .profile for each user
  touch /home/$username/.hushlogin
  echo "tmatrix -t 'TEST 3' --no-fade" >> /home/$username/.profile
  echo "cat /etc/motd" >> /home/$username/.profile

  # Create directory with limited permissions for the password of the user
  mkdir /etc/blacktuque/$username
  chown $username:$username /etc/blacktuque/$username
  chmod 700 /etc/blacktuque/$username
done
