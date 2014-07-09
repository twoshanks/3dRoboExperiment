#Separating Axis Theorem
#Identifies the positions of the bottom corners of a box
#Projects corner positions on arbitrary axis and returns max and minpoint values
from visual import *

def findMaxMin(box, projection_axis):
    side1 = box.pos+norm(box.axis)*(box.length/2)
    side2 = box.pos+norm(vector(box.axis.z,0,-box.axis.x))*(box.width/2)
    corner1 = box.pos+((side1-box.pos)+(side2-box.pos))
    corner1.y = 0
    corner2 = corner1 - norm(box.axis)*box.length
    corner3 = box.pos+((side1-box.pos)-(side2-box.pos))
    corner3.y=0
    corner4 = corner3 - norm(box.axis)*box.length
    corner_list = [corner2,corner3,corner4]
    maxpoint = corner1.dot(projection_axis)
    maxcorner = corner1
    minpoint = corner1.dot(projection_axis)
    mincorner = corner1
    for corner in corner_list:
        projection = corner.dot(projection_axis)
        if projection > maxpoint:
            maxpoint = projection
            maxcorner = corner
        if projection < minpoint:
            minpoint = projection
            mincorner = corner
    return [maxpoint,minpoint]           
                
def collisiondetect(box1,box2):
    axislist = [box1.axis,vector(box1.axis.z,0,-box1.axis.x),box2.axis,vector(box2.axis.z,0,-box2.axis.x)]
    boxlist = [box1,box2]
    for i in range (3):
        maxmin = findMaxMin(box1,axislist[i])
        maxmin2 = findMaxMin(box2,axislist[i])
        if maxmin[0]<maxmin2[1] or maxmin2[0] < maxmin[1]:
            return False
    else:
        return True
