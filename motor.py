import os,sys
import time

class Motor(object):
    def __init__(self, which_motor, speed = 0):
        global ser
        self._speed = speed;
        self._motor_no = which_motor
        

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
        
        if self._speed <=100 and self._speed >= -100:
            if self._speed == 0:
                self.speed=0.000000001
            speed_float = float(self._speed)
            speed_fraction=  speed_float/100.00
            nearest_number_speed = round(speed_fraction *255.0,0)
            int_speed = int(nearest_number_speed)
                  
        elif self._speed >100 or self._speed < -100:
            print "CODE EXITED with ERROR 3: Motor Speed not in range from -100-100"
            sys.exit()

    @speed.deleter
    def speed(self):
        del self._speed
