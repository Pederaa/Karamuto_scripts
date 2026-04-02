import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from pointClass import Point, Points

class OneDModel:
    def __init__(self, r=10, dt=0.1, T=10, numberOfDots=100):
        self.r = r
        self.dt = dt
        self.T = T
        self.numberOfDots = numberOfDots

model = OneDModel(r=10, dt=0.03, T=10, numberOfDots=20)

fig, ax = plt.subplots()

print("Initilizing points ...")

points = Points()
points.initilize_position(model, type="uniform")
points.initilze_k(model, type="equal", mu=0, sigma=0.01)
points.initilize_naturalFrequencies(model, type="random uniform", mu=0.1, sigma=0.1)

print("Points intiilized")
print("Making animation ...")

frames = []
for t in range(int(model.T/model.dt)):
    x, y = points.get_xylist()
    line, = ax.plot(x, y, 'bo')
    frames.append([line])

    # points.addphi(dtheta)
    points.nextStep(model)

anim = animation.ArtistAnimation(fig, frames, interval=model.dt)

print("Animation completed")
print("Saving file ...")

folder = "build"
filename = "circles.mp4"

def save(filename, anim):
    anim.save(filename=filename, fps=1/model.dt)

try:
    save(folder + "/" + filename, anim)
except FileNotFoundError:
    import os
    os.mkdir(folder)
    save(folder + "/" + filename, anim)

print("File saved")