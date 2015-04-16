import numpy as np
import numpy.linalg as la

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
