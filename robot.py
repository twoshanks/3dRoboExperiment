import servo
import motor
import time
import random
import os,sys


'''
Created By Adam Ferguson (@robo_python) 2013
In subsequent uses orginal creator must be credited
but released as opensource software
'''




'''
###BOARD CODES###
1-Servos
2-Motors
3-Output - Digital
4-Input - Analog
5-Input - Digital
#################
'''

round_length = 180

class Robot(object):
	def __init__(self):
		self.zone = 0
		self.mode = "dev"
		global ser
		self.servos = [ servo.Servo(0,0),
				servo.Servo(1,0),
				servo.Servo(2,0),
				servo.Servo(3,0),
				servo.Servo(4,0),
				servo.Servo(5,0),
				servo.Servo(6,0),
				servo.Servo(7,0)]

		self.motors = [	motor.Motor(0,0),
				motor.Motor(1,0),
				motor.Motor(2,0),
				motor.Motor(3,0)]

		print "SWITCHES ON"

		'''
		while True:
			a = self.staff_inputs[0].d
			b = self.staff_inputs[1].d
			c = self.staff_inputs[2].d
			if a == True:
				if self.zone <= 2:
					self.zone +=1
				elif self.zone == 3:
					self.zone = 0
				print "Your zone is:" + str(self.zone)
			
			if b == True:
				if self.mode == "dev":
					self.mode = "comp"
				elif self.mode == "comp":
					self.mode = "dev"
				print "Your mode is:" + self.mode
			
			if c == True:
				print "Starting User Code..."
				break
		'''
		def Timer_exit(round_length):
			while True:
				time.sleep(round_length)
				print "END OF ROUND, NOW EXITING CODE."
				thread.interrupt_main()

		if self.mode == "comp":
			thread.start_new_thread(Timer_exit,(round_length))

