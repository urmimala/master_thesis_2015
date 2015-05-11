import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import numpy.linalg as la
from pyvicon import *
from math import *
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = []
trace_i = []
data_participant = []
color = []

def generate_lineData(dims, length, index):
    '''
        Construct lineData for animation and update
        '''
    lineData = np.empty((dims, length))
    lineData[:, 0] = [0,0,0]
    lineData[:, 1] = [data_participant['x'][index],data_participant['y'][index],data_participant['z'][index]]
    return lineData


def init():
    data_expert = np.genfromtxt('/Users/urmi/Desktop/PythonPrograms/Expert Session02.csv', delimiter=',', skip_header=29, names=['a','b','x1', 'y1', 'z1'])

    right_stroke = [data_expert['x1'][228:310],data_expert['y1'][228:310],data_expert['z1'][228:310]]
    left_stroke = [data_expert['x1'][388:450],data_expert['y1'][388:450],data_expert['z1'][388:450]]
    
    line1.set_data([0,0],[0,0])
    line1.set_3d_properties([0,440])
    line1.set_color('g')
    ax.scatter(right_stroke[0], right_stroke[1], right_stroke[2], c = 'g')
    ax.scatter(left_stroke[0], left_stroke[1], left_stroke[2], c = 'g')
    
    for i in range(len(trace_i)):
        ax.scatter(data_participant['x1'][trace_i[i]],data_participant['y1'][trace_i[i]],data_participant['z1'][trace_i[i]], c='b')
    return line1,

def animate(num) :
    '''
        Update line data for animation
    '''
    line1.set_data(data[num][0],data[num][1])
    line1.set_3d_properties(data[num][2])
    line1.set_color(color[num])
    ax.scatter(data_participant['x1'][num], data_participant['y1'][num], data_participant['z1'][num], c = 'b')
    return line1,




data_participant = np.genfromtxt('/Users/urmi/Desktop/PythonPrograms/Expert Session02.csv', delimiter=',', skip_header=29,
                                 names=['a','b','x1', 'y1', 'z1','x2', 'y2', 'z2','x3', 'y3', 'z3',
                                        'x4', 'y4', 'z4','x5', 'y5', 'z5','x6', 'y6', 'z6','x', 'y', 'z'])

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

# Creating all required data
print "HEre"

data = [generate_lineData(3, 2, index) for index in range(len(data_participant))]

line1, = ax.plot([],[],[])

for num in range(500):
    if data_participant['x'][num] > 22  or data_participant['x'][num] < -2 or data_participant['y'][num] > -3 or data_participant['y'][num] < -24 or data_participant['z'][num] > 428 or data_participant['z'][num] < 426:
        color.append('r')
    else:
        color.append('b')
    if data_participant['x1'][num] >= -30 and data_participant['x1'][num] <= 30:
        if data_participant['y1'][num] >=-20 and data_participant['y1'][num] <= 100:
            if data_participant['z1'][num] >= 30 and data_participant['z1'][num] <=280:
                trace_i.append(num)


# Creating the Animation object
anim = animation.FuncAnimation(fig, animate, 300, init_func=init, interval=5, blit=True)


plt.show()

