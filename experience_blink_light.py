import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False

while True:
    cp.pixels[1] = (50, 50, 50)
    cp.pixels.show()
    time.sleep(1)
    cp.pixels[1] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(1)
