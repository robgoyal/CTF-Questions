#!/usr/bin/python3

CURR_PASSWORD = "<ARG_CURR_USER_PASSWORD>"
NEXT_USERNAME = "<ARG_NEXT_USER_USERNAME>"
NEXT_PASSWORD = "<ARG_NEXT_USER_PASSWORD>"

try:
    guess = input("Submit the current user's password: ")
    if guess == CURR_PASSWORD:
        print(f"Correct! For your rewards, the password for {NEXT_USERNAME} is: '{NEXT_PASSWORD}'")
    else:
        print("Incorrect...Please try again.")
except Exception as e:
    print("Uh oh, something went wrong")
