# convert str to seconds num sin 1st Jan 1970
from datetime import datetime


def sec(tms):
    dt = datetime.strptime(tms, "%Y-%m-%d %H:%M:%S")
    return (dt - datetime(1970, 1, 1)).total_seconds()