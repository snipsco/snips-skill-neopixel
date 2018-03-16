from __future__ import unicode_literals
from enum import IntEnum
from serial import serial


class Animation(IntEnum):
    none, waking_up, standby, listening, error = range(5)


class Animator(object):
    def __init__(self, port, debug=False):
        self.serial = serial.Serial()
        self.serial.baudrate = 9600
        self.serial.timeout = 0.5
        self.serial.port = port
        self.debug = debug

    def open(self):
        self.serial.open()

    def close(self):
        self.serial.close()

    def run(self, animation):
        self.serial.write(bytearray([animation.value]))
        if self.debug:
            while self.serial.in_waiting:
              print('received {}'.format(self.serial.readline()))
            print('sent {}'.format(animation.name))
            print('received {}'.format(self.serial.readline()))

