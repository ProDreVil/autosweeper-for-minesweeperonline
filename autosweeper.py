# TODO: Automated Minesweeper
# Color/Number Detection
# 3 Modes: Flagging, Revealing, Chording
# Corners, 1 2 3, 121 Combo
# Statistics Saving

import pyautogui, time

rows = 5
cols = 5
tile_size = 28
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

def start():
    while True:
        try:
            tlc = pyautogui.locateCenterOnScreen('resources/start.png', confidence = 0.8)
            if tlc:
                pyautogui.click(tlc)
                return pyautogui.Point(int(tlc.x), int(tlc.y))
        except pyautogui.ImageNotFoundException:
            print("Start button not found...")
            zzz()

def tilePosition(row, col):
    return origin.x - 2 + col * tile_size, origin.y - 2 + row * tile_size

def scanBoard(board, origin, tile_size):
    rows = len(board)
    cols = len(board[0])
    zzz()
    boardSS = pyautogui.screenshot(region=(int(origin.x) - 1, int(origin.y) - 1, int(cols * tile_size), int(rows * tile_size)))
    # safeCheck(boardSS, tile_size)
    for r in range(rows):
        for c in range(cols):
            # cx = c * tile_size + tile_size // 2 # - 2
            # cy = r * tile_size + tile_size // 2 # - 2
            # sample = boardSS.crop((cx - 3, cy - 3, cx + 3, cy + 3))
            left = c * tile_size
            top = r * tile_size
            tile = boardSS.crop((left, top, left + tile_size - 1, top + tile_size - 1))
            if r == 0 and c == 0:
                tile.save(f"tile_{r}_{c}.png")
            # pyautogui.moveTo(int(origin.x) + cx - 2, int(origin.y) + cy - 2, duration = 0.2)
            # colors = tile.getcolors()
            # print(f"({r}, {c}) -> {colors}")
            # color = boardSS.getpixel((cx, cy))
            # pyautogui.moveTo(int(origin.x) + cx, int(origin.y) + cy, duration=0.2)
            # print(f"({r}, {c}) -> {color}")
            # zzz()
    return board

def identifyTile(tile):
    pass

def safeCheck(boardSS, tile_size):
    for c in range(3):
        left = c * tile_size
        top = 0
        tile = boardSS.crop((left, top, left + tile_size - 1, top + tile_size - 1))
        tile.save(f"tile_{c}.png")

def clickTile(row, col):
    x, y = tilePosition(row, col)
    pyautogui.click(x, y)

def show(board):
    print('\n'.join(' '.join(map(str, row)) for row in board))


zzz()

skip = True # skip opening sequence? (True / False)
diff = "beginner" # u can change the difficulty here lol (beginner, intermediate, expert)
loops = 1 # how many games to play?

openBrowser(skip)
rows, cols, board = createBoard(diff)
if not skip:
    openMinesweeper()
    difficulty(diff)
    zzz()

zzz()
while loops > 0:
    loops -= 1
    origin = start()
    zzz()
    scanBoard(board, origin, tile_size)
    # supposed loop starts here
    # clickTile(0, 0)
    zzz()
    show(board)

print("This is the end")