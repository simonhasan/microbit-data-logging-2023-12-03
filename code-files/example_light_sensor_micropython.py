from microbit import *
import log
from octopus import Light

log.set_labels('light')

while True:
    log.add({'light': Light(pin1).get_light()})
    sleep(1)