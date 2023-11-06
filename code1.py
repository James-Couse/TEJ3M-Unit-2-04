"""
Created by: James Couse
Created on: Oct 23 2023
This module cycles an RGB LED through all colours.
"""

import time
import board
import digitalio

led_red = digitalio.DigitalInOut(board.GP9)
led_green = digitalio.DigitalInOut(board.GP11)
led_blue = digitalio.DigitalInOut(board.GP13)

led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT
led_blue.direction = digitalio.Direction.OUTPUT

while True:
    # red
    led_red.value = True
    led_green.value = False
    led_blue.value = False
    time.sleep(1)

    # green
    led_red.value = False
    led_green.value = True
    led_blue.value = False
    time.sleep(1)

    # blue
    led_red.value = False
    led_green.value = False
    led_blue.value = True
    time.sleep(1)

    # red-green
    led_red.value = True
    led_green.value = True
    led_blue.value = False
    time.sleep(1)

    # green-blue
    led_red.value = False
    led_green.value = True
    led_blue.value = True
    time.sleep(1)

    # blue-red
    led_red.value = True
    led_green.value = False
    led_blue.value = True
    time.sleep(1)

    # White
    led_red.value = True
    led_green.value = True
    led_blue.value = True
    time.sleep(1)
    