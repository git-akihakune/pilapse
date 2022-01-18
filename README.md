# pilapse
Python module to capture time lapse videos on Raspberry Pi

## Installation
It's recommended to create a virtual environment, but it's not mandatory:
```bash
python -m venv pilapse
cd pilapse
source bin/activate
```

You can simply install pilapse from PyPi:
```bash
pip install pilapse
```

## Acknowledged issues
- [Keep the process running even after log out of SSH](https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session):
```bash
sudo apt install tmux
tmux
pilapse record
```
- [`numpy` error while making videos on Raspberry Pi](https://numpy.org/devdocs/user/troubleshooting-importerror.html):
```bash
sudo apt install libatlas-base-dev ffmpeg
```