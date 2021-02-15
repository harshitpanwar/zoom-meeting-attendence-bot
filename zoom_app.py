import pyautogui
import time

a = input("enter your meeting id")
b = input('enter your password')
c = input("enter message to type in message box")

a = " "+a
time.sleep(2)

pyautogui.click(pyautogui.locateCenterOnScreen('join.png'))

print('meeting id located')
pyautogui.write(a, interval=0.25)

time.sleep(1)

pyautogui.click(pyautogui.locateCenterOnScreen('audio.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('video.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('joinbutton.png'))
time.sleep(5)

pyautogui.write(b, interval=0.25)
pyautogui.click(pyautogui.locateCenterOnScreen('finaljoin.png'))

time.sleep(25)

pyautogui.hotkey('alt', 'f4')
pyautogui.press('enter')
pyautogui.hotkey('alt', 'f4')
pyautogui.hotkey('alt', 'space')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=950, y=1020)

pyautogui.write(c)
pyautogui.press('enter')