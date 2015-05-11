# Importing all required libraries
import matplotlib
matplotlib.use('TkAgg')
from pyvicon import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

# Reading csv file for reference data
data_expert = np.genfromtxt('/Users/urmi/Desktop/PythonPrograms/Expert Session02.csv', delimiter=',', skip_header=29, names=['a','b','x1', 'y1', 'z1'])

right_stroke = [data_expert['x1'][228:310],data_expert['y1'][228:310],data_expert['z1'][228:310]]
left_stroke = [data_expert['x1'][388:450],data_expert['y1'][388:450],data_expert['z1'][388:450]]

# Attaching 3D axis to the figures
fig = plt.figure()

# Inversing the axes to match Vicon
axes = plt.gca()
axes.invert_yaxis()
axes.invert_xaxis()

# Creating subplots for different visualizations
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Creating line object for interactive plotting
user_line, = ax1.plot([],[],[])

# Plotting reference honing rod line and stroke trace
ax1.plot([0,0],[0,0],[0,450])
ax2.plot([0,0],[0,0],[0,450])
ax2.scatter(right_stroke[0], right_stroke[1], right_stroke[2], c = 'g')
ax2.scatter(left_stroke[0], left_stroke[1], left_stroke[2], c = 'g')

# Setting the ax1 properties
ax1.set_xlim3d([-200.0, 200.0])
ax1.set_xlabel('X')

ax1.set_ylim3d([-200.0, 200.0])
ax1.set_ylabel('Y')

ax1.set_zlim3d([0.0, 500.0])
ax1.set_zlabel('Z')

ax1.invert_yaxis()
ax1.invert_xaxis()
ax1.view_init(elev=23., azim=-62)

ax1.set_title('Honing Rod Stability Visualization')

# Setting the ax2 properties
ax2.set_xlim3d([-200.0, 200.0])
ax2.set_xlabel('X')

ax2.set_ylim3d([-200.0, 200.0])
ax2.set_ylabel('Y')

ax2.set_zlim3d([0.0, 500.0])
ax2.set_zlabel('Z')

ax2.invert_yaxis()
ax2.invert_xaxis()
ax2.view_init(elev=23., azim=-28)

ax2.set_title('Knife Range Visualization')

#plt.ion()

# Maximize output figure window
mng = plt.get_current_fig_manager()
#mng.resize(*mng.window.maxsize())
mng.full_screen_toggle()


plt.show()

# Setting up the streaming
s = ViconStreamer()
s.connect("192.168.10.1", 800)

if len(sys.argv) > 1 and sys.argv[1] in ["-l", "--list"]:
    s.printStreamInfo()
    sys.exit(0)
streams = s.selectStreams(["Time", "P-"])

s.startStreams(verbose=False)
x =0
y =0
z =0
try:
    
    # Wait for first data to come in
    while s.getData() is None: pass
    
    while True:
        user_line.set_data([0,s.getData()[19]],[0,s.getData()[20]])
        user_line.set_3d_properties([0,s.getData()[21]])
        user_line.set_color('r')
        
        
        if(s.getData()[1] == 0  or s.getData()[2] == 0 or s.getData()[3] == 0 ) :
            ax2.scatter(x,y,z, c = 'b')
        else:
            x = s.getData()[1]
            y = s.getData()[2]
            z = s.getData()[3]
            ax2.scatter(x,y,z, c = 'b')
        

        print s.getData()[1],s.getData()[2], s.getData()[3]
#print s.getData()[19],s.getData()[20], s.getData()[21]
        plt.draw()
        time.sleep(0.01)
except KeyboardInterrupt:
    pass

