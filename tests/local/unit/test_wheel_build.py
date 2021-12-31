#!/usr/bin/env python3

import os
import pytest

# to make sure this runs from root directory

def test_cwd():
    currentPath = os.getcwd()

    # Get the name of current directory only
    currentDir = currentPath[currentPath.rfind('/') + 1:]

    if currentDir != "pilapse" or "pilapse" not in os.listdir(currentPath):
        pytest.raises("Please execute tests from project's root directory.")


def test_wheel_build():
    os.system('pip wheel . -w wheels')