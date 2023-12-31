# Octopus Sensor Modules with MicroPython

## Contents

The example uses the [ELECFREAKS Octopus Noise Sensor](https://shop.elecfreaks.com/products/elecfreaks-octopus-analog-noise-sensor?_pos=1&_sid=3b206475e&_ss=r) displayed below:

![octopus-light-sensor](assets/octopus-noise-sensor.png)

## Example: Octopus Potentiometer

### Step 1: Connect the Sensor to the Breakout Board

The breakout boards provided for this presentation may differ from the one presented below. The breakout boards from DFRobot have a green pin instead of a yellow pin for the GPIO. Nevertheless, this demonstration's functionality is the same, as the order is still SVG.

Connect the sensor to pin1 on the breakout board. The black pin (GND) should be connected to the black wire.

![micro:bit with Potentiometer](assets/noise-microbit.png)

---

### Step 2: Uploading External Modules

The `log` module is a built-in module. The `octopus` module is an external file that must be uploaded into the [mico:bit Python Editor](https://python.microbit.org/v/3).

#### Downloading `octopus.py`

First, download the octopus module (`octopus.py`) in the GitHub repository [here](code-files/micropython/octopus.py). This is a collection of several official ELECFREAKS modules combined in one file for convenience. Other code that is not available from ELECTFREAKS has been added. This is a module that I created to make it easier for my students to use the sensors using MicroPython.

Click on the ![github-download](assets/github-download.png) icon to download the file.

#### Uploading `octopus.py` into the micro:bit Python Editor.

Click on the **Projects** icon.

![python-editor-file-upload-01](assets/python-editor-file-upload-01.png)

Click on the **Open** button.

![python-editor-file-upload-02](assets/python-editor-file-upload-02.png)

> [!NOTE]
>  **Replace main code with ...** is the default. This will replace the code file flashed to the micro:bit.

![python-editor-file-upload-03](assets/python-editor-file-upload-03.png)

Change the way the file is imported with the file settings icon ![file-settings-icon](assets/file-settings-icon.png).

![python-editor-file-upload-04](assets/python-editor-file-upload-04.png)                                                                            

Change the option from **Replace main code with octopus.py** to **Add file octopus.py**.

![python-editor-file-upload-04](assets/python-editor-file-upload-05.png)

The change is reflected in the dialog box.

![python-editor-file-upload-04](assets/python-editor-file-upload-06.png)

Press the **Confirm** button.

![python-editor-file-upload-04](assets/python-editor-file-upload-07.png)

The file `octopus.py` is now available as a Python module that can be imported.

![python-editor-file-upload-04](assets/python-editor-file-upload-08.png)

The file now works with the micro:bit Python Editor code completion feature.

![python-editor-file-upload-04](assets/python-editor-file-upload-09.png)

---

### Step 3: Import the Modules

Import the necessary modules that are not preloaded with `import log` and `from octopus import Potentiometer` as demonstrated below:

```python
# Imports go at the top
from microbit import *
import log
from octopus import Potentiometer
```

---

### Step 4: Enable `mirroring` in Serial

This is not compulsory, but seeing the data being recorded shows that the code is working.

```python
# Enable mirroring in serial
log.set_mirroring(True)
```

---

### Step 5: Label the Columns on the `MY_DATA.HTM` File

Set the name of the row labels on the log file.

```python
# Label the light column on the MY_DATA.HTM file
log.set_labels('analog_val')
```

---

### Step 6: Create an Instance of the Potentiometer Object

This is just good practice. `pot` is a common name for a potentiometer variable, but this does not work well with students.

```python
# Create an instance of the Potentiometer class 
p = Potentiometer(pin1)
```



---

### Step 7: Log the Data

Log the data every 10 millisecond `sleep(10)` in a `while` loop while with the `log.add()`  method. 

```python
# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the potentiometer data
    if button_a.is_pressed():
        # Add a row to MY_DATA.HTM
        log.add({
            'analog_val': p.get_analog()
        })
    # If button B is pressed delete MY_DATA.HTM    
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()

    # Repeat every 10 milliseconds
    sleep(10)
```

Here is the complete commented code for the Octopus Potentiometer.

```python
# Imports go at the top
from microbit import *
import log
from octopus import Potentiometer

# Enable mirroring in serial
log.set_mirroring(True)

# Label the light column on the MY_DATA.HTM file
log.set_labels('analog_val')

# Create an instance of the Potentiometer class 
p = Potentiometer(pin1)

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed log the potentiometer data
    if button_a.is_pressed():
        # Add a row to MY_DATA.HTM
        log.add({
            'analog_val': p.get_analog()
        })
    # If button B is pressed delete MY_DATA.HTM    
    if button_b.is_pressed():
        # Delete MY_DATA.HTM
        log.delete()

    # Repeat every 10 milliseconds
    sleep(10)
    
```
---

## Other ELECFREAKS Octopus Sensors

Here are the sensors that are available to tinker with in this presentation. The code will be the same as above with a sensor-specific code.  For example:

If the Octopus Water Level sensor is chosen use:

- `from octopus import WaterLevel` instead of `from octopus import Potentiometer`. 
-  `wl = WaterLevel(pin1)` instead of `p = Potentiometer(pin1)` **OR**

Links to the `.hex` files are included in the **Octopus Sensor** column:

|                                                              | Octopus Sensor                                               | `from octopus import ...` | Method for the Sensor                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------ |
| <img src="assets/octopus-button.png" alt="Button" style="zoom:25%;" /> | [Button](code-files/micropython/micropython_button.hex)      | `Button`                  | `button = Button(pin1)`<br /><br />`button.get_presses()`    |
| <img src="assets/octopus-crash-sensor.png" alt="Crash Sensor" style="zoom:25%;" /> | [Crash Sensor](code-files/micropython/micropython_crash.hex) | `Crash`                   | `crash = Crash(pin1)`<br /><br />`crash.get_presses()`       |
| <img src="assets/octopus-noise-sensor.png" alt="Noise Sensor" style="zoom:25%;" /> | [Noise Sensor](code-files/micropython/micropython_noise.hex) | `Noise`                   | `noise = Noise(pin1)`<br /><br />`noise.get_noise()`         |
| <img src="assets/octopus-photocell-sensor.png" alt="Photocell" style="zoom:25%;" /> | [Photocell Light Sensor](code-files/micropython/micropython_photocell.hex) | `Light`                   | `light = Light(pin1)`<br /><br />`light.get_light()`         |
| <img src="assets/octopus-pir-motion-sensor.png" alt="PIR Motion Sensor" style="zoom:25%;" /> | [PIR Motion Sensor](code-files/micropython/micropython_pir.hex) | `PIR`                     | `pir = PIR(pin1)`<br /><br />`pir.get_motion()`              |
| <img src="assets/octopus-analog-rotation-brick.png" alt="Potentiometer" style="zoom:25%;" /> | [Potentiometer](code-files/micropython/micropython_potentiometer.hex) | `Potentiometer`           | `p = Potentiometer(pin1)`<br /><br />`p.get_analog()`        |
| <img src="assets/octopus-soil-moisture-sensor.png" alt="Soil Moisture Sensor" style="zoom:25%;" /> | [Soil Moisture Sensor](code-files/micropython/micropython_soil_moisture.hex) | `SoilMoisture`            | `sm = SoilMoisture(pin1)`<br /><br />`sm.get_soil_moisture()` |
| <img src="assets/octopus-tmp36.png" alt="TMP36" style="zoom:25%;" /> | [TMP36 Temperature Sensor](code-files/micropython/micropython_tmp36.hex) | `TMP36`                   | `temp = TMP36(pin1)`<br /><br />`temp.get_temperature()`     |
| <img src="assets/octopus-ultrasonic.png" alt="Ultrasonic Sensor" style="zoom:25%;" /> | [Ultrasonic Distance Sensor](code-files/micropython/micropython_distance.hex) | `Distance`                | `dist = Distance(pin1)`<br /><br />`dist.get_distance()`     |
| <img src="assets/octopus-uv-sensor.png" alt="UV Sensor" style="zoom:25%;" /> | [UV Sensor](code-files/micropython/micropython_uv.hex)       | `UV`                      | `uv = UV(pin1)`<br /><br />`uv.get_uv()`                     |
| <img src="assets/octopus-water-level-sensor.png" alt="Water Level Sensor" style="zoom:25%;" /> | [Water Level Sensor](code-files/micropython/micropython_water_level.hex) | `WaterLevel`              | `wl = WaterLevel(pin1)`<br /><br />`wl.get_water_level()`    |

