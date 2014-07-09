
'''
#################
Usercode Function
#################


currently using usercode from inside the sim.py too much interdepedance to seperate.



'''    

def usercode():
    while True:
        R.motors[0].speed = 50.0
        R.motors[1].speed = 50.0
        time.sleep(2)
        R.motors[0].speed = 50.0
        R.motors[1].speed = -50.0
        time.sleep(0.5)
        R.motors[0].speed = 50.0
        R.motors[1].speed = 50.0
        time.sleep(2)