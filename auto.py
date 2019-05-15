#!/usr/bin/env python3

import time
import pyautogui as ui

ui.FAILSAFE = True


def main():
    w, h = ui.size()
    print("Screen:", w, h)

    while True:
        time.sleep(0.001)

        x, y = ui.position()

        print(x, y)

        ui.moveRel(10, 0)


if __name__ == "__main__":
    main()
