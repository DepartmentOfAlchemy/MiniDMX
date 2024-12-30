# Example
Example that turns a fixture to RED. When triggered the fixture turns BLUE.

It assumes a fixture with 6 channels on address 1.
The channels are:
- 1: RED Dimmer
- 2: GREEN Dimmer
- 3: BLUE Dimmer
- 4: WHITE Dimmer
- 5: AMBER Dimmer
- 6: ULTRAVIOLET Dimmer

When the trigger button is not pressed the fixture will have a 
red light. When the trigger button is pressed the fixture will
have a blue light.

## Dependencies

The `lib` directory in the repository contains the `doa_dmx.py` library that should be installed in the microcontroller's CircuitPython `lib` directory.

The other dependencies that are required in the microcontroller's CircuitPython `lib` directory are:
- asyncio
- adafruit_ticks