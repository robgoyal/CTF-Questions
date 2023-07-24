#!/usr/bin/python3

import random
import string
import sys

# PASSWORD LINE
NUM_PASSWORDS = 100000
PASSWORD_LINE_NUMBER = random.choice(range(NUM_PASSWORDS))

# PASSWORD
actual_password = sys.argv[1]

"""
Final password matches the following characteristics:
    - $
    - 4 digits
    - colon
    - 2 spaces
    - password
"""

for i in range(NUM_PASSWORDS):
    # Skip generating a random line if the current index matches PASSWORD_LINE_NUMBER
    if i + 1 == PASSWORD_LINE_NUMBER:
        print(f"${random.choice(range(1000, 10000))}:  {actual_password}")
        continue
    
    # Final character
    starting_character = random.choice(['!', '$', '&', '%'])
    # Randomly choose between 3 to 4 digits
    pin = random.choice(range(100, 33333))
    # Choose between 1 or 2 choices
    spaces = random.choice(range(1, 4))
    # 10 - 13 passwords
    password_len = random.choice(range(10, 15))

    # generate alphanumeric password
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_len))
    if password_len == len(actual_password):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)-2) + random.choices('_-/', k=2))
    
    print(f"{starting_character}{pin}:{' ' * spaces}{password}")
