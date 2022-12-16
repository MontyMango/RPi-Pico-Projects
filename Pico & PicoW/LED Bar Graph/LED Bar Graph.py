import machine
import utime

# Safe to edit variables

# How many seconds should the computer wait before doing the next action?
# Suggestions: Shorter time = (.5) | Longer time = (1) 
wait_time = .1

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

# Functions for mainloop()

class LEDBar:
    def __init__(self):
        # Used for subtraction and addition
        self.right_end = 0
        self.left_end = 0

        self.BarGraph = [BARLED1, BARLED2, BARLED3, BARLED4, BARLED5, BARLED6, BARLED7, BARLED8, BARLED9, BARLED10]
        self.SIZE = len(self.BarGraph)

    # Turns LEDs on or off from the left side (LightValue: 1 = Off, 0 = On)
    def Fillfromleft(self, LightValue):
        for LEDBAR in self.BarGraph:
            LEDBAR.value(LightValue)
            self.outputLight(LEDBAR, LightValue)
            utime.sleep(wait_time)
        if LightValue == 1:
            self.resetSides()
        else:
            self.filledSides(False)

    # Turns LEDs on or off from the right side (LightValue: 1 = Off, 0 = On)
    def Fillfromright(self, LightValue):
        for LEDBARNUM in self.SIZE:
            LEDBAR = self.BarGraph[(self.SIZE - 1) - LEDBARNUM]
            LEDBAR.value(LightValue)
            self.outputLight(LEDBAR, LightValue)
            utime.sleep(wait_time)
        if LightValue == 1:
            self.resetSides()
        else:
            self.filledSides(True)

    # (AddOrSubtract Values: 1 = Off, 0 = On)
    def fromleft(self, NumValue, AddOrSubtract):
        OldValue = self.converter(AddOrSubtract)
        NewValue = AddOrSubtract
        if AddOrSubtract == 0: side = self.left_end
        else: side = self.right_end

        if NumValue < self.SIZE:
            for LEDBAR in self.BarGraph:
                if NumValue > 0:
                    if LEDBAR.value() == OldValue:
                        LEDBAR.value(NewValue)  # Turns it either on or off
                        NumValue -= 1
                        side+=1
                        self.outputLight(side, AddOrSubtract)
                        utime.sleep(wait_time)
        else:
            if NewValue == 0:
                self.Fillfromleft(0)
            else:
                self.Fillfromleft(1)

    # Used to show if the light is on or off.
    def outputLight(self, LED, value):
        # 1 = Off, 0 = On
        if value == 1:
            status = "Off"
        else:
            status = "On"
        print("LED-Bar #" + str(LED), status)

    # Turns all LEDs off quickly
    def empty(self):
        for LEDBAR in self.BarGraph:
            LEDBAR.value(1)
        self.resetSides()

    # Turns all LEDs on quickly
    def fill(self):
        for LEDBAR in self.BarGraph:
            LEDBAR.value(0)
        self.right_end = (self.SIZE - 1)
        self.left_end = 0

    @staticmethod
    def converter(value):
        if value == 1:
            return 0
        else:
            return 1

    # Method is to be used in internal methods only!
    def resetSides(self):
        self.right_end = 0
        self.left_end = 0

    # Method is to be used in internal methods only!
    def filledSides(self, flipped):
        if(flipped):
            self.right_end = 0
            self.left_end = (self.SIZE - 1)
        else:
            self.right_end = (self.SIZE - 1)
            self.left_end = 0


# while __name__ == '__main__':
# Makes sure that everything is off before starting.
LEDBG = LEDBar()
LEDBG.empty()

utime.sleep(.4)
LEDBG.fromleft(5, 0)
LEDBG.fromleft(5, 1)
