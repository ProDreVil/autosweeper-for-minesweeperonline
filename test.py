# rows = 5
# cols = 5

# board = [['?' for x in range(cols)] for y in range(rows)]

# print('\n'.join(' '.join(map(str, row)) for row in board))

import time

import pyautogui


# while True:
#     # print(pyautogui.position())
#     # pyautogui.moveTo(623, 581)
#     # time.sleep(1)

for i in range(10):
    x, y = pyautogui.position()
    color = pyautogui.pixel(x, y)
    print(f"({x}, {y}) -> {color}")
    time.sleep(0.5)

# x = 400 y = 355

# def clickCenter(rows, cols):
#     return rows // 2, cols // 2

# def clickRandom(board):
#     hidden = []
#     for r in range(len(board)):
#         for c in range(len(board[0])):
#             if board[r][c] == '?':
#                 hidden.append((r, c))
#     return random.choice(hidden) if hidden else None


# clickCenter(rows, cols)

# for _ in range(loops):
#     clickTile(rows, cols)