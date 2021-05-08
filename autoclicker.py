#first kinda successful project just a auto clicker not much 
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con




#random number generator to avoid detection
#specific range
min = 0.03
max = 0.06
#generate a random floating point number
b = min + (max-min)*random.random()

c = min + (max-min)*random.random()

d = min + (max-min)*random.random()

print(b,c,d)



     
        


#use this to change the key https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
key = 0x06 #the key u hold to auto click
print("Loading please wait")
time.sleep(1)
print("Caimins Autoclicker loaded enjoy")
time.sleep(0.5)
print("Press CTRL+C to end the program")


#defines what a click is
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.00000001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(b)#delay between clicks 


def click2(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.00000005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(c)#delay between clicks


def click3(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.00000003)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(c)#delay between clicks

#the clicker
while True:
    a = win32api.GetKeyState(key)
    if a < 0:
     click(960,540)#position of the click 
     time.sleep(0.00000001)
     click2(960,540)#position of the second click
     time.sleep(0.00000001)
     click3(960,540)#position of the third click
     time.sleep(0.00000001)


     


    
     