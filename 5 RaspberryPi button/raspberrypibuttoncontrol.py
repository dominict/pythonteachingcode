''' Use General Purpose Input/Output controller "GPIO" on the Raspberry Pi
to interface with hardware and respond to a button.'''
# import the GPIO library aliased as GPIO so we don't have to type RPi.GPIO each time
import RPi.GPIO as GPIO
import time
#set the GPIO library to Broadcom chip mode since our Pis have Broadcom chips
GPIO.setmode(GPIO.BCM)
#indicate which pins we will use in these variables
switch_pin = 23
led_pin = 7
#setup the LED pin as an out pin
GPIO.setup(led_pin,GPIO.OUT)
#setup the switch pin as a switch that is always on by default (thus IN)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        #since switch is always on by default, pressing button causes False
        if GPIO.input(switch_pin)== False:
            #print a message with the formatted current time (string format time method)
            print("Button Pressed at "+time.strftime("%Y/%m/%d - %H:%M:%S"))
            GPIO.output(led_pin,True) #turn on LED
            time.sleep(2) #wait 2 seconds
            GPIO.output(led_pin,False) #turn off LED
finally:
    print("cleaning up")
    GPIO.cleanup()
