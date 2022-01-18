#!/usr/bin/env python3

class camera:
    def __init__(self, workdir = '~/Videos/pilapse', length: int = 3280, width: int = 2464):
        from os import chdir, getcwd
        from picamera import PiCamera
        from time import sleep

        self.camera = PiCamera()
        self.camera.resolution = (length, width)

        # process relative paths
        if workdir[0] == '~':
            from pathlib import Path
            homeDir = str(Path.home())
            workdir = workdir.replace('~', homeDir, 1)
        
        self._setUpWorkingDir(workdir)
        chdir(workdir)

        # camera warm-up time
        sleep(2)
        print(f"Successfully set up camera. Working at {getcwd()}")



    def _setUpWorkingDir(self, workdir: str):
        import os, shutil

        if not os.path.exists(workdir):
            print("Specified save path not found. Creating one.")
            os.makedirs(workdir, exist_ok=True)
        elif not os.listdir(workdir) == []:
            # prompt the user to ask if the specified directory
            # should be deleted
            print("The specified path seems to already contains files. Continue will overwrite all data in that file.")
            if (input("Continue? [y/n] ") == "y"):
                shutil.rmtree(workdir)
                os.makedirs(workdir, exist_ok=True)
        else:
            print(f"{workdir} seems already initiated")



    def capture(self, imageName: str, addTime: bool = False, singleCapture: bool = False):
        self.camera.capture(imageName)
        if singleCapture:
            import os
            print(f"Image saved at {os.path.join(os.getcwd(), imageName)}")



    def record(self, duration: int, frequency: int, continuous: bool = False):
        import os
        from time import sleep
        if continuous:
            for filename in self.camera.capture_continuous('img{counter:03d}.jpg'):
                print(f"Captured {filename}")
                sleep(frequency)