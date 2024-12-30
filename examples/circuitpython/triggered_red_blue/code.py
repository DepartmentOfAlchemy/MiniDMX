import doa_dmx
import board
from digitalio import DigitalInOut, Direction, Pull
import asyncio

# Define the pins
TX_PIN = board.TX
DIRECTION_PIN = board.D4
TRIGGER = board.A3

trigger = DigitalInOut(TRIGGER)
trigger.direction = Direction.INPUT
trigger.pull = Pull.UP

# Create the DMX universe
universe = doa_dmx.universe(DIRECTION_PIN, TX_PIN, 6)

print("Sending DMX messages")

async def loop():
    cur_trigger = -1
    while True:
        if trigger.value:
            # NOT triggered
            if (trigger.value != cur_trigger):
                print("Released")
            # red
            universe.set_channels({1: 255, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})
        else:
            # triggered
            if (trigger.value != cur_trigger):
                print("Triggered")
            # blue
            universe.set_channels({1: 0, 2: 0, 3: 255, 4: 0, 5: 0, 6: 0})

        cur_trigger = trigger.value

        await asyncio.sleep(.01)

asyncio.run(loop())