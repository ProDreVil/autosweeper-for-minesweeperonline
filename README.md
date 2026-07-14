# Autosweeper For Minesweeper.Online

A personalized minesweeper solver for Minesweeper.online.

This program uses a model based agent that scans the entire board through screenshots and converts it into a matrix representation.

***Disclaimer:** This solver is made for a school project. When testing, I recommend using a different account. This is still not the final full version. All the features with strikethrough are for the future improvements.*

---

## Features:
- Automated minesweeper solver
- Automated brower + MSO game starter
- Pixel-based tile recognition
- Internal board matrix representation
- Automatic safe tile clicking
- Automatic mine flagging
- Supported difficulties:
  - Beginner
  - Intermediate
  - Expert
- Controlled number of game loops
- Automatic board rescanning after every move
- ~~Pattern Recognition~~
- ~~Realistic mouse movement~~
- ~~Game Log~~

---

## Installation:

### > Prerequisites

The program is made with Python and primarily uses the library `pyautogui`. In order to work, you will need Python 3.10 or higher as they are the versions `pyautogui` is supported.

#### For Python:

1. Go to the official Python website:

   https://www.python.org/downloads/

2. Download the latest Python 3 installer for your operating system.

3. Run the installer.

4. Enable the option:
```
Add Python.exe to PATH
```

5. Click **Install Now**.

6. Verify the installation:
```bash
python --version
```

A Python version should be displayed. That means you already installed it. After that, open Command Prompt or PowerShell then proceed.

#### For PyAutoGUI:

1. Install PyAutoGUI using pip:
```bash
pip install pyautogui
```

2. Verify the installation:
```bash
pip show pyautogui
```

PyAutoGUI should appear with its installed version. Take note that the installation might take a while.


***Additional:** Make sure you have a Minesweeper Online bookmark and name it to "Mine". If you don't plan on adding one, turn the `Skip` variable False instead.*


### > Cloning

Proceed to cloning the repository.

``` bash
cd {ANY FOLDER YOU WANT}
git clone https://github.com/ProDreVil/autosweeper-for-minesweeperonline.git
code .
```

***Note:** Only use `code .` if you have VSCode. If not, proceed to open manually in the File Explorer.*

---

## Operation:

I have nothing much to say here since this project involves automation. One run and the program will do the work needed. Though, it's still worth reading the comments I left in the code.

Inside the code, you can see the variables:
``` python
skip = False
diff = "beginner"
loops = 3
```

The `skip` variable lets you skip the browser + minesweeper tab opening. Set it to True if you already have a Minesweeper.online tab opened.
The `diff` variable is the difficulty of the board. As of now, it supports "beginner", "intermediate", and "expert" (Note that all are in lowercase).
The `loops` variable is responsible for the amount of games to perform.

The way this whole program works is:

> ```
> Takes a screenshot of the board --> Analyze each cropped tile based on pixel color --> Convert them into a value in the matrix --> Stores all possible moves --> Executes all moves --> Repeat
> ```
