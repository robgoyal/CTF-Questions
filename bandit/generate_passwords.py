#!/usr/bin/python3
import os
import random
import string
import shutil

NUM_CHALLENGES = 25

# Paths for the .env files containing the password
dockerfile_env_path = os.path.join(os.getcwd(), ".env")
dockerfile_base_img_env_path = os.path.join(os.getcwd(), "builds/base/.env")



# Generate passwords 
chars = string.ascii_letters + string.digits
with open(dockerfile_env_path, "w") as f:
    # First password should just be bandit0
    f.write(f"BANDIT0=bandit0\n")
    for i in range(1, NUM_CHALLENGES + 1):
        random_password=''.join(random.choices(chars, k=10))
        f.write(f"BANDIT{i}={random_password}\n")

# Create symlink
try:
    os.remove(dockerfile_base_img_env_path)
except:
    pass
shutil.copy(dockerfile_env_path, dockerfile_base_img_env_path)
