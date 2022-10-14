import pyautogui
import time

pyautogui.PAUSE = 0.2

time.sleep(3)

videoid = ['000', '001', '002']

# type url, 'enter', 'enter', 'command + l", repeat
for x in videoid:
    pyautogui.typewrite('INSERT URL' + x + '.ts')
    pyautogui.press('return')
    time.sleep(2)
    pyautogui.press('return')
    time.sleep(2)
    pyautogui.hotkey('command', 'l')
    if x== 'FINAL ITEM IN THE VIDEOID LIST':
        break