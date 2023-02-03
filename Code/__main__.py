#!/usr/bin/env python3

import RPi.GPIO as GPIO

class Pi():
    def __init__(self) -> None:
        """ Initialise the setup of a pi with its GPIO board for default, only the GPIO board
        Default is actually supported at this time"""
        GPIO.setmode(GPIO.BOARD)

        self.pin_status_dict = dict();

    def get_pin_status(self, id: int) -> int:
        """ Checks the Stored Table to see if the pin is currently set as an input pin,
        if it is it will read it otherwise, if it is unset or set as a reciever it will
        update it to an input pin"""

        assert id is int

        status: bool = self.pin_status_dict[id]
        if status is None:
            self.pin_status_dict.update(id,False)
            GPIO.setup(id,GPIO.IN)
        elif status is True:
            self.pin_status_dict.update(id,False)
            GPIO.setup(id,GPIO.IN)
        return GPIO.input(id)

    def set_pin_status(self, id: int, value: int) -> None:
        """ Checks the Stored table to see if the pin is currently set as an output pin,
        if i is it will send the value, othewise it will set it to a sender pin"""

        assert id is int
        assert value is int

        status: bool = self.pin_status_dict[id]
        if status is None:
            self.pin_status_dict.update(id,True)
            GPIO.setup(id,GPIO.OUT)
        elif status is True:
            self.pin_status_dict.update(id,True)
            GPIO.setup(id,GPIO.OUT)
        return GPIO.input(id)


        pass

    def __del__(self):
        """ on the Termination of this class it closes the GPIO pin"""
        GPIO.cleanup()

if __name__ is '__main__':
    print("debug mode!")
