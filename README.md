
# NeoPixel skill for Snips

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/snipsco/snips-skill-hue/master/LICENSE.txt)

## Snips Skills Manager

It is recommended that you use this skill with the [Snips Skills Manager](https://github.com/snipsco/snipsskills). Simply add the following section to your [Snipsfile](https://github.com/snipsco/snipsskills/wiki/The-Snipsfile):

~~~yaml
skills:
  - package_name: snipsneopixel
    pip: https://github.com/snipsco/snips-skill-neopixel
    params:
      arduino_port: <ARDUINO_PORT>
    dialogue_events:
      - event: session_started
        action: |
          {%
          print("->>>> Session started <<<<-")
          snips.skill.listening()
          %}
      - event: session_ended
        action: |
          {%
          print("->>>> Session started <<<<-")
          snips.skill.stand_by()
          %}
~~~

## Usage

The skill allows you to control a [NeoPixel Ring 24](https://www.adafruit.com/product/1586). You can use it as follows:

~~~python
from snipsneopixel.snipsneopixel import SnipsNeopixel

neopixel = SnipsNeopixel(ARDUINO_PORT)
neopixel.loading()
~~~

 
## Copyright

This skill is provided by [Snips](https://www.snips.ai) as Open Source software. See [LICENSE.txt](https://github.com/snipsco/snips-skill-hue/blob/master/LICENSE.txt) for more
information.
