from visual import *
import math, Image, time, robot, usercode, thread

im = Image.open('libkoki.png')  
im2 = Image.open('floor.png') 

tex = materials.texture(data=im, mapping='sign')
tex2 = materials.texture(data=im2, mapping='sign')

lamp = local_light(pos=(200,300,200), color=color.white)

color.brown = (0.38,0.26,0.078)
color.orange = (0.85,0.54,0.18)

#width and height
#0-400

marker_list = []
player_position = vector(1,2,3)

LENGTH = 400
WIDTH = 400
HEIGHT = 50
RATE = 50

#creates arena
arenafloor = box(pos=(0,0,0), size=(4,WIDTH,LENGTH), color=color.orange, material = tex2, axis=(0,1,0))
areawall1 = box(pos=(-WIDTH/2,HEIGHT/2,0), size=(4,HEIGHT,LENGTH), color=color.orange)
areawall2 = box(pos=(WIDTH/2,HEIGHT/2,0), size=(4,HEIGHT,LENGTH), color=color.orange)
areawall3 = box(pos=(0,HEIGHT/2,-LENGTH/2), size=(WIDTH,HEIGHT,4), color=color.orange)
areawall4 = box(pos=(0,HEIGHT/2,LENGTH/2), size=(WIDTH,HEIGHT,4), color=color.orange)



#the marker object creates one "Marker" that represents one paper marker that we stick on the side of a "token".
#For the Boxes look at the "Token" Object
class Marker(object):
    def __init__(self,code,x,y,z,axis_decider,marker_type):
        global player_position
        self.x = x
        self.y = y
        self.z = z
        self.pos = vector(self.x,self.y,self.z)

        self.axis = vector(int(axis_decider[0]),int(axis_decider[1]),int(axis_decider[2]))

        self.marker_type = marker_type
        if self.marker_type == "token marker":
            self.size = 9
        elif self.marker_type == "token arena":
            self.size = 40
        print self.axis
        self.marker = box(pos=self.pos, size=(0.01,self.size,self.size), color=color.white,material=tex,axis = self.axis)



        self.angle = 0
        self.angle_rad = math.radians(self.angle)
        self.distance = math.sqrt((self.pos.x -player_position.x)**2 + (self.pos.y -player_position.y)**2 + (self.pos.z -player_position.z)**2)
        self.code = code



class Token(object):
    def __init__(self,code):
        global player_position
        self.x = random.randint((-WIDTH/2)+11,WIDTH/2-11)
        self.z = random.randint((-LENGTH/2)+11,LENGTH/2-11)
        self.pos = vector(self.x,7,self.z)
        self.size = 10
        self.box = self.marker = box(pos=self.pos, size=(self.size,self.size,self.size), color=color.brown)

        self.markers = [Marker(code,self.x-5,7,self.z,(-1,0,0),"token marker"),
                        Marker(code,self.x+5,7,self.z,(1,0,0),"token marker"),
                        Marker(code,self.x,7,self.z-5,(0,0,-1),"token marker"),
                        Marker(code,self.x,7,self.z+5,(0,0,1),"token marker"),
                        Marker(code,self.x,2,self.z,(0,-1,0),"token marker"),
                        Marker(code,self.x,12,self.z,(0,1,0),"token marker")]



        self.angle = 0
        self.angle_rad = math.radians(self.angle)
        self.pos = vector(self.x,7,self.z)
        #self.token.rotate(angle = self.angle_rad,axis=(0,1,0),origin = self.pos)
        self.code = code


class Robot(robot.Robot):
    def __init__(self,x,y,z):
        robot.Robot.__init__(self)
        self.x = x
        self.y = y
        self.z = z
        self.velocity = vector(0,0,0)
        self.pos = vector(self.x,self.y,self.z)
        self.box = box(pos=self.pos, size=(50,30,30), color=color.blue)


