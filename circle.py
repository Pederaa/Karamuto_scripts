
import numpy as np
import cmath

import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Point:
    def __init__(self, phase=0.0) -> None:
        self.phase = phase
    
    def get_xypoint(self):
        temp = [cmath.exp(1j*self.phase).real, 
                cmath.exp(1j*self.phase).imag]
        return temp
    
    def addphi(self, d_phi):
        self.phase += d_phi


class Points(list):
    def get_xylist(self):
        x = []
        y = []

        for point in self:
            p = point.get_xypoint()
            x.append(p[0])
            y.append(p[1])
        
        return x, y
    
    def addphi(self, add_phi):
        for i in range(len(self)):
            self[i].addphi(add_phi)

r = 1
dt = 0.05
T = 4
fig, ax = plt.subplots()

points = Points()
for i in range(100):
    p = Point(phase=i/(4*np.pi))
    points.append(p)

frames = []
for t in range(int(T/dt)):
    x, y = points.get_xylist()
    line, = ax.plot(x, y, 'ro')
    frames.append([line])

    points.addphi(0.01)

anim = animation.ArtistAnimation(fig, frames, interval=dt*1000)
anim.save(filename="tmp/circles.gif", writer="pillow")