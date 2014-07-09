from visual import *
import time
class Claw:
    def __init__(self, startpos):
        self.basepiece = box(pos=startpos+vector(35,0,0), size = (2,6,32), color = color.red)
        self.rightarm = box(pos=startpos+vector(25,0,16), size = (20,6,2), color = color.red)
        self.leftarm = box(pos=startpos+vector(25,0,-16), size = (20,6,2), color = color.red)
        self.rightclaw = box(pos=startpos+vector(42,0,10), size = (12,10,2), color = color.red, axis = (1,0,0.5))
        self.leftclaw = box(pos=startpos+vector(42,0,-10), size = (12,10,2), color = color.red, axis = (1,0,-0.5))
        
    def closeclaw(self):
        while round(diff_angle(self.leftclaw.axis, R.axis),1) != 0:
            self.leftclaw.rotate(angle = radians(-1), axis = (0,1,0), origin = self.leftclaw.pos - norm(self.leftclaw.axis)*3)
            self.rightclaw.rotate(angle = radians(1), axis = (0,1,0), origin = self.rightclaw.pos - norm(self.rightclaw.axis)*3)
            sleep(0.1)
    
    def openclaw(self):
        while round(diff_angle(self.leftclaw.axis, R.axis),1) < 0.8:
            self.leftclaw.rotate(angle = radians(1), axis = (0,1,0), origin = self.leftclaw.pos - norm(self.leftclaw.axis)*3)
            self.rightclaw.rotate(angle = radians(-1), axis = (0,1,0), origin = self.rightclaw.pos - norm(self.rightclaw.axis)*3)
            sleep(0.1)
            print round(diff_angle(self.leftclaw.axis, R.axis),2)
        
R = box(pos=(0,15,0), size = (50,30,30))
c=Claw(R.pos)
while True:
    c.closeclaw()
    sleep(2)
    c.openclaw()
    rate(24)