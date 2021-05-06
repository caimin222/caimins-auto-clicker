#first kinda successful project just a auto clicker not much 
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#use this to change the key https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
key = 0x06 #the key u hold to auto click

time.sleep(1)
print("Caimins Autoclicker loaded enjoy")
time.sleep(0.5)
print("press CTRL+C to end the program")


#defines what a click is
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.00000001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.060)#delay between clicks 


def click2(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.00000005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.035)#delay between clicks


def click3(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.00000003)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.045)#delay between clicks

#the clicker
while True:
    a = win32api.GetKeyState(key)
    if a < 0:
     click(960,540)#position of the click 
     click2(960,540)#position of the second click
     click3(960,540)#position of the third click