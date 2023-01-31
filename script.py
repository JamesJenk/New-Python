#!/bin/python3

import pyautogui 
from time import sleep
from subprocess import Popen

Popen('firefox https://www.instagram.com/direct/inbox/', shell=True)

username = 'summergeidlinger'
messages = 'test'

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