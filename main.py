from pynput import mouse
from pynput.mouse import Button, Controller

mouse = Controller()

def on_scroll(x, y, dx, dy):
    if dy < 0:
        mouse.click(Button.left, 1)
        mouse.click(Button.right, 1)

listener = mouse.Listener(
    on_scroll=on_scroll)
listener.start()