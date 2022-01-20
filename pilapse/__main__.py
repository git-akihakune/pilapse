#!/usr/bin/env python3
from .arguments import arguments
from . import capture
from .compileVideo import compileVideo
from .interface import banner, print_statusline
from time import sleep


def main():  
    # print program banner if verbose is set
    if arguments['--verbose']:
        banner()

    if arguments['compile']:
        compileVideo(workDir=arguments['--save-dir'], videoName=arguments['--output-video'], fps=int(arguments['--fps']))
        exit()

    camera = capture.camera(workdir=arguments['--save-dir'], length=int(arguments['--length']), width=int(arguments['--width']))

    if arguments['capture']:
        camera.capture(imageName=arguments['--image-name'])
    
    elif arguments['record']:
        waitingTime = int(arguments['--shutter-wait'])
        if waitingTime != 0:
            for sec in range(0, waitingTime + 1):
                print_statusline(f"Countdown before record: {waitingTime - sec}")
                sleep(1)
        camera.record(duration=int(arguments['--duration']), frequency=int(arguments['--frequency']), continuous=arguments['--continuous'])


if __name__  == "__main__":
    main()