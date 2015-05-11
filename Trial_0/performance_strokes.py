import numpy as np
from scipy.signal import argrelextrema

data = []
maxima = []

def divide_strokes(filename, skip_header):
    global data, maxima
    peaks = []
    troughs = []
    
    data = np.genfromtxt(filename, delimiter=',', skip_header=skip_header,
                         names=['a','b','x1', 'y1', 'z1','x2', 'y2', 'z2','x3', 'y3', 'z3',
                                'x4', 'y4', 'z4','x5', 'y5', 'z5','x6', 'y6', 'z6','x', 'y', 'z'])
                                
    maxima = argrelextrema(data['z1'], np.greater)
    minima = argrelextrema(data['z1'], np.less)

    #Clean out the minimas
    for i in range(len(minima[0])):
        try:
            if data['z1'][minima[0][i]] < 175 : # and minima[0][i] - minima[0][i-1] > 25:
                if i < len(minima[0]) - 1:
                    if abs(minima[0][i]-minima[0][i+1]) > 25:
                        #print (minima[0][i])
                        troughs.append(minima[0][i])
                else:
                    #print (minima[0][i])
                    troughs.append(minima[0][i])
        except:
            pass

    #Calculate the peaks from troughs
    for i in range(len(troughs)):
        if i > 0 :
            a = troughs[i-1]
            b = troughs[i]
        else:
            a = 0
            b = troughs[i]
        
        m_list = [i for i in maxima[0] if i <= b and i >= a]
        max_z = max(data['z1'][m_list])
        max_v = [ i for i, j in enumerate(m_list) if data['z1'][j] == max_z]      
        peaks.append(m_list[max_v[0]])
    
    return peaks, troughs
