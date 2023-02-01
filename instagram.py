#!/bin/python3

import datetime as dt
from time import sleep
import pyautogui 
from subprocess import Popen

print('Inputs in chronological order: hour to send, minute to send, username, and message, any mistakes you will have to cancel and restart programme.')
print('For programme to execute at midnight, minute and hour should be set to 0')

# Getting time and contents of message 

print('Enter hour to send message:')
sleep(0.5)
hours = int(input())

print('Enter minute to send message:')
minutes = int(input())

print('Enter specify username to message:')
username = input()

print('What is your message?')
messages = input()

# If it is for midnight then the message will send when the day changes

if hours == 0:
        date = dt.datetime.now()
        day = date.strftime('%d')

# print date that the command has been issued

issue = dt.datetime.now().strftime('%Y:%m:%d:%H:%M:%S')

sleep(1)

print('Command issued @', issue)

# creating a datetime filled with crap minus the hour and minute which will be stripped allowing datetime to be happy and we take what we want

desired_time = dt.datetime(year=2021, month=2, day=2, hour=hours, minute=minutes, second=2)
desired_time = desired_time.strftime('%H:%M')

print('Desired time is: ', desired_time)

# for loop checking time, then if statement executes command

# creating print check requirement (pcr)

pcr = dt.datetime(year=2021, month=2, day=2, hour=hours, minute=30, second=2)
pcr = pcr.strftime('%M')

while True:
    time = dt.datetime.now()
    now = time.strftime("%H:%M")
    days = time.strftime('%d')
    print_check = time.strftime('%M')

    current = time.strftime('%Y:%m:%d:%H:%M:%S')

# try not to burn cpu so ping every 30 seconds

    sleep(30)

# print specs every 30 mins

    if print_check == pcr:
        print('Current time is: ', current, 'Time specefied is: ', desired_time)


# If not midnight then proceed normally, if midnight then will execute

    if hours != 0:
                if now >= desired_time:

        # prints time

                        Popen('firefox https://www.instagram.com/direct/inbox/', shell=True)

                        sleep(5)

        # goes to the search for person tab

                        for i in range(0,12):
                                sleep(0.5)
                                pyautogui.press('tab')

        # enters and selects name

                        sleep(1)
                        pyautogui.press('enter')
                        sleep(1)
                        pyautogui.write(username, interval=0.25)
                        sleep(1)
                        pyautogui.press('tab')
                        sleep(1)
                        pyautogui.press('enter')
                        sleep(1)

        # skips through other options and finishes

                        for i in range(0,25):
                                sleep(0.3)
                                pyautogui.press('tab')


                        pyautogui.press('enter')

                        sleep(2)

                        # message is written and then sent

                        pyautogui.write(messages, interval=0.25)

                        pyautogui.press('enter')


                        
                        break

    else:

        if day != days:

                        Popen('firefox https://www.instagram.com/direct/inbox/', shell=True)

                        sleep(5)

        # goes to the search for person tab

                        for i in range(0,12):
                                sleep(0.5)
                                pyautogui.press('tab')

        # enters and selects name

                        sleep(1)
                        pyautogui.press('enter')
                        sleep(1)
                        pyautogui.write(username, interval=0.25)
                        sleep(1)
                        pyautogui.press('tab')
                        sleep(1)
                        pyautogui.press('enter')
                        sleep(1)

        # skips through other options and finishes

                        for i in range(0,25):
                                sleep(0.3)
                                pyautogui.press('tab')


                        pyautogui.press('enter')

                        sleep(2)

                        # message is written and then sent

                        pyautogui.write(messages, interval=0.25)

                        pyautogui.press('enter')

                        break

sleep(1)

Popen('shutdown', shell=True)
