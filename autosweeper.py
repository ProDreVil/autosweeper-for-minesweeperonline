# TODO: Automated Minesweeper
# Color/Number Detection
# 3 Modes: Flagging, Revealing, Chording
# Corners, 1 2 3, 121 Combo
# Statistics Saving
# Center + Randomized Initial Clicks

import pyautogui, time

rows = 5
cols = 5
board = [['?' for x in range(cols)] for y in range(rows)]

def zzz():
    time.sleep(0.5)

def openBrowser():
    browser = pyautogui.locateCenterOnScreen('resources/chrome.png', confidence = 0.8)
    if browser:
        pyautogui.click(browser)
        pyautogui.hotkey('ctrl', 't')
    else:
        print("Chrome icon not found")
    zzz()

def openMinesweeper():
    while True:
        try:
            mso = pyautogui.locateCenterOnScreen('resources/minesweeperonline.png', confidence = 0.8)
            if mso:
                pyautogui.click(mso)
                zzz()
                break
        except pyautogui.ImageNotFoundException:
            print("Minesweeper Online icon not found")
            zzz()

def difficulty():
    diff = "beginner" # u can change the difficulty here lol (beginner, intermediate, expert)
    sizes = {"beginner": (9, 9), "intermediate": (16, 16), "expert": (16, 30)}
    rows, cols = sizes[diff]
    board = [['?' for x in range(cols)] for y in range(rows)]
    img = f"{diff}.png"
    pos = None
    while pos is None:
        try:
            pos = pyautogui.locateCenterOnScreen(f"resources/{img}", confidence = 0.8)
            if pos:
                pyautogui.click(pos)
        except pyautogui.ImageNotFoundException:
            print(f"{diff} button not found")
            zzz()
    return rows, cols, board

def show(board):
    print('\n'.join(' '.join(map(str, row)) for row in board))

zzz()
openBrowser()
openMinesweeper()
zzz()
rows, cols, board = difficulty()
zzz()

show(board)