# Imports go at the top
from microbit import *
import log
from octopus import BME280

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('temperature', 'humidity', 'pressure', 'altitude')

# Create an instance of the BME280 class without an argument
bme280 = BME280() # DOES NOT TAKE AN ARGUMENT

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the BME280 data
    if button_a.is_pressed():
        # Add a row to MY_DATA.HTM 
        log.add({
            'temperature': bme280.get_temperature(),
            'humidity': bme280.get_humidity(),
            'pressure': bme280.get_pressure(),
            'altitude': bme280.get_altitude()
        })
    # If button B is pressed delete MY_DATA.HTM
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()
        
    # Repeat every 10 milliseconds
    sleep(10)
