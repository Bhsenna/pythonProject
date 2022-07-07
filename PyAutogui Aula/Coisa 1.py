import pyautogui
from time import sleep

# prints mouse's coordinates
# while True:
#     print(pyautogui.position())
#     sleep(2)

# moves the mouse to the coordinates
# (x, y, time)
# pyautogui.moveTo(100, 100)

# adds the value to the mouse's coordinates
# (x, y, time)
# pyautogui.moveRel(100, 100, 2)


# makes the mouse left-click
# pyautogui.click()
# pyautogui.leftClick()
# makes the mouse right-click
# pyautogui.rightClick()
# makes the mouse double-click and triple-click
# pyautogui.doubleClick()
# pyautogui.tripleClick()
# you can put the coordinates inside the click() so it clicks in that position


# presses all selected keys at the same time
# pyautogui.hotkey('ctrl', 'shift', 'esc')
# pyautogui.hotkey('win', 'r')

# keeps the key pressed
# pyautogui.keyDown('win')
# pyautogui.keyDown('r')
# stops pressing the key
# pyautogui.keyUp('win')
# pyautogui.keyUp('r')


# presses then immediately releases
# pyautogui.press('win')


# writes something.
# interval=   makes it write slow
# pyautogui.write('calculadora', interval=0.1)
# pyautogui.press('Enter')


# drags the mouse to the position
# pyautogui.dragTo(1000, 800)
# drags mouse to that
# pyautogui.dragRel(220, 220, duration=0.2)


# creates a pop-up window
# pyautogui.alert(text='Hazime', title='Janela', button='Yeah Yeah')

# creates a pop=up window that accepts input
# a = pyautogui.prompt(text='Hazime', title='Janle', default='Senha')
# print(a)

# same as pyautogui.prompt but you can set up a mask (hides what you tipe)
# pyautogui.password(text='Hazime', title='Coisa', mask='*')

# same as pyautogui.alert but it accepts multiple buttons
# pyautogui.confirm(text='Hazime', title='Janela', buttons=('a', 'cancel', 'uwu'))


pyautogui.press('win')
pyautogui.write('calculadora', interval=0.1)
pyautogui.press('Enter')
sleep(3)
pyautogui.click('sete.png')