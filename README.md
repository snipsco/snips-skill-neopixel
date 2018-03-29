
# Snips Skill NeoPixel

[![Latest Version](https://img.shields.io/pypi/v/snipsneopixel.svg)](https://pypi.python.org/pypi/snipsneopixel/)
[![Build Status](https://travis-ci.org/snipsco/snips-skill-neopixel.svg)](https://travis-ci.org/snipsco/snips-skill-neopixel)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/snipsco/snips-skill-neopixel/master/LICENSE.txt)

## Requirements
- Arduino Board
- NeoPixel Ring 24

## Configuration 
We made a library to use the Arduino board as an actuator of the Raspberry Pi. We would recommend you to use an Arduino Micro as
 it is more than enough for the purpose. Here are the steps to configure it:
- You install the Arduino IDE ([here](https://www.arduino.cc/en/Main/Software)) it will help you upload the code into the Arduino.
- Clone/Download the [Neopixel Ring library](https://github.com/adafruit/Adafruit_NeoPixel) into the Arduino library folder.
~~~
*/documents/arduino/libraries
~~~
- Clone/Download our [Snips_lights](https://github.com/snipsco/Snips_Lights) library into the same Arduino library folder
~~~
Note: if you have Arduino running, you would need to restart it for the libraries to load and show under the Examples menu. 
~~~
- Open the **Snips_lights** library example called home:

![snips-lights](https://cdn-images-1.medium.com/max/1600/1*IdSEqw2EKfpqtosr0R8DCQ.png)

- Plug your Arduino board 
- Pick your Arduino board under **Tools > Board** and upload the example via the Arduino IDE.

## Mount
In order to see the NeoPixel reacting to voice you will need to solder it with the Arduino board first. Here we show you with 
an Arduino Micro: 
- First you need to solder the Neopixel ring and the Arduino Micro. Start to solder red and black wire to the 5V and Gnd pins 
of the Neopixel Ring then solder a color wire to Data pin.

![soldering-step-1](https://cdn-images-1.medium.com/max/1600/1*jpGKItzakYWYZ93PUD2dvA.png)

- Then solder the red and black wire to the 5V and GND of the Arduino Micro, and the Data on pin 6.

![soldering-step-2](https://cdn-images-1.medium.com/max/1600/1*JEN1Lfyit8FXiz-HMNzxnw.png)

## Snips Manager

It is recommended that you use this skill with the [Snips Manager](https://github.com/snipsco/snipsmanager). Simply add the following section to your [Snipsfile](https://github.com/snipsco/snipsmanager/wiki/The-Snipsfile):

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


On your Pi the `<ARDUINO_PORT>` should be `/dev/ttyACM0` but we can double check the connection as follows:
- Plug Arduino to Raspberry Pi using the proper USB cable
- Run `ls /dev/tty*` on your Raspberry Pi terminal. The result should be content 
`/dev/ttyACM0` which will mean that you are good.

## Usage

You can use the NeoPixel skill as follows:

~~~python
from snipsneopixel.snipsneopixel import SnipsNeopixel

neopixel = SnipsNeopixel(<ARDUINO_PORT>)
neopixel.loading()
~~~

## Contributing

Please see the [Contribution Guidelines](https://github.com/snipsco/snips-skill-neopixel/blob/master/CONTRIBUTING.md).

## Copyright

This skill is provided by [Snips](https://www.snips.ai) as Open Source software. See [LICENSE.txt](https://github.com/snipsco/snips-skill-neopixel/blob/master/LICENSE.txt) for more
information.
