# Imports go at the top
from microbit import *
import log
from octopus import TMP36

# Delete MY_DATA.HTM if present
log.delete()

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('temperature')

# Create an instance of the TMP36 class
temp = TMP36(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # Add a row to MY_DATA.HTM 
    log.add({
        'temperature': temp.get_temperature()
    })
    # Repeat every 10 milliseconds
    sleep(10)
