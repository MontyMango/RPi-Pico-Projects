import machine
import utime

# Safe to edit variables

# Seconds on / off
time_on = 3
time_off = 1

# LED pin locations (Consult your device documentation for GP location before editing location)
# Reminder: The resistor cannot resist the long end, also ground the short end.
led_1_GP = 0
led_2_GP = 1
led_3_GP = 2

# ------------------------------ #
# Code is below, have fun learning!

# Wiring locations 
led_1 = machine.Pin(led_1_GP, machine.Pin.OUT) # define 1st led
led_2 = machine.Pin(led_2_GP, machine.Pin.OUT) # define 2nd led
led_3 = machine.Pin(led_3_GP, machine.Pin.OUT) # define 3rd led

# Turns all LED's on
def all_on():
    led_1.value(1)
    led_2.value(1)
    led_3.value(1)
    utime.sleep(time_on)

# Turns only the 1st LED on
def only_1st_led():
    led_1.value(1)
    led_2.value(0)
    led_3.value(0)
    utime.sleep(time_on)

# Turns only the 2nd LED on
def only_2nd_led():
    led_1.value(0)
    led_2.value(1)
    led_3.value(0)
    utime.sleep(time_on)

# Turns only the 3rd LED on
def only_3rd_led():
    led_1.value(0)
    led_2.value(0)
    led_3.value(1)
    utime.sleep(time_on)

# Turns them all off
def all_off():
    led_1.value(0)
    led_2.value(0)
    led_3.value(0)
    utime.sleep(time_off)
    

while __name__ == '__main__':
    while True:
        all_on()
        all_off()
        
        only_1st_led()
        all_off()
        
        only_2nd_led()
        all_off()
        
        only_3rd_led()
        all_off()