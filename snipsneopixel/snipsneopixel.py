# -*-: coding utf-8 -*-
""" Neopixel skill for Snips. """

from __future__ import unicode_literals
from lights import Animator, Animation
import atexit


class SnipsNeopixel:
    """NeoPixel skill for Snips."""

    def __init__(self, arduino_port='/dev/ttyACM0', debug=False, locale=None):
        try:
            print(arduino_port)
            self.animator = Animator(arduino_port, debug)
            self.animator.open()
            self.animator.run(Animation.waking_up)
            atexit.register(self.close)
        except Exception as ex:
            print(ex)
            self.animator = None
            pass

    def stand_by(self):
        self.animator.run(Animation.standby)

    def listening(self):
        self.animator.run(Animation.listening)

    def waking_up(self):
        self.animator.run(Animation.waking_up)

    def error(self):
        self.animator.run(Animation.error)

    def none(self):
        self.animator.run(Animation.none)

    def close(self):
        self.none()
        self.animator.close()



