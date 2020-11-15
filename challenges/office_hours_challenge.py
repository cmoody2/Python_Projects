#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.9.0
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Create a program to check if locations are open of a
#                   Portland-based company with branches in New York and
#                   London. Demonstrates Use of datetime and pytz packages.
#                   
#
#   Tested OS:      Written and tested with Windows 10.


from datetime import datetime, timedelta, time
from pytz import timezone

# Portland HQ time and hours
def Portlandtime():
    # first we format time to military format
    fmt = "%H%M"
    # now we get the current time in regards to specified time zone
    # this is considered an 'aware' time object
    now_time = datetime.now(timezone('US/Pacific'))
    # next we convert current time into an int using our
    # specified format
    now_hour = int(now_time.strftime(fmt))
    # then we check if given time fits with the
    # window of being open with an 'if' statment
    if now_hour >= 900 and now_hour <= 1700:
        print("HQ (Portland) is currently open")
    else:
        print("HQ (Portland) is currently closed")
    return now_hour


# New York time and hours
def Nytime():
    fmt = "%H%M"
    now_time = datetime.now(timezone('US/Eastern'))
    now_hour = int(now_time.strftime(fmt))
    if now_hour >= 900 and now_hour <= 1700:
        print("New York Branch is currently open")
    else:
        print("New York Branch is currently closed")
    return now_hour


# London time and hours
def Londontime():
    fmt = "%H%M"
    now_time = datetime.now(timezone('Europe/London'))
    now_hour = int(now_time.strftime(fmt))
    if now_hour >= 900 and now_hour <= 1700:
        print("London Branch is currently open")
    else:
        print("London is currently closed")
    return now_hour



if __name__ == "__main__":
    hq = Portlandtime()
    ny_office = Nytime()
    london_office = Londontime()

    
    
    












