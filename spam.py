import pyautogui, time, random
time.sleep(4)

for i in range(100000):
    x = random.randint(0, 1)

    pyautogui.typewrite(str(x))



