import pyautogui

# print(pyautogui.position())
#
# pyautogui.moveTo()
# pyautogui.click()
# # i = pyautogui.locateOnScreen('9.png')
# print(pyautogui.position())
# pyautogui.screenshot('1.png', region=(135, 819, 30, 30))

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('notepad', interval=0.1)
pyautogui.press('enter')
pyautogui.typewrite('Hello! It\'s auto typing system.', interval=0.1)
pyautogui.moveTo(1498, 472, 0.25)
pyautogui.click()
pyautogui.moveTo(977, 533, 0.25)
pyautogui.click()
