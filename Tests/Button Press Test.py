import machine
import utime

# IMPORTANT BEFORE STARTING!
# Double check and make sure the wires are in the breadboard and in the correct location!
# If they are not, the controller will go crazy and say that you are pressing the button repeatedly!

# Safe to edit variables

# how long should the device wait for before checking the input again?
# Reminder: Shorter time = more sensitive (<=.25) | Longer time = less sensitive (.5<) 
refresh_time = .25


# LED pin locations (Consult your device documentation for GP location before editing location)
# Used to send a power signal to the buttons
button_1_power = 13
button_2_power = 14
button_3_power = 15

# Used to recieve the power signal to see what buttons were pressed
button_1_reciever = 16
button_2_reciever = 17
button_3_reciever = 18

# ------------------------------ #
# Code is below, have fun learning!

# pins that power the buttons
btn_1_pwr = machine.Pin(button_1_power, machine.Pin.OUT)
btn_2_pwr = machine.Pin(button_2_power, machine.Pin.OUT)
btn_3_pwr = machine.Pin(button_3_power, machine.Pin.OUT)

# pins that recieve the signal from the buttons
btn_1_reciever = machine.Pin(button_1_reciever, machine.Pin.IN)
btn_2_reciever = machine.Pin(button_2_reciever, machine.Pin.IN)
btn_3_reciever = machine.Pin(button_3_reciever, machine.Pin.IN)


# Turns the buttons on for input
def power_on_buttons():
    btn_1_pwr.value(1)
    btn_2_pwr.value(1)
    btn_3_pwr.value(1)

# Checks if any buttons are pressed
def wait_for_press():
    if (btn_1_reciever.value() == 1):
        print("Button 1 pressed")
            
    if (btn_2_reciever.value() == 1):
        print("Button 2 pressed")
            
    if (btn_3_reciever.value() == 1):
        print("Button 3 pressed")




while __name__ == '__main__':
    power_on_buttons()
    
    while True:
        wait_for_press()
        utime.sleep(refresh_time)
