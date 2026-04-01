import cmath
import numpy as np
import random
import time
class Point:
    def __init__(self, r=1, phase=0.0) -> None:
        self.r = r
        self.phase = phase

        # Karamuto paramaters
        self.naturalFrequency = 0.02
        self.K = 0.002
    
    def get_xypoint(self):
        temp = [self.r*cmath.exp(1j*self.phase).real, 
                self.r*cmath.exp(1j*self.phase).imag]
        return temp
    
    def addphi(self, d_phi):
        self.phase += d_phi
    
    def nextStepKaramuto(self, allpoints):
        dphi = self.naturalFrequency
        for point in allpoints:
            dphi += self.K*np.sin(point.phase - self.phase)

        self.addphi(dphi)


class Points(list):
    def initilize_position(self, model, type="uniform"):
        match type.lower():
            case "uniform":
                # dtheta = 2*np.pi/(model.T/model.dt)
                for i in range(model.numberOfDots):
                    p = Point(r=model.r, phase=(i/model.numberOfDots)*2*np.pi)
                    self.append(p)

            case "random":
                random.seed(time.time())
                for i in range(model.numberOfDots):
                    p = Point(r=model.r, phase=random.random()*2*np.pi)
                    self.append(p)
            case _:
                raise TypeError(f"Unrecognised initial position type: {type}")
            
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
    
    def nextStep(self):
        for point in self:
            point.nextStepKaramuto(self)
