#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.9.0
#
#   Author:         Christopher A. Moody
#
#   Purpose:        A comapany branch needs to transfer new and/or modified
#                   files to the home office each day and they need a script that can decide
#                   which files are valid candidates for transfering. Create a program that
#                   can decide whether not a file is new or modified and add it to a directory
#                   that will be sent to the home office.
#
#   Tested OS:      Written and tested with Windows 10.


import shutil
import os


#----------------------
#   FILE LOCATIONS
#----------------------
#set where the source of the files are
src = '/Users/Moody/Documents/GitHub/Python_projects/challenges/File_Transfer_Program/new_orders/'
src_files = os.listdir(src)

# set the destination of the files to be transfered to home office
dst = '/Users/Moody/Documents/GitHub/Python_projects/challenges/File_Transfer_Program/transfers/'
dst_files = os.listdir(dst)


#-----------------------
#   FILE CHECK/COPY OPERATION
#-----------------------

class FileCheck():
    def __init__(self, filename):
        self._cached_stamp = 0
        self.filename = filename # gets filename

    def look(self):
        stamp = os.stat(self.filename).st_mtime
        # define stamp equal to the modify time of given file
        if stamp != self._cached_stamp:
        # checks if the modify time is not equal to cached_stamp
        # which starts as 0. if true, then set cached_stamp equal to
        # stamp(file mod time) and return True
            self._cached_stamp = stamp
            return True
        else:
            return False

# iterate through each file in src directory
# if FileCheck supplied with specified file returns True
# then copy to dst directory
for i in src_files:
    if FileCheck(i):
        shutil.copy2(src + i,dst)

