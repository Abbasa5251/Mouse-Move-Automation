from ctypes import pythonapi
import pyautogui
from random import randint, uniform
from time import sleep

width, height = pyautogui.size()
print(f"Width: {width} Height: {height}")

while True:
    rand_width, rand_height = randint(0, width), randint(0, height)
    print(f"RandomWidth: {rand_width} RandomHeight: {rand_height}")
    duration = round(uniform(0.50, 2.49), 2)
    pyautogui.moveTo(rand_width, rand_height, duration=duration)
    sleep(5)
