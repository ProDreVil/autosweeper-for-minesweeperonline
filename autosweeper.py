# TODO: Automated Minesweeper Online Solver
# Pattern Recognition
# Statistics Saving

import pyautogui, time

rows = 5 # Test and
cols = 5 # Placeholder
tile_size = 28
board = [['?' for x in range(cols)] for y in range(rows)]
pixels = {
        (56, 64, 72): "0",
        (124, 199, 255): "1",
        (102, 194, 102): "2",
        (255, 119, 136): "3",
        (238, 136, 255): "4",
        (221, 170, 34): "5",
        (102, 204, 204): "6",
        (153, 153, 153): "7",
        (208, 216, 224): "8",
        (216, 224, 232): "F",
        (76, 84, 92): "?",
        # (255, 0, 0): "X"
    }

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

def closeAd():
    try:
        close = pyautogui.locateCenterOnScreen('resources/close.png', confidence = 0.8)
        if close:
            pyautogui.click(close)
    except pyautogui.ImageNotFoundException:
        print("No ad to close yay!")

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
    for r in range(rows):
        for c in range(cols):
            left = c * tile_size
            top = r * tile_size
            tile = boardSS.crop((left, top, left + tile_size - 1, top + tile_size - 1))
            if r == 0 and c == 0:
                tile.save(f"tile_{r}_{c}.png")
            board[r][c] = identifyTile(tile)
    return board

def identifyTile(tile):
    color = tile.getpixel((16, 20))
    # print(f"Tile color: {color}")
    return pixels.get(color, "X")

def getAdjacentTiles(board, row, col):
    adjacent = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                adjacent.append((nr, nc))
    return adjacent

def logic(board):
    safeMoves = set()
    flagMoves = set()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in "12345678":
                number = int(board[r][c])
                adjacent = getAdjacentTiles(board, r, c)
                flagged = 0
                unknown = []
                for nr, nc in adjacent:
                    if board[nr][nc] == "F":
                        flagged += 1
                    elif board[nr][nc] == "?":
                        unknown.append((nr, nc))
                # print(f"Tile ({r},{c}) = {number}")
                # print(f"Flags: {flagged}")
                # print(f"Unknown: {unknown}")
                # print()
                if flagged == number and unknown:
                    for nr, nc in unknown:
                        safeMoves.add((nr, nc))
                elif flagged + len(unknown) == number and unknown:
                    for nr, nc in unknown:
                        board[nr][nc] = "F"
                        flagMoves.add((nr, nc))
    print(f"Safe moves: {safeMoves}, Flag moves: {flagMoves}")
    for r, c in flagMoves:
        flagTile(r, c)
        # zzz()
    for r, c in safeMoves:
        clickTile(r, c)
        # zzz()
    return len(safeMoves)

def guess(board):
    rows = len(board)
    cols = len(board[0])
    corners = [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]
    for r, c in corners:
        if board[r][c] == "?":
            clickTile(r, c)
            return True
    return False

def clickTile(row, col):
    x, y = tilePosition(row, col)
    pyautogui.click(x, y)

def flagTile(row, col):
    x, y = tilePosition(row, col)
    pyautogui.rightClick(x, y)

def show(board):
    print('\n')
    print('\n'.join(' '.join(map(str, row)) for row in board))

def won(board):
    return not any('?' in row for row in board)

def lost(board):
    return any('X' in row for row in board)

zzz()

skip = True # skip opening sequence? (True / False)
diff = "beginner" # u can change the difficulty here lol (beginner, intermediate, expert)
loops = 3 # how many games to play?

openBrowser(skip)
if not skip:
    openMinesweeper()
    difficulty(diff)
    zzz()

zzz()
while loops > 0:
    loops -= 1
    rows, cols, board = createBoard(diff)
    closeAd()
    origin = start()
    zzz()
    while True:
        scanBoard(board, origin, tile_size)
        # show(board)
        # zzz()
        if won(board) or lost(board):
            if won(board):
                print("Game won!")
            else:
                print("Game lost!")
            pyautogui.press('space')
            zzz()
            break
        moves = logic(board)
        if moves == 0:
            print("No safe moves found, making a guess...") # Temp
            if not guess(board):
                print("Failed to make a guess.")
                break
        show(board)

print("This is the end")