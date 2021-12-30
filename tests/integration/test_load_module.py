#!/usr/bin/env python3

# Load the module to a raspberry pi

import json
import paramiko
import os.path
from scp import SCPClient
from typing import Dict, List

### Loading config ###

# Load from sensitive file to avoid commiting sensitive files
# to version control
if os.path.isfile('tests/config/sensitive-credentials.json'):
    CREDS_FILE = 'tests/config/sensitive-credentials.json'
else: CREDS_FILE = 'tests/config/credentials.json'
LOAD_DIRS_CONFIG_FILE = 'tests/config/load-dirs.json'

with open(CREDS_FILE) as jsonFile:
    creds: Dict[str, str] = json.load(jsonFile)

with open(LOAD_DIRS_CONFIG_FILE) as jsonFile:
    loadDirs: List[str] = json.load(jsonFile)['load-dirs']
### End config loading ###


def createSSHClient() -> paramiko.client.SSHClient:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(creds['address'], port=creds['port'], username=creds['username'], password=creds['password'])
    return ssh


def allowedDir(ssh: paramiko.client.SSHClient) -> str:
    """Iterate through predefined dirs in load-dirs.json to find a directory to transfer to"""
    for testingDir in loadDirs:
        (ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command(f'mkdir {os.path.join(testingDir, "pilapse")}')
        err = ''.join([line.rstrip() for line in ssh_stderr.readlines()])
        if 'Permission denied' in err:
            continue
        elif 'File exists' in err:
            ssh.exec_command(f'rm -rf {os.path.join(testingDir, "pilapse")}')
            ssh.exec_command(f'mkdir {os.path.join(testingDir, "pilapse")}')
            return os.path.join(testingDir, 'pilapse')
        else:
            return os.path.join(testingDir, 'pilapse')

    # if all else false, may the /tmp directory allowed
    (ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command(f'mkdir {os.path.join("/tmp", "pilapse")}')
    return os.path.join('/tmp', 'pilapse')


def test_transfer():
    ssh = createSSHClient()
    scp = SCPClient(ssh.get_transport())
    remoteDir = allowedDir(ssh)
    scp.put('pilapse', recursive=True, remote_path=remoteDir)
    scp.close()
    ssh.close()