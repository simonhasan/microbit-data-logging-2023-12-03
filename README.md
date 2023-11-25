# micro:bit Data Logging
Data logging with the BBC micro:bit. 

> [!NOTE]
> THIS REPO IS A WORK IN PROGRESS AND NOT THE FINAL REPO FOR THE PRESENTATION.

---





## Useful Links

### General Information

[Awesome micro:bit: A curated list of resources for the BBC micro:bit](https://github.com/carlosperate/awesome-microbit)

### MakeCode

[Documentation for the Datalogger extension](https://makecode.microbit.org/reference/datalogger)

[Documentation for the onboard sensors](https://makecode.microbit.org/reference/input)

### MicroPython

[Documentation for Data Logging with MicroPython](https://microbit-micropython.readthedocs.io/en/v2-docs/log.html)

[Documentation for the buttons](https://microbit-micropython.readthedocs.io/en/v2-docs/button.html)

---

## micro:bit Data Logging with MakeCode

[Water Level Sensor with MakeCode](files/waterlevel-makecode.md)

---

## micro:bit Data Logging with MicroPython

### Waterlevel Sensor

#### Step 1: Import the necessary modules.

```python
from microbit import *
import log
from waterlevel import WATERLEVEL as wl
```

#### Step 2: 



```python
from microbit import *
import log
from waterlevel import WATERLEVEL as wl

wl_pin = wl(pin1)
log.set_labels('water_level')

while True:
    wl_val = wl_pin.get_waterlevel()
    log.add({'water_level': wl_val})
    print('Water Level: ' + str(wl_val))
    sleep(5000)
```

