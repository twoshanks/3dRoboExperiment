import os,sys
import time

class Servo(object):
    def __init__(self, which_servo, angle = 0):
        self._angle = angle;
        self._servo_no = which_servo

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
    	self._angle = value
      
    @angle.deleter
    def angle(self):
        del self._angle
