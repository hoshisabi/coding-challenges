#!/bin/python3

import os
from datetime import datetime, timedelta

# Fri 01 May 2015 13:54:36 -0000
time_format = "%a %d %b %Y %H:%M:%S %z"


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1time = datetime.strptime(t1, time_format)
    t2time = datetime.strptime(t2, time_format)
    s = abs((t1time - t2time).total_seconds())
    return int(s)

# def time_delta(t1, t2):
#     time_format =
#
#     t1 = datetime.strptime(t1, time_format)
#     t2 = datetime.strptime(t2, time_format)
#
#     return str(int(abs((t1-t2).total_seconds())))


print(time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"))
print(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))
