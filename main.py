from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller
import threading
import time

keyboard = Controller()
toggle = False

def on_scroll(x, y, dx, dy):
    if dy < 0:
        keyboard.type("e")
        time.sleep(0.01)
        keyboard.type(";")

def setup(x, y, dx, dy):
    x = threading.Thread(target=on_scroll, args=(x, y, dx, dy), daemon=True)
    x.start()



with mouse.Listener(
        on_scroll=setup) as listener:
    listener.join()