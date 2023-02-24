# Button Press Test
> Used for testing the buttons. This program powers on each LED in the bar graph, and prints out which LED is on and off.

## Needed for this project:
* 7x Jumper wires (1 for power, 3 for powering the buttons, and 3 for recieving button signals)
* 3x Buttons
* 1x Micro USB Cable (for the Pico)
* 1x Pico or Pico W
* 1x Breadboard

## Instructions

### 1. Pico / Pico W Placement 
* Place the Soldered Pico / Pico W on the end of the breadboard.


### 2. Button Placement
* Place the 3 buttons on the breadboard. It doesn't matter which side of the breadboard they are on. But, make sure that the buttons aren't on the same row.


### 3. Time to Power the Buttons!
1. Place a cable from Pin #36 (3V3(OUT)) to the + (positive) column on the left side.

# EDIT BELOW THIS ROW
2. Connect 220Ω resistors from the + (positive) column to each of the buttons. You pick what prong on the button is powered (It does not matter which prong is powered).


### 4. Connect those Buttons to the Reciever
1. Update and use the LED Variables list in the program while you are connecting the cables from the Pico to the LED Bar Graph. (Recommended if you don't want to be confused later)


### Known issues while programming:
* Try/Except for KeyboardInterrupt is not working. When implemented, the program would go back to the beginning of the loop.