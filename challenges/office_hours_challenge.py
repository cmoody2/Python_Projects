from datetime import datetime, timedelta, time
from pytz import timezone


def Portlandtime():
    fmt = "%H:%M:%S %Z%z"
    now_time = datetime.now(timezone('US/Pacific'))
    return now_time.strftime(fmt)


def Nytime():
    fmt = "%H:%M:%S %Z%z"
    now_time = datetime.now(timezone('US/Eastern'))
    return now_time.strftime(fmt)



def Londontime():
    fmt = "%H:%M:%S %Z%z"
    now_time = datetime.now(timezone('Europe/London'))
    return now_time.strftime(fmt)






if __name__ == "__main__":
    ny_office = Nytime()
    london_office = Londontime()
    hq = Portlandtime()
    print(ny_office)
    print(london_office)
    print(hq)
    












