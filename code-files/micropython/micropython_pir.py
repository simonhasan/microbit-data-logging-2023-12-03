# Imports go at the top
from microbit import *
import log
from octopus import PIR

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('motion')

# Create an instance of the PIR class
pir = PIR(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the PIR data
    if button_a.is_pressed():
        # Add a row to MY_DATA.HTM
        log.add({
            'motion': pir.get_motion()
        })
    # If button B is pressed delete MY_DATA.HTM
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()

    # Repeat every 10 milliseconds
    sleep(10)
