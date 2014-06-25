import os,sys
import serial
import time
from pykoki import *
from cv2 import *
import picamera

def width_from_code(code):
	if code <= 27:
		return 0.25 * (10.0/12.0) #0.25 is printed width, inc. white border
	else:
		return 0.093 * (10.0/12.0) 

def vision_see((WIDTH, HEIGHT) = (1280,1024), preview=True, preview_time=1):
		global marker_offsets
		params = CameraParams(Point2Df(WIDTH/2, HEIGHT/2),
								Point2Df(WIDTH, HEIGHT),
								Point2Di(WIDTH, HEIGHT))
		
		camera = picamera.PiCamera()
		camera.resolution = (WIDTH, HEIGHT)
		camera.vflip=False
		
		
		if preview:
			camera.start_preview()
			time.sleep(preview_time)
			camera.stop_preview()
		camera.capture("/media/robousb/lastpic.jpg")  
		camera.close()
		
		pic=cv2.cv.LoadImage("/media/robousb/lastpic.jpg",CV_LOAD_IMAGE_GRAYSCALE) 
		k = PyKoki()
		m = k.find_markers_fp(pic, width_from_code, params) #from basic_example.py
		for element in m:
			if 0<=element.code<=27:
				element.marker_type = "MARKER_ARENA"
			elif 28<=element.code<=31:
				element.marker_type = "MARKER_ROBOT"
			elif 32<=element.code<=40:
				element.marker_type = "MARKER_PEDESTAL"
			elif 41<=element.code<=71:
				element.marker_type = "MARKER_TOKEN"
		return m
