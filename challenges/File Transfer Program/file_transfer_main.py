#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.9.0
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Create a file transfer program that with use the
#                   shutil module to transfer files inbetween different
#                   directories.
#
#   Tested OS:      Written and tested with Windows 10.


import shutil
import os

# set where the source of the files are
source = '/Users/Moody/Desktop/folderA/'

# set the destination path to folderB
destination = '/Users/Moody/Desktop/folderB/'
files = os.listdir(source)

for i in files:
    # we are saying move the files represented by 'i' to their new destination
    shutil.move(source + i, destination)


