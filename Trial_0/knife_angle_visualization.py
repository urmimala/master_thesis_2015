import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import numpy.linalg as la
from pyvicon import *
from math import *
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

'''
def py_ang(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    return np.arctan2(sinang, cosang) * 180 / np.pi

data_expert = np.genfromtxt('/Users/urmi/Desktop/PythonPrograms/Expert Session02.csv', delimiter=',', skip_header=229, skip_footer=1486,
                            names=['a','b','x1', 'y1', 'z1','x2', 'y2', 'z2','x3', 'y3', 'z3',
                                   'x4', 'y4', 'z4','x5', 'y5', 'z5','x6', 'y6', 'z6','x', 'y', 'z'])

data_participant = np.genfromtxt('/Users/urmi/Desktop/PythonPrograms/Participant011.csv', delimiter=',', skip_header=129, skip_footer=858,
                                 names=['a','b','x1', 'y1', 'z1','x2', 'y2', 'z2','x3', 'y3', 'z3',
                                        'x4', 'y4', 'z4','x5', 'y5', 'z5','x6', 'y6', 'z6','x', 'y', 'z'])


v1 = [data_expert['x1'][0], data_expert['y1'][0], data_expert['z1'][0]]
v2 = [data_expert['x'][0], data_expert['y'][0], data_expert['z'][0]]

print v1, v2

print py_ang(v1,v2)
'''

def get_plane(p1,p2,p3):
    # Constructing the vectors in the plane
    v1 = p3 - p1
    v2 = p2 - p1
    
    # the cross product is a vector normal to the plane
    cp = np.cross(v1, v2)
    a, b, c = cp
    
    
    # This evaluates a * x3 + b * y3 + c * z3 which equals d
    d = np.dot(cp, p3)
    
    #print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))
    
    x = np.linspace(100, -100, 3)
    y = np.linspace(100, -100, 3)
    X, Y = np.meshgrid(x, y)
    
    Z = (d - a * X - b * Y) / c
    
    return a, b, c, X, Y, Z

def get_angle(a1,b1,c1,a2,b2,c2) :
    num = abs(a1*a2 + b1*b2 + c1*c2)
    dem = sqrt(a1*a1 + b1*b1 +c1*c1) * sqrt(a2*a2 + b2*b2 +c2*c2)
    angle = np.arccos(num/dem)
    return np.degrees (angle)


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Setting the ax properties
ax.set_xlim3d([-200.0, 200.0])
ax.set_xlabel('X')

ax.set_ylim3d([-200.0, 200.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 500.0])
ax.set_zlabel('Z')

ax.invert_yaxis()
ax.invert_xaxis()


mng = plt.get_current_fig_manager()
#mng.resize(*mng.window.maxsize())
mng.full_screen_toggle()


plt.ion()
plt.show()

# Setting up the streaming

s = ViconStreamer()
s.connect("192.168.10.1", 800)

if len(sys.argv) > 1 and sys.argv[1] in ["-l", "--list"]:
    s.printStreamInfo()
    sys.exit(0)
streams = s.selectStreams(["Time", "P-"])

s.startStreams(verbose=False)

string = ""
fig_text = plt.figtext(.3,.5,  string,fontsize=30)
user_line, = ax.plot([],[],[])
ax.plot([0,0],[0,0],[0,450])

try:
    
    # Wait for first data to come in
    while s.getData() is None: pass
    
    while True:
    
        k_p1 = np.array([   s.getData()[1],s.getData()[2], s.getData()[3] ])
        k_p2 = np.array([   s.getData()[4],s.getData()[5], s.getData()[6] ])
        k_p3 = np.array([   s.getData()[7],s.getData()[8], s.getData()[9] ])

        h_p1 = np.array([   s.getData()[10],s.getData()[11], s.getData()[12] ])
        h_p2 = np.array([   s.getData()[13],s.getData()[14], s.getData()[15] ])
        h_p3 = np.array([   s.getData()[16],s.getData()[17], s.getData()[18] ])

        #print k_p1, k_p2, k_p3, h_p1, h_p2, h_p3
        
        a1,b1,c1,k_X,k_Y,k_Z = get_plane(k_p1, k_p2, k_p3)

        a2,b2,c2,h_X,h_Y,h_Z = get_plane(h_p1, h_p2, h_p3)

        angle = get_angle(a1,b1,c1,a2,b2,c2)

        #ax.plot_surface(k_X,k_Y,k_Z, color='blue')
        #ax.plot_surface(h_X,h_Y,h_Z, color='yellow')
        
        # plot the original points. We use zip to get 1D lists of x, y and z coordinates.
        #ax.plot(*zip(k_p1, k_p2, k_p3), color='r', linestyle=' ', marker='o')
        #ax.plot(*zip(h_p1, h_p2, h_p3), color='b', linestyle=' ', marker='o')
        user_line.set_data([ s.getData()[1],s.getData()[4]],[s.getData()[2],s.getData()[5]])
        user_line.set_3d_properties([s.getData()[3],s.getData()[6]])
        
        string = str(angle) + " \n " + str(90-angle)
        fig_text.set_text(string)
        plt.draw()
            
        #print s.getData()[18], " : ", s.getData()[9], "---->", angle
except KeyboardInterrupt:
    pass

