import machine
import utime

#/I named each LED according to color, and matched them with the corrent pin.
led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

#/While loop starts at top, and ends at bottom, never ending.
while True:
    
    #red led on for 5 secs, then off
    led_red.toggle()
    utime.sleep(5)
    led_red.value(0)
    
    #yellow led on for 2 secs, then off
    led_yellow.toggle()
    utime.sleep(2)
    led_yellow.value(0)
    
    #green led on for 5 secs, then off
    led_green.toggle()
    utime.sleep(5)
    led_green.value(0)
    
    #yellow led on for 2 secs, then off
    led_yellow.toggle()
    utime.sleep(2)
    led_yellow.value(0)
