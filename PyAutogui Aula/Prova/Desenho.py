import pyautogui
from time import sleep

pyautogui.press('win')
pyautogui.write('mspaint')
pyautogui.press('Enter')
sleep(2)

pyautogui.click(672, 78)

x, y = 763, 230
pyautogui.moveTo(x, y)
pyautogui.dragRel(50, 50)
x -= 25
y += 50
pyautogui.moveTo(x, y)
pyautogui.dragRel(100, 100)
x -= 50
y += 100
pyautogui.moveTo(x, y)
pyautogui.dragRel(200, 200)