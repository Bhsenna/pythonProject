import pyautogui
from time import sleep

cont = pyautogui.prompt(text='Digite uma Operação', title='Continha')

pyautogui.press('win')
pyautogui.write('calculadora')
pyautogui.press('Enter')
sleep(1)
pyautogui.write(cont + '=')