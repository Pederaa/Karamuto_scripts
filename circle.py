
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from pointClass import Point, Points

r = 10
dt = 0.1
T = 10

dtheta = 2*np.pi/(T/dt)
numberOfDots = 100

fig, ax = plt.subplots()

print("Initilizing points ...")
points = Points()
for i in range(numberOfDots):
    p = Point(r=r, phase=(i/numberOfDots)*2*np.pi)
    points.append(p)

print("Points intiilized")
print("Making animation ...")

frames = []
for t in range(int(T/dt)):
    x, y = points.get_xylist()
    line, = ax.plot(x, y, 'bo')
    frames.append([line])

    # points.addphi(dtheta)
    points.nextStep()

anim = animation.ArtistAnimation(fig, frames, interval=dt)

print("Animation completed")
print("Saving file ...")

folder = "build"
filename = "circles.mp4"

def save(filename, anim):
    anim.save(filename=filename, fps=1/dt)

try:
    save(folder + "/" + filename, anim)
except FileNotFoundError:
    import os
    os.mkdir(folder)
    save(folder + "/" + filename, anim)

print("File saved")