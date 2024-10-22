
import machine
import time

leds = [machine.Pin(i, machine.Pin.OUT) for i in range(1, 5)]

while True:
   
    for led in leds:
        led.value(1)
        time.sleep(0.06)

    time.sleep(1)

  
    for led in leds:
        led.value(0)

    time.sleep(0.3)



