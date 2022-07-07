import pyautogui
from time import sleep
from webbrowser import open

open('https://web.whatsapp.com/')
sleep(5)
pyautogui.click(205, 298)
sleep(1)
pyautogui.write('heheheHEHEHE')
sleep(1)
pyautogui.press('Enter')