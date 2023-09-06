from adafruit_circuitplayground import cp

cp.pixels.auto_write = False

while True:
    for i in range(10):
        cp.pixels[i] = (0, 255, 0)
    cp.pixels.show()
