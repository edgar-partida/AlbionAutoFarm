import pyautogui, time, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        print(pyautogui.position())
        time.sleep(0.5)
        sys.stdout.flush()
finally:
    print("end")