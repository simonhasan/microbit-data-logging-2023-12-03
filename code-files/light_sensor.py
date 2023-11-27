from microbit import *
import log
from octopus import LIGHT

log.set_labels('light')

while True:
    log.add({'light': LIGHT(pin1).get_light()})
    sleep(100)