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
    self.btn_browse = tk.Button(self.master, width=16, height=2, text='Browse...')
    self.btn_browse.grid(row=2, column=1, padx=(10,10), pady=(0,0), sticky=W)

    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program', command=lambda: check_files_func.ask_quit(self))
    self.btn_close.grid(row=5, column=1, columnspan=1, padx=(15,0), pady=(45,10), sticky=E)


if __name__ == "__main__":
    pass
