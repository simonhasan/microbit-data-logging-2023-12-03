# On-Board Sensor Data Logging with MicroPython

This example uses the onboard sensors displayed below on the micro:bit:

![microbit-labeled](assets/microbit-labeled.png)

---

## Example: Accelerometer

### Step 1: Import the  Modules
Import the necessary module that are not preloaded with `import log`:

```python
# Imports go at the top
from microbit import *
import log
```
---
### Step 2: Enable `mirroring` in Serial

This is not compulsory, but seeing the data being recorded shows that the code is working.

```python
# Enable mirroring in serial
log.set_mirroring(True)
```

---

### Step 3: Label the Column on the `MY_DATA.HTM` File

Set the name of the row labels on the log file.

```python
# Label the accelerometer columns on the MY_DATA.HTM file
log.set_labels('x', 'y', 'z')
```

### Step 4: Log the Data

Log the data every 10 millisecond `sleep(10)` in a `while` loop while with the `log.add()`  method. 

```python
while True:
    # If button A is pressed log the accelerometer data
    if button_a.is_pressed():
        # Add rows to MY_DATA.HTM
        log.add({
            'x': accelerometer.get_x(),
            'y': accelerometer.get_y(),
            'z': accelerometer.get_z()
        })
    # If button B is pressed delete MY_DATA.HTM
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()
    sleep(10)
```

   Here is the complete commented code for the accelerometer.

```python
# Imports go at the top
from microbit import *
import log

# Enable mirroring in serial
log.set_mirroring(True)

# Label the accelerometer columns on the MY_DATA.HTM file
log.set_labels('x', 'y', 'z')

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the accelerometer data
    if button_a.is_pressed():
        # Add rows to MY_DATA.HTM
        log.add({
            'x': accelerometer.get_x(),
            'y': accelerometer.get_y(),
            'z': accelerometer.get_z()
        })
    # If button B is pressed delete MY_DATA.HTM
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()

    sleep(10)

```
---

## Code for Other On-Board Sensors


Change the labels in `log.set_labels()`. Make sure the names are strings in `' '` or `" "`. If there is more than one label, separate them with commas.

`accelerometer.get_x()`: Get acceleration (x).
`accelerometer.get_y()`: Get acceleration (y).
`accelerometer.get_y()`: Get acceleration (z).
`compass.get_field_strength()` : Get magnetic field strength (overall).
`compass.get_x()`: Get magnetic field strength (x).
`compass.get_y()`: Get magnetic field strength (y).
`compass.get_z()`: Get magnetic field strength (z).
`microphone.sound_level()`
`read_light_level()`: Get light level.
`temperature()`: Get temperature.
