import time
import pyautogui as pg
import sys


pg.moveTo(1839, 125)
i = 0


while i < 1:
    pg.moveTo(1839, 125)
    pg.mouseDown(); pg.mouseUp()
    pg.moveTo(1802, 186)
    pg.mouseDown(); pg.mouseUp()
    pg.press('y')

    input('Press ENTER to exit')
