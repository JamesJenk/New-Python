#!/bin/python3

import datetime as dt
from time import sleep

desired_time = dt.datetime(2023, 1, 22, 16, 47)

while True:
    time = dt.datetime.now()
    now = time.strftime("%H:%M:%S")

    if now == desired_time:
        print("It is currently" + desired_time)

        break

    
    print(now)
