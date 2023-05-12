import machine
import utime

# IMPORTANT BEFORE STARTING!
# Double check and make sure the wires are in the breadboard and in the correct location!
# If they are not, the controller will go crazy and say that you are pressing the button repeatedly!

# Safe to edit variables

# How many seconds should the device wait for before checking the input again?
# Suggestions: Shorter time = (.25) | Longer time = (.5) 
refresh_time = .25

# LED pin locations (Consult your device documentation for GP location before editing location)
# Used to send a power signal to the buttons
BUTTON_1_POWER = 13
BUTTON_2_POWER = 14
BUTTON_3_POWER = 15

# Used to receive the power signal to see what buttons were pressed
BUTTON_1_RECIEVER = 16
BUTTON_2_RECIEVER = 17
BUTTON_3_RECIEVER = 18

# ------------------------------ #
# Code is below, have fun learning!

# Pins that power the buttons (These are not used)
BTN_1_PWR = machine.Pin(BUTTON_1_POWER, machine.Pin.OUT)
BTN_2_PWR = machine.Pin(BUTTON_2_POWER, machine.Pin.OUT)
BTN_3_PWR = machine.Pin(BUTTON_3_POWER, machine.Pin.OUT)

# Pins that recieve the signal from the buttons
BTN_1_RCVR = machine.Pin(BUTTON_1_RECIEVER, machine.Pin.IN)
BTN_2_RCVR = machine.Pin(BUTTON_2_RECIEVER, machine.Pin.IN)
BTN_3_RCVR = machine.Pin(BUTTON_3_RECIEVER, machine.Pin.IN)


BUTTON_ARRAY = [BTN_1_RCVR, BTN_2_RCVR, BTN_3_RCVR]


# Turns the buttons on for input
def power_on_buttons():
    for button in BUTTON_ARRAY:
        button.value(1)


# Checks if any buttons are pressed
def check_buttons():
    for button in BUTTON_ARRAY:
        if(button.value() == 1):
            print("Button", BUTTON_ARRAY.index(button), "pressed")


while __name__ == '__main__':
    power_on_buttons()

    while True:
        check_buttons()
        utime.sleep(refresh_time)
