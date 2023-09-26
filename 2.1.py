#/ this code turns the onboard pico led on and off via GP25
import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT) #output for pin 25 (gp25)
while True: #since no conditions, its always true
    led_onboard.value(1) #turn led on
    utime.sleep(.2) # for 2 seconds
    led_onboard.value(0) #turn led off
    utime.sleep(.2) # for 2 seconds
