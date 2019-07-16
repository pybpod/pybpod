#!/usr/bin/python
# -*- coding: utf-8 -*-
import re, os
from setuptools import setup

with open(os.path.join('README.md'), 'r') as fd:
    long_description = fd.read()

setup(
    name='pybpod',
    version="1.7.8",
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
        'pyforms-gui==4.901.2',
        'pyforms_generic_editor==1.5.1',
        'pybpod-api==1.6.4',
        'pybpod-gui-api==1.2.2',
        'pybpod-gui-plugin==1.6.2',
        'pge-plugin-terminal==0.1',
        'pybpod-gui-plugin-session-history==1.4.1',
        'pybpod-gui-plugin-stmdiagram==1.0.0',
        'pybpod-gui-plugin-timeline==1.0.1',
        'pybpod-gui-plugin-trial-timeline==1.0.0',
        'pybpod-gui-plugin-waveplayer==1.0',
        'pybpod-gui-plugin-rotaryencoder==0.1.1',
        'pybpod-gui-plugin-soundcard==0.1.5',
        'pybpod-gui-plugin-emulator==0.1.3'
    ],
    entry_points={
        'console_scripts': [
            'start-pybpod=pybpodgui_plugin.__main__:start',
        ],
    }
)
