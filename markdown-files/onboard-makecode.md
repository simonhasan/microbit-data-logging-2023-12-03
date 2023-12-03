# On-Board Sensor Data Logging with MakeCode

This example uses the onboard sensors displayed below on the micro:bit:

![microbit-labeled](assets/microbit-labeled.png)

## Example: Accelerometer

### Step 1: Import the datalogger Extension

Select the ***Extensions*** in the Blocks Toolbox.

![Extensions Drawer](/Users/simon/Library/CloudStorage/OneDrive-Personal/-OneDrive-Shared/GitHub/Untitled/markdown-files/assets/makecode-extensions-01.png)  

Search for the ***datalogger*** extension and select it. 

![Searching for the datalogger extension](assets/makecode-extensions-02.png)

The datalogger blocks are now available in the Blocks Toolbox.

### Step 2: Mirror Data to Serial

Drag the `mirror data to serial` block into the `on start` block:

![block-enable-logging-serial](assets/block-enable-logging-serial.png)

---

### Step 4: Label the Label the Columns on the `MY_DATA.HTM` File 

 

Select the `set columns` block. Drag it under the `mirror data to serial` block:

![block-enable-logging-serial](assets/block-label-columns.png)