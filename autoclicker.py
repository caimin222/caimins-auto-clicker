#first kinda successful project just a auto clicker not much 
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#use this to change the key https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
key = 0x06 #the key u hold to auto click

#defines what a click is
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.075)#delay between clicks 

#the clicker
while True:
    a = win32api.GetKeyState(key)
    if a < 0:
     click(960,540)#position of the click 
     
	
