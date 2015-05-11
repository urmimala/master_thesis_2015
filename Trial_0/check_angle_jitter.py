import numpy as np
from angle_plane_calculation import *


def check_angle(data,peaks,troughs):
    points = []
    points.append(peaks[0])
    points.append(peaks[0] + (peaks[0] + troughs[0])/2)
    points.append(troughs[0])
    X = []
    Y = []
    Z = []
    angle = []
    flag = False
    
    for i in range(3):
        k_p1 = np.array([data['x1'][points[i]], data['y1'][points[i]], data['z1'][points[i]]])
        k_p2 = np.array([data['x2'][points[i]], data['y2'][points[i]], data['z2'][points[i]]])
        k_p3 = np.array([data['x3'][points[i]], data['y3'][points[i]], data['z3'][points[i]]])
        
        a1,b1,c1,k_X,k_Y,k_Z = get_plane(k_p1, k_p2, k_p3)
        
        knife_angle = get_angle(a1,b1,c1,data['x'][points[i]],data['y'][points[i]],data['z'][points[i]])
        X.append(k_X)
        Y.append(k_Y)
        Z.append(k_Z)
        angle.append("Knife-Honing Rod Angle - " + str(knife_angle) + " degrees")
        if knife_angle > 20 and flag == False:
            flag = True
    #print (flag, X, Y, Z, angle)
    return flag, X, Y, Z, angle

def check_jitter(data,peaks,troughs):
    color = []
    flag = False
    for i in range(len(peaks)):
        color.append([])
        for num in range(peaks[i], troughs[i]):
            if data['x'][num] > 22  or data['x'][num] < -2 or data['y'][num] > -3 or data['y'][num] < -24 or data['z'][num] > 428 or data['z'][num] < 426:
                color[i].append('r')
                if flag == False:
                    flag = True
            else:
                color[i].append('b')

    return flag, color