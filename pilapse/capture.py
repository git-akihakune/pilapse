#!/usr/bin/env python3

class camera:
    def __init__(self, workdir = '~/Videos/pilapse', length: int = 3280, width: int = 2464):
        # Set up logging
        from .logger import logging
        self.log = logging

        # Set up Pi Camera
        from picamera import PiCamera
        self.camera = PiCamera()
        self.camera.resolution = (length, width)
        
        # Set up working directory
        from os import chdir, getcwd
        self._setUpWorkingDir(workdir)
        chdir(workdir)
        self.log.info(f"Working directory: {getcwd()}")

        # camera warm-up time
        from time import sleep
        sleep(2)
        
        self.log.success(f"Successfully set up camera.")



    def _setUpWorkingDir(self, workdir: str):
        import os, shutil

        if not os.path.exists(workdir):
            self.log.info("Specified save path not found. Creating one...")
            os.makedirs(workdir, exist_ok=True)
            self.log.info(f"Created {workdir}")
        elif not os.listdir(workdir) == []:
            # prompt the user to ask if the specified directory
            # should be deleted
            self.log.warning("The specified path seems to already contains files. Continue will overwrite all data in that directory.")
            if (input("[prompt] Continue and overwrite all files? [y/n] ") == "y"):
                shutil.rmtree(workdir)
                os.makedirs(workdir, exist_ok=True)
        else:
            self.log.info(f"{workdir} seems already initiated")



    def capture(self, imageName: str, addTime: bool = False, singleCapture: bool = False):
        self.camera.capture(imageName)
        if singleCapture:
            import os
            self.log.success(f"Image saved at {os.path.join(os.getcwd(), imageName)}")



    def record(self, duration: int, frequency: int, continuous: bool = False):
        import os
        from time import sleep
        if continuous:
            for filename in self.camera.capture_continuous('img{counter:03d}.jpg'):
                self.log.info(f"Captured {filename}")
                sleep(frequency)