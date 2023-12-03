# Imports go at the top
from microbit import *
import log
from octopus import SoilMoisture

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('soil_moisture')

# Create an instance of the SoilMoisture class 
sm = SoilMoisture(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed
    if button_a.is_pressed():
        # Add a row to MY_DATA.HTM
        log.add({
            'soil_moisture': sm.get_soil_moisture()
        })
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()

    # Repeat every 10 milliseconds
    sleep(10)
