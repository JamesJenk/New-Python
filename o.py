#!/bin/python3

import datetime as dt
from time import sleep

while True:

    time = dt.datetime.now()
    time = time.strftime('%H:%M:%S')

    print(time)

    sleep(0.5)