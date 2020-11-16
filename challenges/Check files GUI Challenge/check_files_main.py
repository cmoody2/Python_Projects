#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.9.0
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Create a gui using Tkinter module
#
#   Tested OS:      Written and tested with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


import check_files_func
import check_files_gui

# our main gui class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,170)  #width,height
        self.master.maxsize(500,170)  #width,height

        check_files_func.center_window(self, 500, 170)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        #protocol for a usable close button in the gui itself that will
        #ask before closing using a popup window
        self.master.protocol("WM_DELETE_WINDOW", lambda: check_files_func.ask_quit(self))
        arg = self.master
        check_files_gui.load_gui(self)


if __name__ == "__main__":
    #this makes sure the window stays open
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
