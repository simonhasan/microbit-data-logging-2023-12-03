# Imports go at the top
from microbit import *
import log
from octopus import Potentiometer

# Delete MY_DATA.HTM if present
log.delete()

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('analog_val')

# Create an instance of the Potentiometer class 
p = Potentiometer(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # Add a row to MY_DATA.HTM 
    log.add({
        'analog_val': p.get_analog()
    })
    
    # Repeat every 10 milliseconds
    sleep(10)
