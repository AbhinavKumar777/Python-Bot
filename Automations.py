from os import startfile
from pyautogui import click
from pyautogui import hotkey
from keyboard import write
from keyboard import press 
from time import sleep

WhatsappPath = "C:\\Users\\DCGLocalAdmin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"


def WhatsappMsg(name,meassage):
    startfile(WhatsappPath)
    sleep(10)
    click(x=268, y=173)
    sleep(1.0)
    
    # Clears any name or previous search result
    hotkey('ctrl','backspace')
    click(x=268, y=173)
    
    write(name)
    sleep(2)
    click(x=254, y=379)
    sleep(1)
    click(x=1349, y=968)
    sleep(0.7)
    write(meassage)
    # sleep(1.0)
    # click(x=1865, y=963)
    press('enter')

def WhatsappCall(name):
    startfile(WhatsappPath)
    sleep(9)
    click(x=268, y=173)
    
    sleep(1.0)
    #Clears any name or previous search result
    hotkey('ctrl','backspace')
    click(x=268, y=173)
    
    write(name)
    sleep(2)
    click(x=254, y=379)
    sleep(1)
    click(x=1690, y=80)

def WhatsappChat(name):
    startfile(WhatsappPath)
    sleep(10)
    click(x=268, y=173)
    sleep(1.0)
    
    #Clears any name or previous search result
    hotkey('ctrl','backspace')
    click(x=268, y=173)
    
    write(name)
    sleep(2)
    click(x=254, y=379)
    sleep(1)
    click(x=1349, y=968)
