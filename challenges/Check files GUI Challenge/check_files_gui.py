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

import check_files_main
import check_files_func


def load_gui(self):
    # gui buttons
    self.btn_browse = tk.Button(self.master, width=14, height=1, text='Browse...', command=lambda: check_files_func.askdir(self))
    self.btn_browse.grid(row=3, column=1, padx=(10,10), pady=(45,0), sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=14, height=1, text='Browse...', command=lambda: check_files_func.askdir2(self))
    self.btn_browse2.grid(row=4, column=1, padx=(10,10), pady=(8,0), sticky=W)
    self.btn_check = tk.Button(self.master, width=14, height=2, text='Check for files...')
    self.btn_check.grid(row=5, column=1, padx=(10,10), pady=(8,0), sticky=W)
    self.btn_close = tk.Button(self.master, width=14, height=2, text='Close Program', command=lambda: check_files_func.ask_quit(self))
    self.btn_close.grid(row=5, column=6, padx=(43,0), pady=(8,0), sticky=E)

    #gui text fields
    self.txt_browse = tk.Entry(self.master, width=55, text='')
    self.txt_browse.grid(row=3, column=2, rowspan=1, columnspan=6, padx=(14,40), pady=(45,0), sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master, text='')
    self.txt_browse2.grid(row=4, column=2, rowspan=1, columnspan=6, padx=(14,40), pady=(8,0), sticky=N+E+W)



if __name__ == "__main__":
    # passing to the main file
    pass
