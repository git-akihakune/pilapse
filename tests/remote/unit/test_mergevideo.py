#!/usr/bin/env python3

import pytest
import os

@pytest.mark.order(4)
def test_copy_video():
    """Duplicate file /tmp/pilapse-test/image2vid.mp4 2 times"""

    if not os.path.isfile('/tmp/pilapse-test/image2vid.mp4'):
        pytest.skip("No process video file found")

    workDir = '/tmp/pilapse-test'

    import shutil
    source = os.path.join(workDir, 'image2vid.mp4')

    for dupName in ['dup1', 'dup2']:
        shutil.copyfile(source, os.path.join(workDir, f"image2vid-{dupName}.mp4"))


@pytest.mark.order(5)
def test_merge_video():
    """Merge 2 above duplicated videos"""

    workDir = '/tmp/pilapse-test'
    video1 = os.path.join(workDir, 'image2vid-dup1.mp4')
    video2 = os.path.join(workDir, 'image2vid-dup2.mp4')

    if not (os.path.isfile(video1) and os.path.isfile(video2)):
        pytest.skip("Not enough duplicated video files found")

    from moviepy.editor import VideoFileClip, concatenate_videoclips

    video1 = VideoFileClip(video1)
    video2 = VideoFileClip(video2)
    merged = concatenate_videoclips([video1, video2])
    merged.write_videofile(os.path.join(workDir, 'merged.mp4'))