import matplotlib
matplotlib.use('TkAgg')
from angle import *
from jitter_trace_visualization import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import datetime
from socket import error as socket_error
from pyvicon import *

import sys

# Create a global variable for storing the data for the participants
data_participant = ([])
write = True
f = ""
    

def press(event):
    global data_participant
    global write, f, s
    
    print 'press', event.key,
    sys.stdout.flush()
    
    # Press 'c' for generating the file
    if event.key == 'c':
        print "In event C"
        # Create the file handle for the current participant using current time
        file_handle = "Participant" + str(datetime.datetime.now().time()) +".csv"
        f = open(file_handle,'w')

        try:
            s.startStreams(verbose=False)
            f.write ( ",".join(streams))
            f.write ("\n")
            try:
                # Wait for first data to come in
                while s.getData() is None: pass
                
                while write:
                    f.write ( ",".join(map(str,s.getData())))
                    f.write ("\n")
                    print s.getData()
                    time.sleep(0.01)
            except KeyboardInterrupt:
                raise
        except:
            file = "/Users/urmi/Desktop/PythonPrograms/Participant011.csv"
            skip_header = 29

        #Parse file to get data in array
        data_participant = np.genfromtxt('/Users/urmi/Desktop/PythonPrograms/Expert Session02.csv', delimiter=',', skip_header=skip_header,
                                 names=['a','b','x1', 'y1', 'z1','x2', 'y2', 'z2','x3', 'y3', 'z3',
                                        'x4', 'y4', 'z4','x5', 'y5', 'z5','x6', 'y6', 'z6','x', 'y', 'z'])
    if event.key == 'x':
        print "in x"
        f.close()
        s.close()
    
    if event.key == 'a':
        plt.cla	()
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        draw_angle(data_participant,fig,ax)

    if event.key == 'h':
        plt.cla()
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        draw_jitter_and_range(data_participant, fig, ax)

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
try:
    s = ViconStreamer()
    s.connect("192.168.10.1", 800)

    if len(sys.argv) > 1 and sys.argv[1] in ["-l", "--list"]:
        s.printStreamInfo()
        sys.exit(0)

    streams = s.selectStreams(["Time", "P-"])
except socket_error as serr:
    pass




plt.show()

