#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.9.0
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Create a webpage generator. This will spin up a users
#                   web browser and display a simple webpage using provide
#                   html file.
#
#   Tested OS:      Written and tested with Windows 10.
import webbrowser as wb


hFile = open("index.html","w")

hFile.write("""
<html>
    <body>
        <h1>
            Stay tuned for our amazing summer sale!
        </h1>
    <body>
</html>
""")

hFile.close()


wb.open_new_tab("index.html")
