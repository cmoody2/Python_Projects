from datetime import datetime, timedelta, time
from pytz import timezone


def Portlandtime():
    fmt = "%H%M"
    now_time = datetime.now(timezone('US/Pacific'))
    now_hour = int(now_time.strftime(fmt))
    if now_hour >= 900 and now_hour <= 1700:
        print("HQ (Portland) is currently open")
    else:
        print("HQ (Portland) is currently closed")
    return now_hour


def Nytime():
    fmt = "%H%M"
    now_time = datetime.now(timezone('US/Eastern'))
    now_hour = int(now_time.strftime(fmt))
    if now_hour >= 900 and now_hour <= 1700:
        print("New York Branch is currently open")
    else:
        print("New York Branch is currently closed")
    return now_hour


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

    
    
    












