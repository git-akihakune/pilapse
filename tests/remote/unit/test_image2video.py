#!/usr/bin/env python3

import pytest
import os

def _naturalSort(sortingList: list[str]) -> list:
    import re

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(sortingList, key=alphanum_key)


@pytest.mark.order(3)
def test_image2video():
    workDir = '/tmp/pilapse-test'
    if not os.path.isdir(workDir):
        pytest.skip('No captured image found')
    
    import moviepy.video.io.ImageSequenceClip

    imageFiles = [
        os.path.join(workDir, img)
        for img in _naturalSort(os.listdir(workDir))
        if img.endswith(".jpg")
    ]

    video = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(
        imageFiles, fps=22
    )
    video.write_videofile(os.path.join(workDir, 'image2vid.mp4'))