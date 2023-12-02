# Imports go at the top
from microbit import *
import log
from octopus import UV

# Delete MY_DATA.HTM if present
log.delete()

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('uv')

# Create an instance of the UV class 
uv = UV(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # Add a row to MY_DATA.HTM 
    log.add({
        'uv': uv.get_uv()
    })
    # Repeat every 10 milliseconds
    sleep(10)