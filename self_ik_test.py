import math 

end = (16.263,16.263)
link = (13,10)
theta = [0,0]

theta[1] = math.acos(float((end[0]*end[0])+(end[1]*end[1])-(link[0]*link[0])-(link[1]*link[1]))/(2*link[0]*link[1]))
#print float((end[0]*end[0])+(end[1]*end[1])-(link[0]*link[0])-(link[1]*link[1]))/(2*link[0]*link[1])
theta[0] = math.atan(float(end[1])/end[0]) - math.atan(float(link[1]*math.sin(theta[1]))/(link[0] + (link[1]*math.cos(theta[1]))))

print (math.degrees(theta[0]))
print (math.degrees(theta[1]))
