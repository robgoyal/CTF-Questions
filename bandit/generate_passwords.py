#!/usr/bin/python3
import os
import random
import string

NUM_CHALLENGES = 25

# Paths for the .env files containing the password
dockerfile_env_path = os.path.join(os.getcwd(), ".env")
dockerfile_base_img_env_path = os.path.join(os.getcwd(), "builds/base/.env")

# Generate passwords 
chars = string.ascii_letters + string.digits
with open(dockerfile_env_path, "w") as f:
    # +1 because we need to account for the initial 0 user
    for i in range(NUM_CHALLENGES + 1):
        random_password=''.join(random.choices(chars, k=10))
        f.write(f"BANDIT{i}={random_password}\n")

# Create symlink
try:
    os.unlink(dockerfile_base_img_env_path)
except:
    pass
os.symlink(dockerfile_env_path, dockerfile_base_img_env_path)
