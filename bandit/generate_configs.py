#!/usr/bin/python3

import os
NUM_CHALLENGES = 25

# Verify that the ./config directory exists
BASE_PATH = os.path.join(os.getcwd(), "builds/sshpiper/configs")

if not os.path.exists(BASE_PATH):
    os.mkdir(BASE_PATH)

for i in range(0, NUM_CHALLENGES + 1):
    userpath = os.path.join(BASE_PATH, f"bandit{i}")
    if not os.path.exists(userpath):
        os.mkdir(userpath)

    filepath = os.path.join(userpath, "sshpiper_upstream")
    with open(filepath, "w") as f:
        f.write(f"bandit{i}@bandit-{i}-ctr:22")
