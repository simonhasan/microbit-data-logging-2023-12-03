# Octopus Sensor Modules with MakeCode

The following example uses the [ELECFREAKS Octopus Water Level Sensor](https://www.elecfreaks.com/octopus-water-level-sensor.html) displayed below:

![octopus-waterlevel-sensor](assets/octopus-light-sensor.png)

Documentation for this sensor can be found [here](https://wiki.elecfreaks.com/en/microbit/sensor/octopus-sensors/sensor/octopus_ef04094).

---
## Example: Octopus Light Sensor
### Step 1: Connect the Water Level Sensor to the Breakout Board

The breakout boards provided for this presentation may differ from the one presented below. The breakout boards from DFRobot have a green pin instead of a yellow pin for the GPIO. Nevertheless, the functionality is the same for this demonstration, as the order is still SVG.

Connect the water level sensor to pin 1 on the breakout board. The black pin (GND) should be connected to the black wire.

![micro:bit with Light Sensor](assets/microbit-octopus-light-sensor.png)

---

### Step 2: Import the Extensions

Select the ***Extensions*** in the Blocks Toolbox.

![Extensions Drawer](assets/makecode-extensions-01.png)  

Search for the ***datalogger*** extension and select it. 

![Searching for the datalogger extension](assets/makecode-extensions-02.png)

The datalogger blocks are now avalable in the Blocks Toolbox.

![Datalogger extension](assets/makecode-extensions-03.png)

---

### Step 3: Label the Column on the `MY_DATA.HTM` File

Select the `set columns` block.

![Available blocks](assets/makecode-extensions-04.png)

Place the the `set columns` block in the `on start` block.

![Placing set columns block in on start block](assets/name-columns-02.png)

Enter text

![Placing set columns block in on start block](assets/name-columns-03.png)





|                                                              | Octopus Sensor         | MakeCode Block                                               |
| ------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------ |
| <img src="assets/octopus-bme280-sensor.png" alt="octopus-bme280-sensor" style="zoom:25%;" /> | BME280 Pressure Sensor | <img src="assets/octopus-bme280-sensor-makecode.png" alt="octopus-bme280-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-light-sensor.png" alt="octopus-light-sensor" style="zoom:25%;" /> | Light Sensor           | <img src="assets/octopus-light-sensor-makecode.png" alt="octopus-light-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-noise-sensor.png" alt="octopus-noise-sensor" style="zoom:25%;" /> | Noise Sensor           | <img src="assets/octopus-noise-sensor-makecode.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-soil-moisture-sensor.png" alt="octopus-noise-sensor" style="zoom:25%;" /> | Soil Moisture Sensor   | <img src="assets/octopus-soil-moisture-sensor-makecode.png" alt="octopus-soil-moisture-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-uv-sensor.png" alt="octopus-uv-sensor" style="zoom:25%;" /> | UV Sensor              | <img src="assets/octopus-uv-sensor-makecode.png" alt="octopus-uv-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-water-level-sensor.png" alt="octopus-water-level-sensor" style="zoom:25%;" /> | Water Level Sensor     | <img src="assets/octopus-water-level-sensor-makecode.png" alt="octopus-water-level-sensor-makecode" style="zoom:60%;" /> |

![name-columns-03](assets/name-columns-03.png)
