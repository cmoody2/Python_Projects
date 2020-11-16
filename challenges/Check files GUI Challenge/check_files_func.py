#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.9.0
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Create a gui using Tkinter module
#
#   Tested OS:      Written and tested with Windows 10.


import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import check_files_gui
import check_files_main

# this centers the gui window
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



if __name__ == "__main__":
    pass
