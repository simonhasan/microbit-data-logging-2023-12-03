# Imports go at the top
from microbit import *
import log
from octopus import PIR

# Delete MY_DATA.HTM if present
log.delete()

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('motion')

# Create an instance of the PIR class
pir = PIR(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # Add a row to MY_DATA.HTM 
    log.add({
        'motion': pir.get_motion()
    })
    # Repeat every 10 milliseconds
    sleep(10)
