'''
Modified and unified version of modules from ELECFREAKS
https://github.com/elecfreaks/Octopus_MicroPython
'''

from microbit import *
import time
import utime
from time import sleep_us
from machine import time_pulse_us

BME280_I2C_ADDR = 0x76 # For BME280

# Octopus BME280 Pressure Sensor
class BME280():
    def __init__(self):
        """BME280 temperature, humidity, and barometric pressure sensor
        
        Returns:
            temperature C
            humidity 0-100% 
            atmospheric pressure hPa 
            altitude M according to air pressure
        """
        self._T1 = self.__g2r(0x88)
        self._T2 = self.__short(self.__g2r(0x8A))
        self._T3 = self.__short(self.__g2r(0x8C))
        self._P1 = self.__g2r(0x8E)
        self._P2 = self.__short(self.__g2r(0x90))
        self._P3 = self.__short(self.__g2r(0x92))
        self._P4 = self.__short(self.__g2r(0x94))
        self._P5 = self.__short(self.__g2r(0x96))
        self._P6 = self.__short(self.__g2r(0x98))
        self._P7 = self.__short(self.__g2r(0x9A))
        self._P8 = self.__short(self.__g2r(0x9C))
        self._P9 = self.__short(self.__g2r(0x9E))
        self._H1 = self.__gr(0xA1)
        self._H2 = self.__short(self.__g2r(0xE1))
        self._H3 = self.__gr(0xE3)
        a = self.__gr(0xE5)
        self._H4 = (self.__gr(0xE4) << 4) + (a % 16)
        self._H5 = (self.__gr(0xE6) << 4) + (a >> 4)
        self._H6 = self.__gr(0xE7)
        if self._H6 > 127:
            self._H6 -= 256
        self.__sr(0xF2, 0x04)
        self.__sr(0xF4, 0x2F)
        self.__sr(0xF5, 0x0C)
        self.__T = 0
        self.__P = 0
        self._H = 0

    def __short(self, dat):
        if dat > 32767:
            return dat - 65536
        else:
            return dat

    # set reg
    def __sr(self, reg, dat):
        i2c.write(BME280_I2C_ADDR, bytearray([reg, dat]))

    # __get reg
    def __gr(self, reg):
        i2c.write(BME280_I2C_ADDR, bytearray([reg]))
        t = i2c.read(BME280_I2C_ADDR, 1)
        return t[0]

    # __get two reg
    def __g2r(self, reg):
        i2c.write(BME280_I2C_ADDR, bytearray([reg]))
        t = i2c.read(BME280_I2C_ADDR, 2)
        return t[0] + t[1] * 256

    def __get(self):
        adc_T = (self.__gr(0xFA) << 12) + (self.__gr(0xFB) << 4) + \
                (self.__gr(0xFC) >> 4)
        var1 = (((adc_T >> 3) - (self._T1 << 1)) * self._T2) >> 11
        var2 = (((((adc_T >> 4) - self._T1) * ((adc_T >> 4) - self._T1)) >> 12)
                * self._T3) >> 14
        t = var1 + var2
        self.__T = ((t * 5 + 128) >> 8) / 100
        var1 = (t >> 1) - 64000
        var2 = (((var1 >> 2) * (var1 >> 2)) >> 11) * self._P6
        var2 = var2 + ((var1 * self._P5) << 1)
        var2 = (var2 >> 2) + (self._P4 << 16)
        var1 = (((self._P3 * ((var1 >> 2) * (var1 >> 2)) >> 13) >> 3) +
                (((self._P2) * var1) >> 1)) >> 18
        var1 = ((32768 + var1) * self._P1) >> 15
        if var1 == 0:
            return  # avoid exception caused by division by zero
        adc_P = (self.__gr(0xF7) << 12) + (self.__gr(0xF8) << 4) + \
                (self.__gr(0xF9) >> 4)
        p = ((1048576 - adc_P) - (var2 >> 12)) * 3125
        if p < 0x80000000:
            p = (p << 1) // var1
        else:
            p = (p // var1) * 2
        var1 = (self._P9 * (((p >> 3) * (p >> 3)) >> 13)) >> 12
        var2 = ((p >> 2) * self._P8) >> 13
        self.__P = p + ((var1 + var2 + self._P7) >> 4)
        adc_H = (self.__gr(0xFD) << 8) + self.__gr(0xFE)
        var1 = t - 76800
        var2 = (((adc_H << 14) - (self._H4 << 20) -
                 (self._H5 * var1)) + 16384) >> 15
        var1 = var2 * (((((((var1 * self._H6) >> 10) * (
                ((var1 * self._H3) >> 11) + 32768)) >> 10) + 2097152) *
                        self._H2 + 8192) >> 14)
        var2 = var1 - (((((var1 >> 15) * (var1 >> 15)) >> 7) * self._H1) >> 4)
        if var2 < 0:
            var2 = 0
        if var2 > 419430400:
            var2 = 419430400
        self._H = (var2 >> 12) / 1024
        return [self.__T, self.__P, self._H]

    # __get Temperature in Celsius ℃
    def get_temperature(self):
        """
        Read temperature C
        """
        self.__get()
        return self.__T

    # __get Humidity in %RH
    def get_humidity(self):
        """
        Read humidity %
        """
        self.__get()
        return self._H

    # __get Pressure in Pa
    def get_pressure(self):
        """
        Read barometric pressure pa
        """
        self.__get()
        return self.__P

    # Calculating absolute altitude
    def get_altitude(self):
        """
        Read altitude M
        """
        self.__get()
        return 44330 * (1 - (self.__P / 101325) ** (1 / 5.255))

    # normal mode
    def set_power_on(self):
        """
        The module starts working, monitoring environmental variables in real time
        """
        self.__sr(0xF4, 0x2F)

    # sleep mode
    def set_power_off(self):
        """
        The module sleeps, retains the last detected environment value, and is not refreshed
        """
        self.__sr(0xF4, 0)

class DataError(Exception):
    pass

# Octopus Sonor:bit
class DISTANCE(object):
    """HC_SR04 ultrasonic sensor

    Args:
        pin_trig (pin): Trig pin
        pin_echo (pin): Echo pin   
    """

    def __init__(self, pin_d):
        self.__pin_e = pin_d
        self.__pin_t = pin_d

    def get_distance(self, unit=0):
        """Read the distance

        Args:
            unit (number)

        Returns:
            distance 
        """
        self.__pin_e.read_digital()
        self.__pin_t.write_digital(1)
        sleep_us(10)
        self.__pin_t.write_digital(0)
        ts = time_pulse_us(self.__pin_e, 1, 25000)

        distance = ts * 9 / 6 / 58
        if unit == 0:
            return distance
        elif unit == 1:
            return distance / 254

# Octopus Dust Sensor
class DUST(object):
    """Dust sensor

    Args:
        pin
    """

    def __init__(self, pin_vo, pin_vLED):
        self.__pin_vo = pin_vo
        self.__pin_vLED = pin_vLED

    def get_dust(self):
        """Read the dust value

        Returns:
            dust value ug/m3
        """
        __voltage = 0
        __dust = 0
        self.__pin_vLED.write_digital(0)
        utime.sleep_us(160)
        __voltage = self.__pin_vo.read_analog() * 6.5
        utime.sleep_us(100)
        self.__pin_vLED.write_digital(1)
        __voltage = ((__voltage - 0) * 3100) / (1023 - 0) + 0
        __dust = (__voltage - 380) * 5 / 29
        if __dust < 0:
            __dust = 0
        return __dust

# Octopus Light Sensor
class LIGHT(object):
    """Ambient light sensor

    Args:
        pin
    """
    def __init__(self, pin):
        self.__pin = pin

    def get_light(self):
        """Read the illuminance

        Returns:
            illuminance 0-16000 lux
        """
        __value = self.__pin.read_analog()
        if __value <= 200:
            return ((__value - 45) * (1600 - 0)) / (200 - 45) + 0
        else:
            return ((__value - 200) * (14000 - 1600)) / (1023 - 200) + 1600

# Octopus Analog Noise Sensor                
class NOISE:
    """Sound sensor

    Args:
        pin
    """
    def __init__(self, pin):
        self.pin = pin

    def get_noise(self):
        """Read the decibel level

        Returns:
            sound decibels
        """
        level, tl, h, sum_l, sum_h = 0, 0, 0, 0, 0
        for i in range(0, 1000):
            level = level + self.pin.read_analog()
            self.pin.read_analog()
        level = level / 1000
        for i in range(0, 1000):
            voltage = self.pin.read_analog()
            if voltage >= level:
                h += 1
                sum_h = sum_h + voltage
            else:
                tl += 1
                sum_l = sum_l + voltage
        if h == 0:
            sum_h = level
        else:
            sum_h = sum_h / h
        if tl == 0:
            sum_l = level
        else:
            sum_l = sum_l / tl
        sound = sum_h - sum_l
        if sound <= 4:
            sound = ((sound - 0) * (50 - 30)) / (4 - 0) + 30
        elif sound <= 8:
            sound = ((sound - 4) * (55 - 50)) / (8 - 4) + 50
        elif sound <= 14:
            sound = ((sound - 9) * (60 - 55)) / (14 - 9) + 55
        elif sound <= 32:
            sound = ((sound - 15) * (70 - 60)) / (32 - 15) + 60
        elif sound <= 60:
            sound = ((sound - 33) * (75 - 70)) / (60 - 33) + 70
        elif sound <= 100:
            sound = ((sound - 61) * (80 - 75)) / (100 - 61) + 75
        elif sound <= 150:
            sound = ((sound - 101) * (85 - 80)) / (150 - 101) + 80
        elif sound <= 231:
            sound = ((sound - 151) * (90 - 85)) / (231 - 150) + 85
        else:
            sound = ((sound - 231) * (120 - 90)) / (1023 - 231) + 90
        return sound

# Octopus Soil Moisture Sensor   
class SOIL_MOISTURE(object):
    """Soil moisture sensor

    Args:
        pin
    """
    def __init__(self, pin):
        self.__pin = pin

    def get_soil_moisture(self):
        """Read the soil moisture percentage
        
        Returns:
            soil moisture percentage
        """
        __value = self.__pin.read_analog()
        value = ((__value - 0) * (100 - 0)) / (1023 - 0) + 0
        return 100-value

# Octopus TMP36 Temperature Sensor


# Octopus Analog UV Sensor    
class UV(object):
    """Ultraviolet sensor
    
    Args:
        pin
    """
    def __init__(self, pin):
        self.__pin = pin

    def get_uv_index(self):
        """Read the UV index
 
        Returns:
            UV index 0-15
        """
        __value = self.__pin.read_analog()
        value = ((__value - 0) * (15 - 0)) / (625 - 0) + 0
        return value

# Octopus Water Level Sensor    
class WATER_LEVEL(object):
    """Water level sensor
 
    Args:
        pin
    """
    def __init__(self, pin):
        self.__pin = pin

    def get_water_level(self):
        """Read the water level

        Returns:
            water level percentage
        """
        __value = self.__pin.read_analog()
        value = ((__value - 0) * (100 - 0)) / (700 - 0) + 0
        return value
    
# Octopus Distance Sensor
class DISTANCE(object):
    """HC_SR04 Ultrasonic Sensor

    Args:
        pin_trig (pin)
        pin_echo (pin)

    Returns:
        distance
    """

    def __init__(self, pin_d):
        self.__pin_e = pin_d
        self.__pin_t = pin_d

    def get_distance(self, unit=0):
        """基本描述

        读取距离值

        Args:
            unit (number): 检测距离单位 0 厘米 1 英尺

        Returns:
            distance: 距离
        """
        self.__pin_e.read_digital()
        self.__pin_t.write_digital(1)
        sleep_us(10)
        self.__pin_t.write_digital(0)
        ts = time_pulse_us(self.__pin_e, 1, 25000)

        distance = ts * 9 / 6 / 58
        if unit == 0:
            return distance
        elif unit == 1:
            return distance / 254