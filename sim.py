from visual import *
import Image, time, robot, usercode, thread
from math import *

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
RATE = 100

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

'''
New version calculates moment caused by each motor
'''
   
    
#function contains usercode as it appears visual must run in main thread 
def usercode():
    while True:
        R.motors[0].speed = 30.0
        R.motors[1].speed = 50.0
        time.sleep(2)
        R.motors[0].speed = 50.0
        R.motors[1].speed = 10.0
        time.sleep(2)
        R.motors[0].speed = -50.0
        R.motors[1].speed = 50.0
        time.sleep(1)
        R.motors[0].speed = -100.0
        R.motors[1].speed = -100.0
        time.sleep(5)

def shortest_distance(stick1, stick2, div):
    print "1"
    # To find the top and bottom point of the sticks
    stick1_top=stick1.box.pos+(stick1.box.axis)/2
    stick1_bot=stick1.box.pos-(stick1.box.axis)/2
    stick2_top=stick2.box.pos+(stick2.box.axis)/2
    stick2_bot=stick2.box.pos-(stick2.box.axis)/2
    point=stick1_top #Assuming top point of stick1 has the smallest distance from the center of stick2
    ref_point=stick2_bot #Assigning the bottom point of stick2 as the reference point
    ref_vec=stick2.box.axis #Assigning the asix of stick2 as the reference vector

    #Assigns the distance between the top point of stick1 and center of stick2 to the variable small

    small =math.hypot(stick1_top.x-stick2.box.pos.x, stick1_top.z-stick2.box.pos.z)

    # The following if statements check if the distance from the selected point of one stick to the center of          #another stick is smaller than the small
    # If it is smaller, then it changes the value of variable point and variable small
    # It also changes the reference point to bottom point of stick1 and the reference vector to axis of stick1      #if the smallest distance is from a point in stick2

    if math.hypot(stick1_bot.x-stick2.box.pos.x,stick1_bot.z-stick2.box.pos.z)< small:
        point=stick1_bot
        small= math.hypot(stick1_bot.x-stick2.box.pos.x,stick1_bot.z-stick2.box.pos.z)

    if math.hypot(stick2_bot.x-stick1.box.pos.x,stick2_bot.z-stick1.box.pos.z)< small:
        point=stick2_bot
        ref_point=stick1_bot
        ref_vec=stick1.box.axis
        small= math.hypot(stick2_bot.x-stick1.box.pos.x,stick2_bot.z-stick1.box.pos.z)

    if math.hypot(stick2_top.x-stick1.box.pos.x,stick2_top.z-stick1.box.pos.z)< small:
        point=stick2_top
        ref_point=stick1_bot
        ref_vec=stick1.box.axis
        small=math.hypot(stick2_top.x-stick1.box.pos.x,stick2_top.z-stick1.box.pos.z)

     # This loop divides the reference vector into 100 sub-vectors gradually increasing in length from the              #reference point
     # The distance between the variable point and every single point found after adding the sub-vectors to        #the reference point is calculated
     # The smallest distance found is kept in the variable small

    while div <=1:
        a=ref_vec*div
        point2=ref_point+a
        length=math.hypot(point.x-point2.x, point.z-point2.z)

        if length<small:
            small=length

        div=div+0.01
    print small
    return small # Returns the smallest distance between the variable point and the axis of the other stick
     
#sim code is here
if __name__ == "__main__":
    for x in xrange(41,50):
        marker_list.append(Token(x))
        populate_walls(5,5)
    global R
    R = Robot(0,15,0)
    thread.start_new_thread(usercode,())
    while True:
        #Goes a bit wonky without the prints, not sure why
        #print "looping"
        rate(RATE)
        #Calculates turning effect of each motor and uses them to make a turn
        averagespeed = (R.motors[0].speed + R.motors[1].speed)/2
        velocity = norm(R.box.axis)*averagespeed/RATE
        moment0 = R.motors[0].speed
        moment1 = -R.motors[1].speed
        totalmoment = (moment0 + moment1)/RATE
        #Check for collisions with walls
        newpos = R.box.pos+velocity
        if newpos.x > (-WIDTH/2) + 30 and newpos.x < WIDTH/2 -30 and newpos.z  < LENGTH/2 -30 and newpos.z > -LENGTH/2+30:
            R.box.pos += velocity
            R.box.rotate(angle=totalmoment/RATE, axis = (0,1,0), origin = R.box.pos)
        else:
            velocity = (0,0,0)
        for markers in marker_list:
            if shortest_distance(markers, R, 0.01) < (markers.box.height/2+R.box.height/2):
                newmarkerpos = markers.box.pos + velocity
                if newmarkerpos.x > (-WIDTH/2) + 5 and newmarkerpos.x < WIDTH/2 -5 and newmarkerpos.z  < LENGTH/2 -5 and newmarkerpos.z > -LENGTH/2+5:
                    markers.box.pos += velocity
                    for things in markers.markers:
                        things.marker.pos += velocity
        #print velocity

    


