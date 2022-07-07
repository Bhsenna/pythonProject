import pyautogui
from time import sleep

pyautogui.press('win')
pyautogui.write('mspaint')
pyautogui.press('Enter')
sleep(2)
k = 5
pyautogui.moveTo(500, 200)
for i in range(500, 0, -10):
    pyautogui.dragRel(i, 0)
    pyautogui.dragRel(0, i)
    pyautogui.dragRel((k-i), 0)
    pyautogui.dragRel(0, (k-i))