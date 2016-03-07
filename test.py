import sys
import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
try:
    while True:
        gpio.output(7, 1)
        time.sleep(1)
        gpio.output(7, 0)
        time.sleep(1)
        gpio.output(11, 1)
        time.sleep(1)
        gpio.output(11, 0)
        time.sleep(1)

        gpio.output(13, 1)
        time.sleep(1)
        gpio.output(13, 0)
        time.sleep(1)
        gpio.output(15, 1)
        time.sleep(1)
        gpio.output(15, 0)
        time.sleep(1)
except KeyboardInterrupt:
    gpio.cleanup()
    sys.exit()

