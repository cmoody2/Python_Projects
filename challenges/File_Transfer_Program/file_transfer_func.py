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
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import file_transfer_main
import file_transfer_gui


#---------------------------------
#   Window GUI Functions
#---------------------------------
def center_window(self, w, h):  # Pass in the tkinter frame (master) reference and the w and h
    # Get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # Calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


#---------------------------------
#   Directory Button Function
#---------------------------------
def askdir(self):
    folder = filedialog.askdirectory(initial="/")
    self.txt_browse.insert(0,folder)

def askdir2(self):
    folder = filedialog.askdirectory(initial="/")
    self.txt_browse2.insert(0,folder)

#----------------------
#   FILE LOCATIONS
#----------------------

#set where the source of the files are
##src = '{}'.format(self.txt_browse.get())
##src_files = os.listdir(src)

# set the destination of the files to be transfered to home office
##dst = '/Users/Moody/Documents/GitHub/Python_projects/challenges/File_Transfer_Program/transfers/'
##dst_files = os.listdir(dst)


#-----------------------
#   FILE CHECK/COPY OPERATION
#-----------------------

class FileCheck():
    def cache(self, filename):
        self._cached_stamp = 0
        self.filename = filename # gets filename
        
    def paths(self):
        #set where the source of the files are
        src = '{}'.format(self.txt_browse.get())
        src_files = os.listdir(src)

        # set the destination of the files to be transfered to home office
        dst = '{}'.format(self.txt_browse2.get())
        dst_files = os.listdir(dst)
        
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
def transfer():
    for i in src_files:
        if FileCheck(i):
            shutil.copy2(src + i,dst)


if __name__ == "__main__":
    pass