def populate_walls(Tokens_per_wallx,Tokens_per_wallz):
    spacingx = WIDTH/(Tokens_per_wallx+1)
    spacingz = LENGTH/(Tokens_per_wallz+1)
    #xwall1
    counter = 0
    xpos = -WIDTH/2
    ypos = HEIGHT/2
    zpos = LENGTH/2+4
    while counter <=Tokens_per_wallx:
        xposnew = xpos + (counter * spacingx)
        if counter > 0:
            box = Marker(2,xposnew,ypos,zpos-6,(0,0,-1),"token arena")
        counter +=1

    while counter <=Tokens_per_wallx+Tokens_per_wallz:
        zposnew = zpos - ((counter-Tokens_per_wallx) * spacingz)
        if counter > Tokens_per_wallx:
            box = Marker(2,xpos+2,ypos,zposnew,(1,0,0),"token arena")
        counter +=1

    while counter <=((Tokens_per_wallx*2)+Tokens_per_wallz):
        xposnew = xpos + ((counter-Tokens_per_wallx-Tokens_per_wallz) * spacingz)
        if counter > Tokens_per_wallx+Tokens_per_wallz:
            box = Marker(2,xposnew+2,ypos,zpos-LENGTH,(0,0,1),"token arena")
        counter +=1

    while counter <=(Tokens_per_wallx+Tokens_per_wallz)*2:
        zposnew = zpos - ((counter-Tokens_per_wallx-Tokens_per_wallz-Tokens_per_wallx) * spacingz)
        if counter > Tokens_per_wallx+Tokens_per_wallz+Tokens_per_wallx:
            box = Marker(2,xpos+WIDTH-2,ypos,zposnew,(-1,0,0),"token arena")
        counter +=1

#Special Cases
#If either motor is zero, speeddiff = 1 or -1
#If one motor forward and one back and equal, pivot = box position
#If both negative 
def runsim():
    for x in xrange(41,50):
        marker_list.append(Token(x))
    populate_walls(5,5)
    global R
    R = Robot(0,15,0)
    R.motors[0].speed = 0.0
    R.motors[1].speed = 0.0
    thread.start_new_thread(updatemotion,())
    
    while True:
        rate(100)
        sleep(1)
        R.motors[0].speed = 50.0
        R.motors[1].speed = 50.0
        sleep(4)
        R.motors[0].speed = 0.0
        R.motors[1].speed = 0.0
        R.motors[0].speed = -50.0
        R.motors[1].speed = 50.0
        sleep(2)
        R.motors[0].speed = 0.0
        R.motors[1].speed = 0.0
        R.motors[0].speed = -50.0
        R.motors[1].speed = -50.0
        sleep(2)
        R.motors[0].speed = 0.0
        R.motors[1].speed = 0.0
        R.motors[0].speed = 50.0
        R.motors[1].speed = -50.0
        
        
def updatemotion():
    
    oldspeed1 = 1.0
    oldspeed2 = 1.0
    while True:
        global R
        if oldspeed1 != R.motors[0].speed or oldspeed2 != R.motors[1].speed:
            oldspeed1 = R.motors[0].speed
            oldspeed2 = R.motors[1].speed
            print "stuff"
            pivot = vector(R.box.axis.z,0,-R.box.axis.x)
            pivot = norm(pivot)
            averagespeed = (abs(R.motors[0].speed) + abs(R.motors[1].speed))/2
            speeddiff = (R.motors[0].speed - R.motors[1].speed)/100
            if speeddiff == 0:
                speeddiff += 0.000000001
            if (R.motors[0].speed < 0.1 and R.motors[0].speed > -0.1):
                speeddiff = 1
            elif (R.motors[1].speed < 0.1 and R.motors[1].speed > -0.1):
                speeddiff = -1
            pivot = pivot * R.box.size.z/2 / speeddiff
            radius = mag(pivot)
            if (R.motors[0].speed > 0 and R.motors[1].speed < 0) or (R.motors[0].speed < 0 and R.motors[1].speed > 0):
                pivot = R.box.pos
                radius = R.box.size.z
            if R.motors[1].speed>R.motors[0].speed:
                print "bigger than"
                radius = radius*-1
            if R.motors[0].speed < 0 and R.motors[1].speed < 0:
                averagespeed = -averagespeed
            print averagespeed
            angularvelocity = averagespeed/radius
        if R.box.pos.x > -WIDTH/2 and R.box.pos.x < WIDTH/2 and R.box.pos.z < LENGTH/2 and R.box.pos.z > -LENGTH/2:
            R.box.rotate(angle=angularvelocity/RATE, axis=(0,1,0), origin = pivot )
                
        else:
            print R.box.pos
        wait(0.02)    
if __name__ == "__main__":
    runsim()
