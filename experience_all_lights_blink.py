import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False

while True:
    for i in range(10):
        cp.pixels[i] = (50, 0, 0)
    cp.pixels.show()
    time.sleep(1)

    for i in range(10):
        cp.pixels[i] = (0, 50, 0)
    cp.pixels.show()
    time.sleep(1)

    for i in range(10):
        cp.pixels[i] = (0, 0, 50)
    cp.pixels.show()
    time.sleep(1)
