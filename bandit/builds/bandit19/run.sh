#!/bin/bash

USERNAME=$1
PASSWORD=$2
GITDIR=/home/$USERNAME/nettools

mkdir $GITDIR
cd $GITDIR
find /tmp/versions/ -type f -exec sed -i "s/<ARG_NEXT_USER_PASSWORD>/$PASSWORD/g" {} \;

git init
git config user.email "$USERNAME@bandit.local"
git config user.name "$USERNAME"

touch main.py
git add main.py
git commit -m "Initial commit"
git checkout -b "dev"

# Initial commit
cp /tmp/versions/v1-main.py main.py
git add main.py
git commit -m "POC: calling a system command in Python"

# Second commit
cp /tmp/versions/v2-main.py main.py
git add main.py
git commit -m "POC: calling a process as another user and password their password"

# Third commit
cp /tmp/versions/v3-main.py main.py
git add main.py
git commit -m "Fixes issue where subprocess response is a bytes object and needs to decode"

# Fourth commit
cp /tmp/versions/v4-main.py main.py
git add main.py
git commit -m "POC: pass a password to sudo using subprocess"

# Fifth commit
cp /tmp/versions/v5-main.py main.py
git add main.py
git commit -m "POC: capture network traffic using tcpdump"

# Sixth commit
cp /tmp/versions/v6-main.py main.py
git add main.py
git commit -m "Removes hardcoded password, adds functions to print ip config, routing table, and ports/connections"

# Merge branches
git checkout master
git merge --squash dev
git commit -m "Merge dev into main"

# Seventh commit
cp /tmp/versions/v7-main.py main.py
git add main.py
git commit -m "Adds docstrings, cleans up code, removes password from sudo"

# Delete everything
rm /tmp/run.sh
rm -r /tmp/versions
