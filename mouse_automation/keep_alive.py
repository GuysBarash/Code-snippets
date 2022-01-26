import os
import mouse
import sys
import pyautogui
import time
from datetime import datetime
from tqdm import tqdm

STEP_SIZE = 200
TAB_SIZE = 220
LOOP_DELAY_IN_SEC = 60


def down(step=None):
    if step is None:
        step = STEP_SIZE
    mouse.move(0, step, absolute=False, duration=0.2)
    time.sleep(0.2)


def up(step=None):
    if step is None:
        step = STEP_SIZE
    mouse.move(0, -step, absolute=False, duration=0.2)
    time.sleep(0.2)


def left(step=None):
    if step is None:
        step = STEP_SIZE
    mouse.move(-step, 0, absolute=False, duration=0.2)
    time.sleep(0.2)


def right(step=None):
    if step is None:
        step = STEP_SIZE
    mouse.move(+step, 0, absolute=False, duration=0.2)
    time.sleep(0.2)


class KeepAlive:
    def __init__(self, tabs=3):
        self.tabs = tabs
        self.step = STEP_SIZE
        self.starting_position = None

    def ping(self):
        for i in range(self.tabs):
            self.handle_tab()
            right(self.step)

    def handle_tab(self):
        pyautogui.leftClick()
        time.sleep(0.1)
        down()
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(0.1)
        up()

    def sleep(self, sleep_time=1, msg='Sleeping...'):
        time.sleep(0.1)
        for i in tqdm(range(sleep_time), desc=msg):
            time.sleep(1)
        time.sleep(0.1)

    def loop(self):
        print("Place mouse at starting point.")
        self.sleep(10, 'Place mouse')
        x, y = pyautogui.position()
        print("Now move to the next tab")
        self.sleep(6, 'Move to the next tab')
        xt, yt = pyautogui.position()
        self.step = xt - x

        self.starting_position = [x, y]
        start_time = datetime.now()
        print(f"Starting position recorded. [{x} , {y}]")
        print(f"Step size: {self.step}")
        for ping_idx in range(99999999999999):
            pyautogui.moveTo(self.starting_position[0], self.starting_position[1])
            self.ping()
            current_time = datetime.now()
            print(f"[{ping_idx+1}]\tCurrent time: {current_time}\tRunning time: {current_time - start_time}")
            self.sleep(LOOP_DELAY_IN_SEC)

    def sniff(self):
        while True:
            time.sleep(0.3)
            x, y = pyautogui.position()
            print(f"position. [{x} , {y}]")


if __name__ == '__main__':
    keeper = KeepAlive(tabs=6)
    # keeper.sniff()
    keeper.loop()
