import os,sys
import serial
import time

ser = serial.Serial("/dev/ttyACM0",9600, timeout= 2)

class Servo(object):
    def __init__(self, which_servo, angle = 0):
        self._angle = angle;
        self._servo_no = which_servo
        global ser

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
    	self._angle = value
	
	if self._angle <=180:
		print "sending data"
		ser.write("1" +"," + str(self._servo_no)+"," +str(self._angle))
		self.a =ser.readline().rstrip()
		print self.a
		print self._angle
            	if not str(self.a) == str(self._angle):
                	print "CODE EXITED with ERROR 1: Serial Error"
                	#sys.exit()
        
        elif self._angle >180 or self._angle < 0:
            print "CODE EXITED with ERROR 2: Servo Position not in range from 0-180"
            sys.exit()
       

    @angle.deleter
    def angle(self):
        del self._angle
