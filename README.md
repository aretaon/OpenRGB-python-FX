# OpenRGB-python-FX

## Effect List

### UI is user input, *not* gui this time. sorry

* Rainbow wave

* Spectrum cycling (cycle.py) (Credit to James Potkukelkka on discord for this one)

* Gradient cycling

* Breathing

* Ambient (credit to usrErr0r on discord for this one, Not working on linux due to ImageGrab not having an import)

* Rain (**Massive** thanks and credit to Bahorn on discord for this one)

* Cram

* Chase (Per request of Titanium on Discord)

* Rave (Basically multiple instances of rain with different colors that make a cool effect, Discovered by Saint Mischievous on discord)

If you would like a specific effect then DM me on discord (CoffeeIsLife)

## Usage

* start the openRGB sdk server, otherwise this *will not work*

* you may need to install the sdk binding ```pip install openrgb-python``` or ```pip3 install openrgb-python``` (you may also need to add --user at the end for linux)

* clone the repository or download the effect you want

* cd into the folder with the python files

* run using ```python3 file.py``` or ```python file.py```

* enjoy the effect :)

### Most effects support flags, See the table below for details

Effect (left to right), Flag (top to bottom)

|         | Ambient| Breathing | Chase | Cram | Cycle | Gradcycle | Rain | Rainbow wave | Rave|
|---------|--------|-----------|-------|------|-------|-----------|------|--------------|-----|
|C1       | No     | Yes       | Yes   | Yes  | No    | Yes       | Yes  | No           | No  |
|C2       | No     | No        | Yes   | No   | No    | Yes       | No   | No           | No  |
|Speed    | No     | Yes       | No    | No   | No    | Yes       | No   | Yes          | No  |
|Reversed | No     | No        | Yes   | No   | No    | Yes       | Yes  | Yes          | Yes |
|Only-Set | No     | Yes       | Yes   | Yes  | Yes   | Yes       | Yes  | Yes          | Yes |

* ``--C1``: AKA Color 1. Usage is ``python file.py --C1 Value(0 - 255) Value(0 - 255) Value(0-255)`` or ``python file --C1 0 0 255``

* ``--C2``: AKA Color 2. Same Usage as C1 but with a different flag

* ``--speed``: Self explanitory, It is kinda hard to implement or I am lazy so it isn't in a lot of effects. Usage is ``python file.py --speed int`` (any number is fine but I haven't tested over 50)

* ``--reversed``: Reverses effects for specific devices. Usage is ``python file.py --reversed "example device"`` or ``python file.py --reversed "device 1 , device 2`` for multiple devices. seperate the devices by `` , ``(space comma space)

* ``--only-set``: Used if you only want to apply the effect to one device. I made it a goal for all effects to use this flag. Enables all devices if the flag isn't called. Also same usage as --reversed but with a different flag

## Writing effects

Effects are stored in their own .py file for now

```python
import openrgb , time , string , colorsys , sys
from openrgb.utils import RGBColor , ModeData , DeviceType , ZoneType

client = openrgb.OpenRGBClient()

Dlist = client.devices
```

is a good starting point

## Notes

While this is system wide, there are some limitations.

if the device isn't in openRGB then the effect *will not* apply to it

currently rainbow is poorly optimized due to a lack of big brainedness on my part (I did do some optimizations that allows me to use .show() and that made it more readable for other people)

Ambient grabs the entire screen leading to some shade of white or black. hopefully this will get fixed soon

## Todo

* Make contributing easier (more templates and comments/doc strings)

* Add matrix zone support for some effects (rainbow wave and gradcycle)

* Smooth out some of the effects (rainbow wave)

* Create GUI for launching effects (most effects are built as functions so incorporating them wouldn't be that hard)
