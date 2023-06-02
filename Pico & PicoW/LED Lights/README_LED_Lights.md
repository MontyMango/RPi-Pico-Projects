# Button Press Test
> Used for testing the buttons. This program powers on each LED in the bar graph, and prints out which LED is on and off.

## Needed for this project:
* 7x Male to Male Jumper wires (1 for the ground column, 3 for powering each LED, and 3 for grounding the LEDs)
* 3x 220Ω resistors
* 3x LEDs 
* 1x Micro USB Cable (for the Pico)
* 1x Pico or Pico W
* 1x Breadboard

## Instructions

### 1. Pico / Pico W Placement 
* Place the Soldered Pico / Pico W on the end of the breadboard.


### 2. LED Placement
* Place the 3 LEDs on the breadboard. It doesn't matter which side of the breadboard they are on. But, make sure that the LEDs aren't on the same row.


### 3. Connect the LEDs!
1. Place a (male to male) cable from the GP led pins that are stated on the code (led_#_GP) to a open port next to the LEDs.
> Please review and follow the code and pinout documentation while doing step 1!

2. Place a cable from pin #38 (GND) to the - (negative) column on the right side.

3. Connect a cable from the right side's - (negative) column to each of the LEDs' SHORTEST pin to ground them.

4. Connect the 220Ω resistors from the cable's row that you placed near the LEDs in step #1 to the LONGEST pin in the LEDs to power them! 

5. Run the script and enjoy the light show!


### Known issues while programming:
* Try/Except for KeyboardInterrupt is not working. When implemented, the program would go back to the beginning of the loop.