# Octopus Sensor Modules with MakeCode

The following example uses the [ELECFREAKS Octopus Water Level Sensor](https://www.elecfreaks.com/octopus-water-level-sensor.html) displayed below:

![octopus-waterlevel-sensor](assets/octopus-light-sensor.png)

Documentation for this sensor can be found [here](https://wiki.elecfreaks.com/en/microbit/sensor/octopus-sensors/sensor/octopus_ef04094).

---
## Example: Octopus Potentiometer
### Step 1: Connect the Potentiometer to the Breakout Board

The breakout boards provided for this presentation may differ from the one presented below. The breakout boards from DFRobot have a green pin instead of a yellow pin for the GPIO. Nevertheless, this demonstration's functionality is the same, as the order is still SVG.

Connect the water level sensor to pin 1 on the breakout board. The black pin (GND) should be connected to the black wire.

![micro:bit with Potentiometer](assets/microbit-octopus-potentiometer.png)

---

### Step 2: Import the Extensions

#### Importing the **datalogger** Extension

Select the ***Extensions*** in the Blocks Toolbox.

![Extensions Drawer](assets/makecode-extensions-01.png)  

Search for the ***datalogger*** extension and select it. 

![Searching for the datalogger extension](assets/makecode-extensions-02.png)

The datalogger blocks are now available in the Blocks Toolbox.

#### Importing the Extensions for Octopus Sensor Modules

> [!NOTE]
> THIS EXTENSION IS NOT USED TO READ THE ANALOG VALUE OF THE POTENTIOMETER, BUT IS USED TO READ THE OTHER SENSORS. 

![Datalogger extension](assets/makecode-extensions-03.png)

---

### Step 3: Label the Column on the `MY_DATA.HTM` File

Select the `set columns` block.

![Available blocks](assets/makecode-extensions-04.png)

Place the the `set columns` block in the `on start` block.

![Placing set columns block in on start block](assets/name-columns-02.png)

Enter text

![Placing set columns block in on start block](assets/name-columns-03.png)





|                                                              | Octopus Sensor                                       | MakeCode Block                                               |
| ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------ |
| <img src="assets/octopus-bme280-sensor.png" alt="octopus-bme280-sensor" style="zoom:25%;" /> | BME280 Temperature/Humidity/Pressure/Altitude Sensor | <img src="assets/octopus-bme280-sensor-makecode.png" alt="octopus-bme280-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-button.png" alt="Button" style="zoom:25%;" /> | Button                                               |                                                              |
| <img src="assets/octopus-crash-sensor.png" alt="Crash Sensor" style="zoom:25%;" /> | Crash Sensor                                         |                                                              |
| <img src="/Users/simon/Library/CloudStorage/OneDrive-Personal/-OneDrive-Shared/GitHub/Untitled/markdown-files/assets/octopus-dht11.png" alt="octopus-dht11" style="zoom:25%;" /> | DHT11 Temperature and Humidity Sensor                |                                                              |
| <img src="/Users/simon/Library/CloudStorage/OneDrive-Personal/-OneDrive-Shared/GitHub/Untitled/markdown-files/assets/octopus-ds18b20.png" alt="octopus-ds18b20" style="zoom:25%;" /> | DS18B20 Waterproof Temperature Sensor                |                                                              |
| <img src="assets/octopus-noise-sensor.png" alt="octopus-noise-sensor" style="zoom:25%;" /> | Noise Sensor                                         | <img src="assets/octopus-noise-sensor-makecode.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-photocell-sensor.png" alt="Photocell" style="zoom:25%;" /> | Photocell Light Sensor                               | <img src="assets/octopus-light-sensor-makecode.png" alt="octopus-light-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-pir-motion-sensor.png" alt="PIR Motion Sensor" style="zoom:25%;" /> | PIR Motion Sensor                                    |                                                              |
| <img src="assets/octopus-analog-rotation-brick.png" alt="Potentiometer" style="zoom:25%;" /> | Potentiometer                                        |                                                              |
| <img src="assets/octopus-soil-moisture-sensor.png" alt="octopus-noise-sensor" style="zoom:25%;" /> | Soil Moisture Sensor                                 | <img src="assets/octopus-soil-moisture-sensor-makecode.png" alt="octopus-soil-moisture-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-ultrasonic.png" alt="Ultrasonic Sensor" style="zoom:25%;" /> | Ultrasonic Distance Sensor                           |                                                              |
| <img src="assets/octopus-uv-sensor.png" alt="octopus-uv-sensor" style="zoom:25%;" /> | UV Sensor                                            | <img src="assets/octopus-uv-sensor-makecode.png" alt="octopus-uv-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-water-level-sensor.png" alt="octopus-water-level-sensor" style="zoom:25%;" /> | Water Level Sensor                                   | <img src="assets/octopus-water-level-sensor-makecode.png" alt="octopus-water-level-sensor-makecode" style="zoom:60%;" /> |

---

## Data Logging MakeCode Files
### Full Code Files

BME280 Temperature/Humidity/Pressure/Altitude Sensor

[DHT11 Temperature and Humidity Sensor](https://makecode.microbit.org/S03719-79254-31365-14802)

[DS18B20 Waterproof Temperature Sensor](https://makecode.microbit.org/S17353-69686-04118-57184)

[Noise Sensor](https://makecode.microbit.org/S68700-11119-27920-44083)

Photocell Light Sensor

[PIR Motion Sensor](https://makecode.microbit.org/S57511-02520-74396-99456)

[Potentiometer](https://makecode.microbit.org/S77162-35748-31506-14166)

Soil Moisture Sensor

[Ultrasonic Distance Sensor](https://makecode.microbit.org/S88082-50114-95773-88133)

[UV Sensor](https://makecode.microbit.org/S45208-14340-04934-11502)

[Water Level Sensor](https://makecode.microbit.org/S38317-05858-09223-80552)

### 
