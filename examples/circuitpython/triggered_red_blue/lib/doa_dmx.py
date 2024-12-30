"""UART based CircuitPython DMX transmitter"""
import busio
import digitalio
import time
from array import array
import asyncio

# Original inspiration from https://github.com/adafruit/circuitpython/issues/673
# Other inspiration from https://github.com/Lycee-Experimental/dmx-lxp/blob/main/ESP32-S3/dmx.py
# Further inspiration from https://github.com/sparkfun/SparkFunDMX

DMX_WRITE_DIR = 1

# Currently only supports sending DMX data, not receiving

class universe():
    def __init__(self, en, tx, max_channels):
        '''
        en: enable pin, used to set direction
        tx: transmit pin
        max_channels: the maximum number of channels to send
        '''
        self.en = en
        self.tx = tx
        self.max_channels = max_channels
        
        self.com_direction = digitalio.DigitalInOut(self.en)
        self.com_direction.direction = digitalio.Direction.OUTPUT
        self.com_direction.value = DMX_WRITE_DIR

        self.uart = digitalio.DigitalInOut(self.tx)
        self.uart.direction = digitalio.Direction.OUTPUT
        self.uart.value = 1
        self.dmx_message = array('B', [0] * (6+1))
        asyncio.create_task(self.send_dmx())

    def set_communication_direction(self, direction):
        self.com_direction.value = direction

    def set_channels(self, message):
        for ch in message:
            self.dmx_message[ch] = message[ch]

    async def send_dmx(self):
        """Send the DMX message every 100ms"""
        while True:
            # break
            self.uart.value = 0
            time.sleep(88E-6)
            # make after break
            self.uart.value = 1
            self.uart.deinit()
            time.sleep(8E-6)
            # send DMX data
            self.uart = busio.UART(tx=self.tx, rx=None, baudrate=250000, bits=8, parity=None, stop=2)
            self.uart.write(self.dmx_message)
            self.uart.deinit()
            self.uart = digitalio.DigitalInOut(self.tx)
            self.uart.direction = digitalio.Direction.OUTPUT
            self.uart.value = 1
            await asyncio.sleep(0.1)