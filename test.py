# rows = 5
# cols = 5

# board = [['?' for x in range(cols)] for y in range(rows)]

# print('\n'.join(' '.join(map(str, row)) for row in board))

import time

import pyautogui


while True:
    print(pyautogui.position())
    time.sleep(1)
# x = 400 y = 355