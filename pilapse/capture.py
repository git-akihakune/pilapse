#!/usr/bin/env python3

class camera:
    def __init__(self, workdir = '~/Videos/pilapse', length: int = 3280, width: int = 2464):
        from picamera import PiCamera
        from time import sleep

        # process relative paths
        if workdir[0] == '~':
            from pathlib import Path
            homeDir = str(Path.home())
            workdir = workdir.replace('~', homeDir, 1)

        self.camera = PiCamera()
        self.camera.resolution = (length, width)

        # camera warm-up time
        sleep(2)

        self.workdir = workdir
        self._setWorkingDir()


    def _setWorkingDir(self):
        import os, shutil

        print(f"Working dir at {self.workdir}")

        if not os.path.exists(self.workdir):
            print("Specified save path not found. Creating one.")
            os.makedirs(self.workdir, exist_ok=True)
        elif not os.listdir(self.workdir) == []:
            # prompt the user to ask if the specified directory
            # should be deleted
            print("The specified path seems to already contains files. Continue will overwrite all data in that file.")
            if (input("Continue? [y/n] ") == "y"):
                shutil.rmtree(self.workdir)
                os.makedirs(self.workdir, exist_ok=True)
        else:
            print(f"{self.workdir} seems already initiated")



    def capture(self, imageName: str):
        from os.path import join
        self.camera.capture(join(self.workdir, imageName))


    def record(self, duration: int, frequency: int):
        pass