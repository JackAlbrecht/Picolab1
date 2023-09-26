#/the pico minicontroller runs power from the computer into the breadboard where it is then harnessed from the positive connection into the LED and then into the resistor into the pi and then back to the ground.
#/this code tells the led to turn on, off, on, off, on in different amounts of time.
import machine
import utime
led = machine.Pin(13, machine.Pin.OUT)
while True:
    led.toggle() #turns the led off/on
    utime.sleep(.01) # for 1 second
    led.value(0) #turns the led off
    utime.sleep(.01) # for .5 seconds
    led.value(1) #turns the led on
    utime.sleep(.01) # for 5 seconds
    led.value(0) #turns the led off
    utime.sleep(.01) # for .5 seconds
    led.value(1) #turns the led on
    utime.sleep(.01) # for 1 second
