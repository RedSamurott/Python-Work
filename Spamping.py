from pynput.keyboard import Key, Controller
import time

time.sleep(5)
keyboard = Controller()

                
for x in range(5400):
    keyboard.press(Key.ctrl)
    keyboard.press("v")
    keyboard.release(Key.ctrl)
    keyboard.release("v")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)