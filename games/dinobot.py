import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(330, 470):
        for j in range(900, 1080):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(330, 470):
        for j in range(1105, 1250):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    time.sleep(2)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

