#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import call
from install import install


call(["git", "pull", "--recurse-submodules"])
install()

