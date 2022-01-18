#!/usr/bin/env python3

from typing import Dict


def _createConfigFile(path: str) -> None:
    """overwrite previous config file and create a new one"""
    import os
    CONFIG_FILE_PATH: str = os.path.join(path, 'pilapse.conf')
    if not os.path.isfile(CONFIG_FILE_PATH):
        import configparser
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'length': '1920',
            'width': '1080'
        }
        with open(CONFIG_FILE_PATH, 'w') as configfile:
            config.write(configfile)
    else:
        print(f"Config file already exists at {CONFIG_FILE_PATH}.")


def _loadConfig(path: str) -> Dict[str, str]:
    """Load config data from specified path"""
    import configparser
    from os.path import join
    config = configparser.ConfigParser()
    config.read(join(path, 'pilapse.conf'))
    return dict(config.items('DEFAULT'))