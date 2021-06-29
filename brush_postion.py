#Program to give a list of servo angles for given list of co-ordinates
import math
link_length = [6.0,8.0] 

#function which returns inverse kinematic angles for given position
def inverse_kinematics(position):
    joint_angles = [0,0]
    arm_end = ((float(position[0])),(float(position[1])))
    try:
        joint_angles[1] = math.acos(float((arm_end[0]*arm_end[0])+(arm_end[1]*arm_end[1])-(link_length[0]*link_length[0])-(link_length[1]*link_length[1]))/(2*link_length[0]*link_length[1]))
        joint_angles[0] = math.atan(float(arm_end[1])/arm_end[0]) - math.atan(float(link_length[1]*math.sin(joint_angles[1]))/(link_length[0] + (link_length[1]*math.cos(joint_angles[1]))))
    except:
        pass
    
    joint_angles[0] = int(round(math.degrees(joint_angles[0])))
    joint_angles[1] = int(round(math.degrees(joint_angles[1]))) + 90 
    if joint_angles[0] < 0:
        joint_angles[0] =  -joint_angles[0]
        joint_angles[1] = 180 - joint_angles[1]
    return joint_angles

# used to set up the path variables (parabola/elipse) and define list acc. to that
def path_shape(arg):
    if arg is "parabola":
        pass
    elif arg is "elipse":
        pass

# returns servo angles in list/array format 
def path_angles():
    pass


#for elipse
arr = [9, 10, 11, 12, 13]

for i in arr:
    pos = ( 6 , i )
    print((inverse_kinematics(pos)))
