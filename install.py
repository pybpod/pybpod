#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pip, os
from subprocess import call

SUBMODULES_FOLDERS = [
    'logging-bootstrap',
    'pysettings',
    'pyforms',
    'pyforms-generic-editor',
    'pybpod-api',
    'pybpod-gui-api',
    'pybpod-gui-plugin',
    'pybpod-gui-plugin-session-history',
    'pybpod-gui-plugin-timeline',
    'pybpod-rotary-encoder-module'
]

def install():
    for submodule in SUBMODULES_FOLDERS:
        pip.main(['install', '--upgrade', os.path.join(submodule,'.')])

def check_submodules():
    for submodule in SUBMODULES_FOLDERS:
        if not os.path.exists(os.path.join(submodule,'setup.py')):
            call(["git", "pull", "--recurse-submodules"])
            break


if __name__=='__main__': 
    install()