#!/usr/bin/env python3

# Because it's better not to rely on external libraries
class logger:
    def __init__(self, verbose: bool) -> None:
        self.verbose = verbose
    
    def error(self, text): print("{} {}".format("\033[95m[error]\033[00m", text))
    def critical(self, text): print("{} {}".format("\033[91m[critical]\033[00m", text)) 
    
    def debug(self, text): 
        if self.verbose:
            print("{} {}".format("\033[94m[debug]\033[00m", text))
    
    def info(self, text): 
        if self.verbose:
            print("{} {}".format("\033[96m[info]\033[00m", text))
    
    def warning(self, text): 
        if self.verbose:
            print("{} {}".format("\033[93m[warn]\033[00m", text))
    
    def success(self, text): 
        if self.verbose:
            print("{} {}".format("\033[92m[success]\033[00m", text))


def banner():
    """Print the program's banner"""
    banner = """
 ____  ____  __      __    ____  ___  ____ 
(  _ \(_  _)(  )    /__\  (  _ \/ __)( ___)
 )___/ _)(_  )(__  /(__)\  )___/\__ \ )__) 
(__)  (____)(____)(__)(__)(__)  (___/(____)

"""
    print(f"\033[96m{banner}\033[00m")
    print("Capture & record time lapse videos on Raspberry Pi!")
    print("\033[95m{}\033[00m".format("@akihakune, https://github.com/git-akihakune/pilapse"))
    print()