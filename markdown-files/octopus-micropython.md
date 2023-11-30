# Octopus Sensor Modules with MicroPython

The following example uses the [ELECFREAKS Octopus Light Sensor](https://www.elecfreaks.com/octopus-water-level-sensor.html) displayed below:

![octopus-light-sensor](assets/octopus-light-sensor.png)

## Example: Octopus Light Sensor

### Step 1: Connect the Sensor to the Breakout Board

The breakout boards provided for this presentation may differ from the one presented below. The breakout boards from DFRobot have a green pin instead of a yellow pin for the GPIO. Nevertheless, the functionality is the same for this demonstration, as the order is still SVG.

Connect the sensor to pin 1 on the breakout board. The black pin (GND) should be connected to the black wire.

![micro:bit with Light Sensor](assets/microbit-octopus-light-sensor.png)

---

### Step 2: Import the Modules

The `log` module is a built-in module. The `octopus` module is an external file that must be uploaded into the [mico:bit Python Editor](https://python.microbit.org/v/3).

#### Downloading `octopus.py`

First, download the octopus module (`octopus.py`) in the GitHub repository [here](https://github.com/simonhasan/microbit-data-logging-2023-12-03/blob/main/code-files/octopus.py). 

Click on the ![github-download](assets/github-download.png) icon to download the file.

#### Uploading `octopus.py` into the micro:bit Python Editor.

Click on the **Projects** icon.

![python-editor-file-upload-01](assets/python-editor-file-upload-01.png)

Click on the **Open** button.

![python-editor-file-upload-02](assets/python-editor-file-upload-02.png)

[!NOTE] **Replace main code with ...** is the default. This will replace the code file flashed to the micro:bit.

![python-editor-file-upload-03](assets/python-editor-file-upload-03.png)

```python
from micro:bit import *
import log
from octopus import LIGHT
```



---

### Step 3: Label the Column on the `MY_DATA.HTM` File

```python
log.set_labels('light')
```



```python
while True:
    log.add({'light': LIGHT(pin1).get_light()})
    sleep(100)
```



```python
from microbit import *
import log
from octopus import LIGHT

log.set_labels('light')

while True:
    log.add({'light': LIGHT(pin1).get_light()})
    sleep(100)
```

|                                                              | Octopus Sensor         | `from octopus import ...` | Method for Sensor                                            |
| ------------------------------------------------------------ | ---------------------- | ------------------------- | ------------------------------------------------------------ |
| <img src="assets/octopus-bme280-sensor.png" alt="octopus-BME280-sensor" style="zoom:25%;" /> | BME280 Pressure Sensor | `BME20`                   | `BME280(pin1).get_temperature()`<br />`BME280(pin1).get_humidity()`<br />`BME280(pin1).get_altitude()`<br />`BME280(pin1).get_pressure()` |
| <img src="assets/octopus-light-sensor.png" alt="octopus-light-sensor" style="zoom:25%;" /> | Light Sensor           | `LIGHT`                   | `LIGHT(pin1).get_light()`                                    |
| <img src="assets/octopus-noise-sensor.png" alt="octopus-noise-sensor" style="zoom:25%;" /> | Noise Sensor           | `NOISE`                   | `NOISE(pin1).get_noise()`                                    |
| <img src="assets/octopus-soil-moisture-sensor.png" alt="octopus-noise-sensor" style="zoom:25%;" /> | Soil Moisture Sensor   | `SOIL_MOISTURE`           | `SOIL_MOISTURE(pin1).get_soil_moisture()`                    |
| <img src="assets/octopus-uv-sensor.png" alt="octopus-uv-sensor" style="zoom:25%;" /> | UV Sensor              | `UV`                      | `UV(pin1).get_uv_index()`                                    |
| <img src="assets/octopus-water-level-sensor.png" alt="octopus-water-level-sensor" style="zoom:25%;" /> | Water Level Sensor     | `WATER_LEVEL`             | `WATER_LEVEL(pin1).get_water_level()`                        |

