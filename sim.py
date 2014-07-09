from visual import *
import Image, time, thread, collisiondetection
from math import *
from objects import *
from variables import *
import Tkinter as tk
#from usercode import usercode





'''
#################
Usercode Function
#################
'''    

if SWARM_MODE == False:
    def usercode0():
        seen=False
        grabbed = False
        while True:
            templist = []
            markers = R.see()
            for m in markers:
                print m.marker_type
                if m.marker_type != "token arena":
                    templist.append(m)
                    print templist
            markers = templist[:]
            markers = sorted(markers, key=lambda marker: marker.distance)
            print len(markers)
            if grabbed:
                R.motors[0].speed = -10
                R.motors[1].speed = 10
                time.sleep(4)
                R.motors[0].speed = 70
                R.motors[1].speed = 70
                time.sleep(2)
                R.motors[0].speed = 0
                R.motors[1].speed = 0
                R.claw.openclaw(R.box.axis)
                time.sleep(1)
                R.motors[0].speed = -10
                R.motors[1].speed = -10
                time.sleep(3)
                R.motors[0].speed = 10
                R.motors[1].speed = -10
                time.sleep(3)
                grabbed = False
            elif len(markers)>0:
                
                angle = markers[0].bearing.y
                if angle >10 and angle <30:
                    R.motors[0].speed = -10
                    R.motors[1].speed = 10
                    time.sleep(0.2)
                elif angle < -10 and angle > -30:
                    R.motors[0].speed = 20
                    R.motors[1].speed = -20
                    time.sleep(0.2)
                elif angle <10 and angle >-10:
                    R.motors[0].speed = 30
                    R.motors[1].speed = 30
                    time.sleep(m.distance/3)
                    seen = True
            elif seen:
                R.motors[0].speed = 50
                R.motors[1].speed = 50
                time.sleep(1)
                R.motors[0].speed = 0
                R.motors[1].speed = 0
                R.claw.closeclaw(R.box.axis)
                seen=False
                grabbed = True
            else:
                R.motors[0].speed = -10
                R.motors[1].speed = 10
            

    def usercode1():
        while True:
            markers = S.see()
            print len(markers)
            S.motors[0].speed = -50.0
            S.motors[1].speed = -50.0
            time.sleep(2)
            S.motors[0].speed = 50.0
            S.motors[1].speed = -50.0
            time.sleep(0.5)

    def usercode2():
        while True:
            markers = T.see()
            print len(markers)
            T.motors[0].speed = -50.0
            T.motors[1].speed = -50.0
            time.sleep(2)
            T.motors[0].speed = 50.0
            T.motors[1].speed = -50.0
            time.sleep(0.5)

    def usercode3():
        while True:
            markers = S.see()
            print len(markers)
            U.motors[0].speed = -50.0
            U.motors[1].speed = -50.0
            time.sleep(2)
            U.motors[0].speed = 50.0
            U.motors[1].speed = -50.0
            time.sleep(0.5)


if SWARM_MODE == True:
    def usercode(number):
        while True:
            robot_list[number].motors[0].speed = -50.0
            robot_list[number].motors[1].speed = 50.0
            markers = R.see()
    



   

     
'''
#############################
Movement update and collision
#############################
'''

if __name__ == "__main__":
    
    for x in xrange(41,41+NUMBER_OF_TOKENS):
        token_list.append(Token(x))
        print len(token_list)
        for thing in token_list[x-41].markers:
            marker_list.append(thing)
    
    
    if SWARM_MODE == False:
        R = Robot(0,15,0)
        #S = Robot(-150,15,-150)
        #T = Robot(150,15,-150)
        #U = Robot(-150,15,150)
        thread.start_new_thread(usercode0,())
        #thread.start_new_thread(usercode1,())
        #thread.start_new_thread(usercode2,())
        #thread.start_new_thread(usercode3,())
        while True:
            rate(RATE)
            R.update()
            #S.update()
            #T.update()
            #U.update()
    if SWARM_MODE == True:
        for x in xrange(SWARM_NUMBER):
            robot_list.append(Robot(random.randint(-150,150),15,random.randint(-150,150)))

        counter = 0
        while counter < SWARM_NUMBER:
            counter2 = counter
            thread.start_new_thread(usercode,(counter,))
            counter +=1

        while True:
            rate(RATE)
            for r in robot_list:
                r.update()

