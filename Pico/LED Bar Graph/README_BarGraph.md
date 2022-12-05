# LED Bar Graph
Used for testing the LED bar graph. This program powers on each LED in the bar graph, and 
prints out which LED is on and off.

## Needed for this project:
* 10x 220Ω resistors (To deliver power to the LEDs)
* 11x Jumper wires (1 for power, 10 for each LED bar)
* 1x Micro USB Cable (for the Pico)
* 1x Pico or Pico W
* 1x LED Bar Graph
* 1x Breadboard

## Set up
### 1. Bar Graph LED Placement
> Place the Bar Graph LED in the middle of the breadboard (Face the label towards the left of the breadboard 
> to avoid confusion later)


### 2. Powering on the Bar Graph 
> 1. Place a cable from Pin #36 (3V3(OUT)) to the + (positive) column on the left side.


> 2. Connect 220Ω resistors from the + (positive) column to each of the Bar Graph LED's pins.
> (One resistor should connect to one of the pins on the LED Bar Graph)


### 3. LED Cable Placement
> 1. Update and use the LED Variables list in the program while you are connecting the cables from the Pico to the LED Bar Graph.
    (Recommended if you don't want to be confused later)

### Known issues while programming
> * Try/Except for KeyboardInterrupt is not working. 
> When implemented, the program would go back to the beginning of the loop.