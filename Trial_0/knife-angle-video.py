# Importing required libraries
import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import subprocess
from math import *
from performance_strokes import *
from check_angle import *
import time


import time
class Video(object):
    def __init__(self,path):
        self.path = "C:/Program Files (x86)/QuickTime/QuickTimePlayer.exe"
    
    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"




pause = False

files = []
files.append(['/Users/urmi/Desktop/PythonPrograms/Expert Session02.csv', 29])
files.append(['/Users/urmi/Desktop/PythonPrograms/Participant021.csv', 29])

flag = []


for i in range(len(files)):
    peaks, troughs = divide_strokes(files[i][0], files[i][1])
    #print peaks, troughs
    data = np.genfromtxt(files[i][0], delimiter=',', skip_header=files[i][1],
                         names=['a','b','x1', 'y1', 'z1','x2', 'y2', 'z2','x3', 'y3', 'z3',
                                'x4', 'y4', 'z4','x5', 'y5', 'z5','x6', 'y6', 'z6','x', 'y', 'z'])
                                
    f, x, y, z, a = check_angle(data, peaks, troughs)
    flag.append(f)


#print (angle)

if flag[1]:
    # adjust the view so we can see the point/plane alignment
    subprocess.Popen(["open", "/Users/urmi/code/master_thesis_2015/Trial_0/knife-angle.mp4"])