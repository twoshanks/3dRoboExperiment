import os,sys
import serial
import time 

ser = serial.Serial("/dev/ttyACM0",9600, timeout= 2)

#arduino won't read strings as im using getint() so changed query to 1

# you can't do int(0) so as always 1 is False, 2 is True

class Input(object):
    def __init__(self, which_pin, d = False):
	global ser
        self._d = d
        self._pin_no = which_pin
	self._dinput_value = False

    @property
    def d(self):

        ser.write("7" + "," +str(self._pin_no) +","+"1")
        self._dinput_value = ser.readline().rstrip()
	self._dinput_value = ser.readline().rstrip()
	
	if str(self._dinput_value) =="1":
		self._d = False
		return self._d
	elif str(self._dinput_value) == "2":
		self._d =True
		return self._d
	
	else:
		print "CODE EXITED with ERROR ??: Arduino went funny, sorry"
		sys.exit()

       
    @d.setter
    def d(self, d):
        print "CODE EXITED with ERROR 5: You are not allowed to set input values"
        sys.exit()

    @d.deleter
    def d(self):
        del self._d
