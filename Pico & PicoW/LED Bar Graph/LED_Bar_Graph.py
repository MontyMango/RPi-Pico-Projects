import machine
import utime

# Safe to edit variables

# How many seconds should the computer wait before doing the next action?
# Suggestions: Shorter time = (.5) | Longer time = (1) 
wait_time = .5

# LED Variables
# Consult your device documentation for GP location before editing location (ex: GP0 = 0 (Pin 1) )
LED1_GP = 0
LED2_GP = 1
LED3_GP = 2
LED4_GP = 3
LED5_GP = 4
LED6_GP = 5
LED7_GP = 6
LED8_GP = 8
LED9_GP = 13
LED10_GP = 15

# ------------------------------ #
# Code is below, have fun learning!

# Wiring locations
BARLED1 = machine.Pin(LED1_GP, machine.Pin.OUT)  # defines the 1st bar led
BARLED2 = machine.Pin(LED2_GP, machine.Pin.OUT)  # defines the 2nd bar led
BARLED3 = machine.Pin(LED3_GP, machine.Pin.OUT)  # defines the 3rd bar led
BARLED4 = machine.Pin(LED4_GP, machine.Pin.OUT)  # defines the 4th bar led
BARLED5 = machine.Pin(LED5_GP, machine.Pin.OUT)  # defines the 5th bar led
BARLED6 = machine.Pin(LED6_GP, machine.Pin.OUT)  # defines the 6th bar led
BARLED7 = machine.Pin(LED7_GP, machine.Pin.OUT)  # defines the 7th bar led
BARLED8 = machine.Pin(LED8_GP, machine.Pin.OUT)  # defines the 8th bar led
BARLED9 = machine.Pin(LED9_GP, machine.Pin.OUT)  # defines the 9th bar led
BARLED10 = machine.Pin(LED10_GP, machine.Pin.OUT)  # defines the 10th bar led

# List for each led bar
BarGraph = [BARLED1, BARLED2, BARLED3, BARLED4, BARLED5, BARLED6, BARLED7, BARLED8, BARLED9, BARLED10]
SIZE = len(BarGraph)


# Functions for mainloop()

# Turns LEDs on or off from the left side (LightValue: 1 = Off, 0 = On)
def fromleft(LightValue):
    for LEDBAR in BarGraph:
        LEDBAR.value(LightValue)
        outputLight(LEDBAR, LightValue)
        utime.sleep(wait_time)


# Turns LEDs on or off from the right side (LightValue: 1 = Off, 0 = On)
def fromright(LightValue):
    for LEDBARNUM in range(0, SIZE):
        LEDBAR = BarGraph[SIZE - LEDBARNUM]
        LEDBAR.value(LightValue)
        outputLight(LEDBAR, LightValue)
        utime.sleep(wait_time)


# Used to show if the light is on or off.
def outputLight(LED, value):
    # 1 = Off, 0 = On
    if value == 1: onoroff = "Off:"
    else: onoroff = "On:"
    print(onoroff, LED)


# Turns all LEDs off
def alloff():
    for LEDBAR in BarGraph:
        LEDBAR.value(1)


# Turns all LEDs on
def allon():
    for LEDBAR in BarGraph:
        LEDBAR.value(0)


# Special functions
def exiting():
    alloff()


while __name__ == '__main__':
    # Makes sure that everything is off before starting.
    alloff()

    while True:
        fromright(0)
        fromleft(1)

        utime.sleep(wait_time)
        allon()
        utime.sleep(wait_time)
        alloff()
        utime.sleep(wait_time)
