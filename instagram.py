#!/bin/python3

import datetime as dt
from time import sleep
import pyautogui 
from subprocess import Popen

print('Inputs in chronological order: hour to send, minute to send, username, and message, any mistakes you will have to cancel and restart programme.')

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

# creating a datetime filled with crap minus the hour and minute which will be stripped allowing datetime to be happy and we take what we want

desired_time = dt.datetime(year=2021, month=2, day=2, hour=hours, minute=minutes, second=2)
desired_time = desired_time.strftime('%H:%M')

# for loop checking time, then if statement executes command

while True:
    time = dt.datetime.now()
    now = time.strftime("%H:%M")

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


sleep(1)

pyautogui.hotkey('alt', 'tab')

sleep(1)

Popen('shutdown', shell=True)
