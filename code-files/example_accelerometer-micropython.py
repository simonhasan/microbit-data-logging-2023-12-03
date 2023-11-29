from microbit import *
import log

log.set_labels('x', 'y', 'z')

while True:
    log.add({
      'x': accelerometer.get_x(),
      'y': accelerometer.get_x(),
      'z': accelerometer.get_x()
    })
    sleep(100)
