import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = True

while True:
    for i in range(10):
        cp.pixels[i] = (i * 20, 0, 0)
        time.sleep(1)
