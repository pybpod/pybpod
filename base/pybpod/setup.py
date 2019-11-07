#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

with open(os.path.join("README.md"), "r") as fd:
    long_description = fd.read()

setup(
    name="pybpod",
    version="1.8.0",
    description="Pybpod is a behavioral experiments control system written in Python for Bpod",
    author=["Ricardo Ribeiro", "Luís Teixeira"],
    author_email="ricardo.ribeiro@research.fchampalimaud.org, ricardojvr@gmail.com, micboucinha@gmail.com",
    license="MIT",
    url="https://pybpod.readthedocs.io",
    include_package_data=True,
    packages=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "pyforms-gui==4.901.2",
        "pyforms_generic_editor==1.5.1",
        "pybpod-api==1.8.0",
        "pybpod-gui-api==1.8.0",
        "pybpod-gui-plugin==1.8.0",
        "pge-plugin-terminal==0.1",
        "pybpod-gui-plugin-session-history==1.4.2",
        "pybpod-gui-plugin-stmdiagram==1.0.0",
        "pybpod-gui-plugin-timeline==1.0.1",
        "pybpod-gui-plugin-trial-timeline==1.0.0",
        "pybpod-gui-plugin-waveplayer==1.0",
        "pybpod-gui-plugin-rotaryencoder==0.1.4",
        "pybpod-gui-plugin-soundcard==0.1.6",
        "pybpod-gui-plugin-emulator==0.1.4",
    ],
    entry_points={
        "console_scripts": ["start-pybpod=pybpodgui_plugin.__main__:start"],
    },
)
