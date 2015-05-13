# Importing required libraries
import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from math import *
from performance_strokes import *
from check_angle_jitter import *
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
ax.view_init(elev=40., azim=-90)
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
txt = fig.suptitle('Knife-Honing Rod Jitter')

pause = False

def init():
    line.set_data([0,0],[0,0])
    line.set_3d_properties([0,data[0]['z'][0]])
    line.set_color('g')
    for i in range(peaks[0][0], peaks[0][1]):
        ax.scatter(data[0]['x1'][peaks[0][0] + i], data[0]['y1'][peaks[0][0] + i], data[0]['z1'][peaks[0][0] + i], c = 'g')
    #ax.scatter(left_stroke[0], left_stroke[1], left_stroke[2], c = 'g')
    return line,


def animate(i,offset, colors,data):
    if not pause:
        ax.plot([0,0],[0,0], zs = [0,data[0]['z'][0]], c = 'g')
        line.set_data([0,data[1]['x'][i]],[0,data[1]['y'][i]])
        line.set_3d_properties([0,data[1]['z'][i]])
        line.set_color(colors[1][0][i])
        ax.scatter(data[1]['x1'][offset + i], data[1]['y1'][offset + i], data[1]['z1'][offset + i], c = 'b')
        return line,

def key_press(event):
    if event.key == 'x':
        global pause
        pause ^= True


mng = plt.get_current_fig_manager()
#mng.resize(*mng.window.maxsize())
mng.full_screen_toggle()

line, = ax.plot([],[],[])


files = []
files.append(['Expert Session02.csv', 29])
files.append(['LiveDataFile.csv', 1])


flag = []
colors = []
data = []
frames = []
peaks = []
troughs = []

for i in range(len(files)):
    p, t = divide_strokes(files[i][0], files[i][1])
    #print peaks, troughs
    d = np.genfromtxt(files[i][0], delimiter=',', skip_header=files[i][1],
                         names=['a','x1', 'y1', 'z1','x2', 'y2', 'z2','x3', 'y3', 'z3',
                                'x4', 'y4', 'z4','x5', 'y5', 'z5','x6', 'y6', 'z6','x', 'y', 'z'])
                                
    f, color = check_jitter(d, p, t)
    flag.append(f)
    colors.append(color)
    data.append(d)
    peaks.append(p)
    troughs.append(t)


for i in range(len(peaks[1])):
    frames.append(troughs[1][i] - peaks[1][i])


if flag[1]:
    # adjust the view so we can see the point/plane alignment
    
    honing_rod_line, = ax.plot([],[],[])
    fig.canvas.mpl_connect('key_press_event', key_press)
    line_ani = animation.FuncAnimation(fig, animate, min(frames), init_func=init, fargs =(peaks[1][0],colors,data), repeat=True, blit=False)
    plt.show()
