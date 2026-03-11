
import numpy as np
import cmath

import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Point:
    def __init__(self, r=1, phase=0.0) -> None:
        self.r = r
        self.phase = phase
    
    def get_xypoint(self):
        temp = [self.r*cmath.exp(1j*self.phase).real, 
                self.r*cmath.exp(1j*self.phase).imag]
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

r = 10
dt = 0.1
T = 4

dtheta = 2*np.pi/(T/dt)
numberOfDots = 7

fig, ax = plt.subplots()

points = Points()
for i in range(numberOfDots):
    p = Point(r=r, phase=(i/numberOfDots)*2*np.pi)
    points.append(p)


frames = []
for t in range(int(T/dt)):
    x, y = points.get_xylist()
    line, = ax.plot(x, y, 'bo')
    frames.append([line])

    print((x[0], y[0]))

    points.addphi(dtheta)

anim = animation.ArtistAnimation(fig, frames, interval=dt, repeat=False)

folder = "build"
filename = "circles.gif"
try:
    anim.save(filename=folder + "/" + filename, writer="pillow")
except FileNotFoundError:
    import os
    os.mkdir(folder)

    anim.save(filename=folder + "/" + filename, writer="pillow")
