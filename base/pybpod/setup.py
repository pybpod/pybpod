#!/usr/bin/python
# -*- coding: utf-8 -*-
import re, os
from setuptools import setup

with open(os.path.join('README.md'), 'r') as fd:
    long_description = fd.read()

setup(
    name='pybpod',
    version="1.7.5",
    description="Pybpod is a behavioral experiments control system written in Python for Bpod",
    author=['Ricardo Ribeiro', 'Luís Teixeira'],
    author_email='ricardo.ribeiro@research.fchampalimaud.org, ricardojvr@gmail.com, micboucinha@gmail.com',
    license='Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>',
    url='https://pybpod.readthedocs.io',
    include_package_data=True,
    packages=[],
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires = [
        'pyforms-gui',
        'pyforms_generic_editor',
        'pybpod-gui-api',
        'pybpod-gui-plugin',
        'pge-plugin-terminal',
        'pybpod-gui-plugin-session-history',
        'pybpod-gui-plugin-stmdiagram',
        'pybpod-gui-plugin-timeline',
        'pybpod-gui-plugin-trial-timeline',
        'pybpod-gui-plugin-waveplayer',
        'pybpod-gui-plugin-rotaryencoder',
        'pybpod-gui-plugin-soundcard',
        'pybpod-gui-plugin-emulator'
    ],
    entry_points={
        'console_scripts': [
            'start-pybpod=pybpodgui_plugin.__main__:start',
        ],
    }
)
