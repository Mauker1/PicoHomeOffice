from neopixel import Neopixel
from picozero import Pot
import machine
import math
import utime
import random

# Taken from https://stackoverflow.com/a/37697840/4070469
# Thanks to Erwin Mayer
def truncate(number, digits) -> float:
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

dial = Pot(0) # Connected to pin A0 (GP_26)
EMA_a = 0.6
EMA_S = dial.value

redBtn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
yelBtn = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
grnBtn = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
rstBtn = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

numpix = 12
strip = Neopixel(numpix, 0, 29, "GRB")

mode = {
  "red": 1,
  "yellow": 2,
  "green": 3,
  "white": 4
}

curMode = mode["red"]

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
white = (255, 255, 255)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet, white]

delay = 0.1
strip.brightness(42)
blank = (0,0,0)

color = colors_rgb[random.randint(0, len(colors_rgb)-1)]
strip.set_pixel(0, red)

i = 0
isRight = True
while True:
    #if (isRight):
    #    strip.rotate_right()
    #else:
    #    strip.rotate_left()
    
    #if (i >= 11):
    #    i = 0
    #    isRight = not isRight
    
    brightness = int(math.floor(255 * truncate(dial.value, 2)))
    strip.brightness(brightness)
    
    if (redBtn.value() == 0):
        print("RED!")
        strip.fill((0,0,0))
        utime.sleep(delay)
        curMode = mode["red"]
    if (yelBtn.value() == 0):
        print("YELLOW!")
        strip.fill((0,0,0))
        utime.sleep(delay)
        curMode = mode["yellow"]
    if (grnBtn.value() == 0):
        print("GREEN!")
        strip.fill((0,0,0))
        utime.sleep(delay)
        curMode = mode["green"]
    if (rstBtn.value() == 0):
        print("RESET!")
        strip.fill((0,0,0))
        utime.sleep(delay)
        curMode = mode["white"]
        
        
    if (curMode == mode["red"]):
        strip.set_pixel_line(0, 11, red, brightness)
    elif (curMode == mode["yellow"]):
        strip.set_pixel_line(0, 11, yellow, brightness)
    elif (curMode == mode["green"]):
        strip.set_pixel_line(0, 11, green, brightness)
    elif (curMode == mode["white"]):
        strip.set_pixel_line(0, 11, white, brightness)
    
    strip.show()
    utime.sleep(delay)
    #i = i + 1
    #strip.fill((0,0,0))

