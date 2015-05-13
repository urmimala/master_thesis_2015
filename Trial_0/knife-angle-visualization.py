# Importing required libraries
import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from math import *
from performance_strokes import *
from check_angle import *
import matplotlib.animation as animation
import time


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Setting the axes properties
FLOOR = -200
CEILING = 200
ax.set_xlim3d(FLOOR, CEILING)
ax.set_ylim3d(FLOOR, CEILING)
ax.set_zlim3d(0, 500)
ax.view_init(elev=26., azim=-66)
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
txt = fig.suptitle('Knife-Honing Rod Angle')

pause = False

def animate(i,X, Y,Z, angle):
    if not pause:
        ax.clear()
        ax.set_xlim3d(FLOOR, CEILING)
        ax.set_ylim3d(FLOOR, CEILING)
        ax.set_zlim3d(0, 500)
        #ax.view_init(elev=26., azim=-66)
        ax.plot([0,0],[0,0],zs = [0,440],c ='k', linewidth = 2)
        txt.set_text(angle[1][i])
        ax.plot_surface(X[0][i],Y[0][i],Z[0][i], color='green')
        line = ax.plot_surface(X[1][i],Y[1][i],Z[1][i], color='red')
        #time.sleep(2)
        return honing_rod_line,

def key_press(event):
    if event.key == 'x':
        global pause
        pause ^= True


mng = plt.get_current_fig_manager()
#mng.resize(*mng.window.maxsize())
mng.full_screen_toggle()


files = []
files.append(['Expert Session02.csv', 29])
files.append(['LiveDataFile.csv', 1])

flag = []
X = []
Y = []
Z = []
angle = []

for i in range(len(files)):
    peaks, troughs = divide_strokes(files[i][0], files[i][1])
    #print peaks, troughs
    data = np.genfromtxt(files[i][0], delimiter=',', skip_header=files[i][1],
                         names=['a','x1', 'y1', 'z1','x2', 'y2', 'z2','x3', 'y3', 'z3',
                                'x4', 'y4', 'z4','x5', 'y5', 'z5','x6', 'y6', 'z6','x', 'y', 'z'])
                                
    f, x, y, z, a = check_angle(data, peaks, troughs)
    flag.append(f)
    X.append(x)
    Y.append(y)
    Z.append(z)
    angle.append(a)

#print (angle)

if flag[1]:
    # adjust the view so we can see the point/plane alignment
    
    honing_rod_line, = ax.plot([],[],[])
    fig.canvas.mpl_connect('key_press_event', key_press)
    line_ani = animation.FuncAnimation(fig, animate, 3, fargs =(X,Y,Z,angle), repeat=True, blit=False)
    plt.show()
