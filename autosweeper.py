# TODO: Automated Minesweeper
# Color/Number Detection
# 3 Modes: Flagging, Revealing, Chording
# Corners, 1 2 3, 121 Combo
# Statistics Saving
# Center + Randomized Initial Clicks

import pyautogui, time, random

rows = 5
cols = 5
board = [['?' for x in range(cols)] for y in range(rows)]

def zzz():
    time.sleep(0.5)

def openBrowser(skip):
    browser = pyautogui.locateCenterOnScreen('resources/chrome.png', confidence = 0.8)
    if browser:
        pyautogui.click(browser)
        if not skip:
            pyautogui.hotkey('ctrl', 't')
    else:
        print("Chrome icon not found...")
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
            print("Minesweeper Online icon not found...")
            zzz()

def createBoard(diff):
    sizes = {"beginner": (9, 9), "intermediate": (16, 16), "expert": (16, 30)}
    if diff not in sizes:
        raise ValueError(f"Invalid difficulty: {diff}. Choose from {list(sizes.keys())}.")
    rows, cols = sizes[diff]
    board = [['?' for _ in range(cols)] for _ in range(rows)]
    return rows, cols, board

def difficulty(diff):
    img = f"{diff}.png"
    while True:
        try:
            pos = pyautogui.locateCenterOnScreen(f"resources/{img}", confidence = 0.8)
            if pos:
                pyautogui.click(pos)
                break
        except pyautogui.ImageNotFoundException:
            print(f"{diff} button not found...")
            zzz()

def clickCenter(rows, cols):
    return rows // 2, cols // 2

def clickRandom(board):
    hidden = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '?':
                hidden.append((r, c))
    return random.choice(hidden) if hidden else None

def clickTile(rows, cols):
    pyautogui.click(clickCenter(rows, cols))

def show(board):
    print('\n'.join(' '.join(map(str, row)) for row in board))


zzz()

skip = False # skip opening sequence?
diff = "beginner" # u can change the difficulty here lol (beginner, intermediate, expert)
loops = 1 # how many games to play

openBrowser(skip)
rows, cols, board = createBoard(diff)
if not skip:
    openMinesweeper()
    difficulty(diff)
    zzz()

zzz()
# clickCenter(rows, cols)

# for _ in range(loops):
#     clickTile(rows, cols)

show(board)