#!/usr/bin/env python3

"""piLapse - capture time lapse image on Raspberry Pi.

Usage:
    pilapse configure
    pilapse record [-d <duration>] [-f <frequency>] [-F <fps>] [-s <save-dir>] [--preserve] [--verbose]
    pilapse (-h | --help)
    pilapse --version

Options:
-h --help                   Show this screen.
-d --duration DURATION      Set recording duration (by seconds) [default: 600].
-f --frequency FREQUENCY    Set time interval between shots (by seconds) [default: 5].
-F --fps FPS                Set final video fps [default: 24].
-s --save-dir SAVINGDIR     Set working and saving directory [default: ~/Videos/pilapse].
-p --preserve               Do not automatically clean up after recording.
--verbose                   Set to verbose mode.
--version                   Show version.


"""
from docopt import docopt
from . import __version__

if __name__  == "__main__":
    arguments = docopt(__doc__, version=__version__)
    print(arguments)