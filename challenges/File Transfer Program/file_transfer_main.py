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
import filecmp
import datetime as dt

### set where the source of the files are
##source = '/Users/Moody/Desktop/new_orders/'
##
### set the destination path to folderB
##destination = '/Users/Moody/Desktop/transfer_orders/'
##files = os.listdir(source)

comparison = filecmp.cmpfiles('new_orders','transfer_orders','common',shallow=False)

print(comparison)



