# If the exact combination is the following:
# - bandit17 => user
# - bandit16 => group
# - /usr/local/src => location
# - repetitions => 50,60,70,80,90,100

import random
import string
import sys
import os
import uuid
import pwd

# passed arguments 
users = sys.argv[1].split(",")
groups = sys.argv[1].split(",")
actual_password = sys.argv[2]
password_len = len(actual_password)

# list of possible directories
directories = ["/srv", "/run", "/opt", "/usr/local/src", "/var/mail", "/var/opt"] + [f"/home/{user}" for user in users]

def generate_file(filepath, user, group, lines, password):
    with open(filepath, "w") as f:
        for i in range(lines):
            f.write(f"The password for the next user is: {password}\n")

    userdata = pwd.getpwnam(user)
    groupdata = pwd.getpwnam(group)
    os.chown(filepath, userdata.pw_uid, groupdata.pw_gid)


# Generate 500 files
for i in range(500):
    user = random.choice(users)
    group = random.choice(groups)
    directory = random.choice(directories)
    lines = random.choice(range(50, 101, 10))

    # random password unless the criteria is met for the actual file location
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_len))
    random_filename = str(uuid.uuid4())

    # Check if we ended up at the following combination AND we haven't planted the password
    if not (user == users[1] and group == groups[0] and lines == 90):
        generate_file(os.path.join(directory, random_filename), user, group, lines, random_password)

generate_file(os.path.join("/usr/local/src", str(uuid.uuid4())), users[1], groups[0], 90, actual_password)
