import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib
matplotlib.use("Agg")

from pointClass import Point, Points

class OneDModel:
    def __init__(self, r=10, dt=0.1, T=10, numberOfDots=100):
        self.r = r
        self.dt = dt
        self.T = T
        self.numberOfDots = numberOfDots

model = OneDModel(r=5, dt=0.03, T=10, numberOfDots=20)

fig, ax = plt.subplots()

print("Initilizing points ...")

points = Points()
points.initilize_position(model, type="random")
points.initilze_k(model, type="random gaussian", mu=0.5, sigma=0.01)
points.initilize_naturalFrequencies(model, type="equal", mu=0.1, sigma=0.1)

print("Points intiilized")
print("Making animation ...")

x, y = points.get_xylist()
scat = ax.scatter(x, y, c=points.colors, s=50)
ax.set(xlim=[-model.r*1.1, model.r*1.1], ylim=[-model.r*1.1, model.r*1.1])

def update(frame):
    ax.clear()
    points.nextStep(model)
    x, y = points.get_xylist()
    scat = ax.scatter(x, y, c=points.colors, s=50)
    ax.set(xlim=[-model.r*1.1, model.r*1.1], ylim=[-model.r*1.1, model.r*1.1])

    return (scat)

anim = animation.FuncAnimation(fig=fig, func=update, frames=int(model.T/model.dt), interval=model.dt)


print("Animation completed")
print("Saving file ...")

folder = "build"
filename = "circles.mp4"

def save(filename, anim):
    anim.save(filename=filename, fps=int(1/model.dt))

try:
    save(folder + "/" + filename, anim)
except FileNotFoundError:
    import os
    os.mkdir(folder)
    save(folder + "/" + filename, anim)

print("File saved")