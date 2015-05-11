import numpy as np
from math import *

def get_plane(p1,p2,p3):
    # Constructing the vectors in the plane
    v1 = p2 - p1
    v2 = p3 - p1
    
    # the cross product is a vector normal to the plane
    cp = np.cross(v1, v2)
    a, b, c = cp
    
    
    # This evaluates a * x3 + b * y3 + c * z3 which equals d
    d = np.dot(cp, p3)
    
    #print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))
    
    x = np.linspace(20, -20, 3)
    y = np.linspace(20, -20, 3)
    X, Y = np.meshgrid(x, y)
    
    Z = (d - a * X - b * Y) / c
    
    return a, b, c, X, Y, Z


def get_angle(a1,b1,c1,a2,b2,c2) :
    num = abs(a1*a2 + b1*b2 + c1*c2)
    dem = sqrt(a1*a1 + b1*b1 +c1*c1) * sqrt(a2*a2 + b2*b2 +c2*c2)
    angle = np.arcsin(num/dem)
    return np.degrees (angle)

