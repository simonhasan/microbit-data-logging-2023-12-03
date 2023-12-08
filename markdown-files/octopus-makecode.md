# Octopus Sensor Modules with MakeCode

The example uses the [ELECFREAKS Octopus Noise Sensor](https://shop.elecfreaks.com/products/elecfreaks-octopus-analog-noise-sensor?_pos=1&_sid=3b206475e&_ss=r) displayed below:

![octopus-waterlevel-sensor](assets/octopus-noise-sensor.png)

---
## Example: Octopus Noise Sensor
### Step 1: Connect the Noise to the Breakout Board

The breakout boards provided for this presentation may differ from the one presented below. The breakout boards from DFRobot have a green pin instead of a yellow pin for the GPIO. Nevertheless, this demonstration's functionality is the same, as the order is still SVG.

Connect the water level sensor to pin 1 on the breakout board. The black pin (GND) should be connected to the black wire.

![micro:bit with Potentiometer](assets/noise-microbit.png)

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

The Octopus blocks are now available in the Blocks Toolbox.

---

### Step 3: Mirror Data to Serial

Drag the `mirror data to serial` block from `Data Logger` into the `on start` block:

![block-enable-logging-serial](assets/block-enable-logging-serial.png)

---

### Step 4: Label the Label the Columns on the `MY_DATA.HTM` File 

 

Select the `set columns` block from `Data Logger`. Drag it under the `mirror data to serial` block:

![block-enable-logging-serial](assets/block-label-columns.png)

Name the column.

![block-label-columns-named](assets/block-label-columns-named.png)



---

### Step 5: Get a Timed Loop 

Get an `every <500> ms` block from `Loops` (green):

![block-every-ms](assets/block-every-ms.png)

---

### Step 6: Get Conditional Blocks

Get two `if < > then` blocks from `Logic` (teal):

![block-conditionals](assets/block-conditionals.png)

---

### Step 7: Get the Conditions

Get two `block < > is pressed` blocks from `Input` . Place them in the open space of the `if < > then` blocks. Make sure that one is `A` and one is `B`.

![block-every-button](assets/block-every-button.png)



---

### Step 8: Add The Data Logging Block

Get a `log data < >` block from `Data Logger` Place it in the `if button <A> is pressed then` block.

![block-if-button-a-log-01](assets/block-if-button-a-log-01.png)

Name the column the same name as in **Step 4**:

![block-if-button-a-log-02](assets/block-if-button-a-log-02.png)

Drag an Octopus block in as the value:

![block-if-button-a-log-03](assets/block-if-button-a-log-03.png)

Add a `delete log` block in the `if button <b> is pressed` block.



**All done**

![block-if-button-a-log-05](assets/block-if-button-a-log-05.png)

Here is the full code:

![block-octopus-all-code](assets/block-octopus-all-code.png)

## Other ELECFREAKS Octopus Sensors

Here are the sensors that are available to tinker with in this presentation. The code will be the same as above with a sensor-specific code.  For example:

|                                                              | Octopus Sensor                        | MakeCode Block                                               |
| ------------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------------ |
| <img src="/Users/simon/Library/CloudStorage/OneDrive-Personal/-OneDrive-Shared/GitHub/Untitled/markdown-files/assets/octopus-dht11.png" alt="octopus-dht11" style="zoom:25%;" /> | DHT11 Temperature and Humidity Sensor | <img src="assets/block-octopus-dht11.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="/Users/simon/Library/CloudStorage/OneDrive-Personal/-OneDrive-Shared/GitHub/Untitled/markdown-files/assets/octopus-ds18b20.png" alt="octopus-ds18b20" style="zoom:25%;" /> | DS18B20 Waterproof Temperature Sensor | <img src="assets/block-octopus-ds18b20.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-noise-sensor.png" alt="octopus-noise-sensor" style="zoom:25%;" /> | Noise Sensor                          | <img src="assets/block-octopus-noise.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-photocell-sensor.png" alt="Photocell" style="zoom:25%;" /> | Photocell Light Sensor                | <img src="assets/block-octopus-light.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-pir-motion-sensor.png" alt="PIR Motion Sensor" style="zoom:25%;" /> | PIR Motion Sensor                     | <img src="assets/block-octopus-pir.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-soil-moisture-sensor.png" alt="octopus-noise-sensor" style="zoom:25%;" /> | Soil Moisture Sensor                  | <img src="assets/block-octopus-soil-moisture.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-ultrasonic.png" alt="Ultrasonic Sensor" style="zoom:25%;" /> | Ultrasonic Distance Sensor            | <img src="assets/block-octopus-ultrasonic.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-uv-sensor.png" alt="octopus-uv-sensor" style="zoom:25%;" /> | UV Sensor                             | <img src="assets/block-octopus-uv.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |
| <img src="assets/octopus-water-level-sensor.png" alt="octopus-water-level-sensor" style="zoom:25%;" /> | Water Level Sensor                    | <img src="assets/block-octopus-water-level.png" alt="octopus-noise-sensor-makecode" style="zoom:60%;" /> |

---

## Data Logging MakeCode Files
### Full Code Files

[DHT11 Temperature and Humidity Sensor](https://makecode.microbit.org/S03719-79254-31365-14802)

[DS18B20 Waterproof Temperature Sensor](https://makecode.microbit.org/S17353-69686-04118-57184)

[Noise Sensor](https://makecode.microbit.org/S68700-11119-27920-44083)

[Photocell Light Sensor](https://makecode.microbit.org/S89999-13858-88027-85367)

[PIR Motion Sensor](https://makecode.microbit.org/S57511-02520-74396-99456)

[Potentiometer](https://makecode.microbit.org/S77162-35748-31506-14166)

[Soil Moisture Sensor](https://makecode.microbit.org/S36205-15253-87046-65346)

[Ultrasonic Distance Sensor](https://makecode.microbit.org/S88082-50114-95773-88133)

[UV Sensor](https://makecode.microbit.org/S45208-14340-04934-11502)

[Water Level Sensor](https://makecode.microbit.org/S38317-05858-09223-80552)

### 
