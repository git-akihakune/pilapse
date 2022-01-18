#!/usr/bin/env python3
import os

def _naturalSort(sortingList: list[str]) -> list:
    import re

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(sortingList, key=alphanum_key)



def compileVideo(workDir: str, videoName: str, fps: int = 24):
    if not os.path.isdir(workDir):
        print('No captured image found')
    
    import moviepy.video.io.ImageSequenceClip

    imageFiles = [
        os.path.join(workDir, img)
        for img in _naturalSort(os.listdir(workDir))
        if img.endswith(".jpg")
    ]

    print(f"Images file found: {imageFiles}")

    video = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(
        imageFiles, fps=fps
    )
    video.write_videofile(os.path.join(workDir, videoName))
    
    print("Video file created.")