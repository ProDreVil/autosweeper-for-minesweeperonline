# TODO: Automated Minesweeper
# Color/Number Detection
# 3 Modes: Flagging, Revealing, Chording
# Download Selenium
# Corners, 1 2 3, 121 Combo
# Statistics Saving

import pyautogui, time

def zzz():
    time.sleep(0.5)

def openBrowser():
    browser = pyautogui.locateCenterOnScreen('chrome.png', confidence = 0.8)
    if browser:
        pyautogui.click(browser)
        pyautogui.hotkey('ctrl', 't')
    else:
        print("Chrome icon not found")
    zzz()

def openMinesweeper():
    while True:
        try:
            mso = pyautogui.locateCenterOnScreen('minesweeperonline.png', confidence = 0.8)
            if mso:
                pyautogui.click(mso)
                zzz()
                break
        except pyautogui.ImageNotFoundException:
            print("Minesweeper Online icon not found")
            zzz()

def difficulty():
    diff = "beginner" # u can change the difficulty here lol (beginner, intermediate, expert)
    img = f"{diff}.png"
    pos = None
    while pos is None:
        try:
            pos = pyautogui.locateCenterOnScreen(img, confidence = 0.8)
            if pos:
                pyautogui.click(pos)
        except pyautogui.ImageNotFoundException:
            print(f"{diff} button not found")
            zzz()

zzz()
openBrowser()
openMinesweeper()
difficulty()

# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://roblox.com")

# pyautogui.PAUSE = 0.3

# for i in range(10):
#     print(pyautogui.position())
#     time.sleep(0.3)

#pyautogui.moveTo(100, 100)
#pyautogui.click()