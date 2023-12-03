# Imports go at the top
from microbit import *
import log
from octopus import Button

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('button')

# Create an instance of the Button class 
button = Button(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the button data
    if button_a.is_pressed():
        # Add a row to MY_DATA.HTM
        log.add({
            'button': button.get_presses()
        })
    # If button B is pressed delete MY_DATA.HTM
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()
        
    # Repeat every 10 milliseconds
    sleep(10)
