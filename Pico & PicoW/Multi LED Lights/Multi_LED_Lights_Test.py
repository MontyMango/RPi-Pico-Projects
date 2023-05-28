import machine
import utime
import random

# Safe to edit variables

# Seconds on / off
time_on = 2			# Time (in seconds) for the LED lights to be left on until the next action.
time_off = 1		# Time (in seconds) for the LED lights to be left off until the next action.
time_til_nxt_light = 1 # Time (in seconds), this is used for waiting for the next LED 
                       # to either turn on or off in all_on and all_off.  


# LED power pin locations (Consult your device documentation for GP location before editing location)
# Reminder: The resistor cannot resist the long end, also ground the short end.
led_1_GP = 0
led_2_GP = 1
led_3_GP = 2
# led_#_GP = # (Extra LEDs can be added after this like this)

# ------------------------------ #
# Code is below, have fun learning!

# Wiring locations (if you want to add more LEDs, you can add them here and in the array)
LED_1 = machine.Pin(led_1_GP, machine.Pin.OUT)  # define 1st led
LED_2 = machine.Pin(led_2_GP, machine.Pin.OUT)  # define 2nd led
LED_3 = machine.Pin(led_3_GP, machine.Pin.OUT)  # define 3rd led
# led_# = machine.Pin(led_#_GP, machine.Pin.OUT) # Extra LED

LED_ARRAY = [LED_1, LED_2, LED_3]


# Turns all LEDs on
# FORCE = If you want to turn every LED off without waiting
def all_on(FORCE):
    for i in LED_ARRAY:
        i.value(1)
        if(not FORCE):
            utime.sleep(time_til_nxt_light)
    utime.sleep(time_on)
    
# Turns all LEDs off
# FORCE = If you want to turn every LED off without waiting
def all_off(FORCE):
    for i in LED_ARRAY:
        i.value(0)
        if(not FORCE):
            utime.sleep(time_til_nxt_light)
    utime.sleep(time_off)
    

# Turns only the 1st LED on
def only_1st_led():
    LED_1.value(1)
    LED_2.value(0)
    LED_3.value(0)
    utime.sleep(time_on)


# Turns only the 2nd LED on
def only_2nd_led():
    LED_1.value(0)
    LED_2.value(1)
    LED_3.value(0)
    utime.sleep(time_on)


# Turns only the 3rd LED on
def only_3rd_led():
    LED_1.value(0)
    LED_2.value(0)
    LED_3.value(1)
    utime.sleep(time_on)


# Turns on a random LED in the array.
def turn_random_led_on():
    random.choice(LED_ARRAY).value(1)
    utime.sleep(time_on)


# Turns off a random LED in the array
def turn_random_led_off():
    random.choice(LED_ARRAY).value(0)
    utime.sleep(time_off)





while __name__ == '__main__':
    while True:
        all_on(False)
        all_off(True)

        only_1st_led()
        all_off(True)

        only_2nd_led()
        all_off(True)

        only_3rd_led()
        all_off(True)
