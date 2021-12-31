#!/usr/bin/env python3

from picamera.camera import PiCamera
import pytest

def take_picture(camera, workdir:str, image_name:str, res_x:int, res_y:int):
    from time import sleep
    from os import path

    camera.resolution = (res_x, res_y)

    # camera warm-up time
    sleep(2)

    camera.capture(path.join(workdir, image_name))


    
@pytest.mark.order(1)
def test_camera(numberOfTakes:int = 6, res_x:int = 3280, res_y:int = 2464):
    import os
    from shutil import rmtree
    from picamera import PiCamera

    # Make sure the previous test run does not
    # affect the later ones
    if os.path.isdir('/tmp/pilapse-test'):
        rmtree('/tmp/pilapse-test', ignore_errors=True)
    os.mkdir('/tmp/pilapse-test')
    tempdir = '/tmp/pilapse-test'

    camera = PiCamera()


    # take several pictures to test multiple images
    # taking ability
    for picNum in range(numberOfTakes):
        take_picture(camera, tempdir, str(picNum) + '.jpg', res_x, res_y)