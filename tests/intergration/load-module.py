#!/usr/bin/env python3

# Load the module to a raspberry pi

import json
import paramiko
import os.path
from typing import Dict

if os.path.isfile('sensitive-credentials.json'):
    CREDS_FILE = 'sensitive-credentials.json'
else: CREDS_FILE = 'credentials.json'

with open(CREDS_FILE) as jsonFile:
    creds: Dict[str, str] = json.load(jsonFile)

def test_ssh_connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(creds['address'], username=creds['username'], password=creds['password'])

    (ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command("cat /etc/*-release")
    for line in ssh_stdout.readlines():
        print(line.rstrip())

    ssh.close()