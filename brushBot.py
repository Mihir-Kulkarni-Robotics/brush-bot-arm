#Program that converts real time cursor position to inverse kinematic angles for robot arm 
import pygame , math 
from pygame.locals import *
position = (0,0)
link_length = [13,10]
servo_angles = [0,0]

# Function takes in X and Y co-ords from cursor position and finds the joint angles, assuming that the cursor end is where the end of the
# arm.
def inverse_kinematics(cursor_position):
    joint_angles = [0,0]
    arm_end = ((float(cursor_position[0])/40)+0.001,(float(cursor_position[1])/40)+0.001)
    try:
        joint_angles[1] = math.acos(float((arm_end[0]*arm_end[0])+(arm_end[1]*arm_end[1])-(link_length[0]*link_length[0])-(link_length[1]*link_length[1]))/(2*link_length[0]*link_length[1]))
        joint_angles[0] = math.atan(float(arm_end[1])/arm_end[0]) - math.atan(float(link_length[1]*math.sin(joint_angles[1]))/(link_length[0] + (link_length[1]*math.cos(joint_angles[1]))))
    except:
        pass
    
    joint_angles[0] = round(math.degrees(joint_angles[0]),1)
    joint_angles[1] = round(math.degrees(joint_angles[1]),1)  

    return joint_angles
    
# This block just defines all the values necessary to show the pygame window
pygame.init()
window_length = 650
running = True
rect = (255,255,255)
screen = pygame.display.set_mode((window_length,window_length))
pygame.display.set_caption("Inverse Kinematics")
font = pygame.font.Font(None,30)
text = font.render(str(servo_angles), True, rect, (0,0,0))
textRect = text.get_rect()
textRect.center = (30,30)
#

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEMOTION:
        position = event.pos                 
        servo_angles = inverse_kinematics(position)                 #calling the inverse kinematic function

    text = font.render(str(servo_angles), True, rect, (0,0,0))      #rendering the value of returned angles into text
    screen.fill((0,0,0))
    
    pygame.draw.line(screen,(0,255,0),(0,position[1]),(window_length,position[1]))  #draws the reference line for Y co-ordinate value
    pygame.draw.line(screen,(0,0,255),(position[0],0),(position[0],window_length))  #draws the reference line for X co-ordinate value
    pygame.draw.rect(screen, rect, (position[0],position[1],10,10))
    
    screen.blit(text,textRect)
    pygame.display.flip()