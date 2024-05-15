import pyautogui, time

time.sleep(4)

for i in range(100000):

    if i == 1:
        pyautogui.typewrite('hiiii beauty')
    else:
        pyautogui.typewrite("if she say it's over 😂")

    pyautogui.press('Enter')
