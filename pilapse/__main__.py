#!/usr/bin/env python3

"""piLapse - capture time lapse video on Raspberry Pi.

Usage:
    pilapse capture [-i <image-name>] [-s <save-dir>]
    pilapse record [-d <duration> | -c] [-f <frequency>] [-l <length>] [-w <width>] [-F <fps>] [-s <save-dir>] [-S <wait-time>] [--no-text] [--preserve] [--verbose]
    pilapse compile [-s <save-dir>]
    pilapse (-h | --help)
    pilapse --version

Actions:
capture     Take 1 image only.
record      Record a timelapse video.
compile     Compile labelled images into a video.

Options:
-h --help                   Show this screen.
-c --continuous             Set to continuously run mode.
-d --duration DURATION      Set recording duration (by seconds) [default: 600].
-f --frequency FREQUENCY    Set time interval between shots (by seconds) [default: 5].
-F --fps FPS                Set final video fps [default: 24].
-l --length LENGTH          Set image length dimension (by pixel) [default: 3280].
-w --width WIDTH            Set image width dimension (by pixel) [default: 2464].
-s --save-dir SAVINGDIR     Set working and saving directory [default: ~/Videos/pilapse].
-S --shutter-wait TIME      Set timer before start capturing (by seconds) [default: 0].
-p --preserve               Do not automatically clean up after recording.
-i --image-name NAME        Set image name in capture mode [default: image.jpg].
-n --no-text                Do not add time in capture mode.
--verbose                   Set to verbose mode.
--version                   Show version.


"""
from docopt import docopt
from . import __version__
from . import capture


def main():
    arguments = docopt(__doc__, version=__version__)
    camera = capture.camera(workdir=arguments['--save-dir'], length=int(arguments['--length']), width=int(arguments['--width']))

    if arguments['capture']:
        camera.capture(imageName=arguments['--image-name'], singleCapture=True)
    elif arguments['record']:
        camera.record(duration=int(arguments['--duration']), frequency=int(arguments['--frequency']), continuous=arguments['--continuous'])

if __name__  == "__main__":
    main()