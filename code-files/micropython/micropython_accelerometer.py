# Imports go at the top
from microbit import *
import log

# Enable mirroring in serial
log.set_mirroring(True)

# Label the accelerometer columns on the MY_DATA.HTM file
log.set_labels('x', 'y', 'z')

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the accelerometer data
    if button_a.is_pressed():
        # Add rows to MY_DATA.HTM
        log.add({
            'x': accelerometer.get_x(),
            'y': accelerometer.get_y(),
            'z': accelerometer.get_z()
        })
    # If button B is pressed delete MY_DATA.HTM
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()

    sleep(10)
