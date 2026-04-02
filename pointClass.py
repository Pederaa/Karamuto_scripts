import cmath
import numpy as np
import random
import time
class Point:
    def __init__(self, r=None, phase=None) -> None:
        self.r = r
        self.phase = phase

        # Karamuto paramaters
        self.naturalFrequency = 0.02
    
    def get_xypoint(self):
        temp = [self.r*np.cos(self.phase), 
                self.r*np.sin(self.phase)]
        return temp
    
    def addphi(self, d_phi):
        self.phase += d_phi

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
    
    def initilze_k(self, model, type="uniform", mu=None, sigma=None):
        self.K = np.zeros((len(self), len(self)))

        match type.lower():
            case "equal":
                for i in range(model.numberOfDots):
                    for j in range(model.numberOfDots):
                        self.K[i][j] = mu

            case "random uniform":
                random.seed(time.time())
                for i in range(model.numberOfDots):
                    for j in range(model.numberOfDots):
                        self.K[i][j] = random.random()*mu
            
            case "random gaussian":
                random.seed(time.time())
                for i in range(model.numberOfDots):
                    for j in range(model.numberOfDots):
                        self.K[i][j] = random.gauss(mu, sigma)

            case _:
                raise TypeError(f"Unrecognised initial position type: {type}")
 
    def initilize_naturalFrequencies(self, model, type="equal", mu=None, sigma=None):
        match type.lower():
            case "equal":
                for i in range(model.numberOfDots):
                    self[i].naturalFrequency = mu

            case "random uniform":
                random.seed(time.time())
                for i in range(model.numberOfDots):
                    self[i].naturalFrequency = random.random()*mu
            
            case "random gaussian":
                random.seed(time.time())
                for i in range(model.numberOfDots):
                    self[i].naturalFrequency = random.gauss(mu, sigma)

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
    
    def nextStep(self, model):
        for i in range(len(self)):
            dphi = self[i].naturalFrequency

            for j in range(len(self)):
                dphi += self.K[i][j]*np.sin(self[i].phase - self[j].phase)
            
            self[i].addphi(dphi)

    # def nextStepKaramuto(self, model, allpoints, i):
    #     dphi = self.naturalFrequency
    #     for point in allpoints:
    #         dphi += self.K*np.sin(point.phase - self.phase)

    #     self.addphi(dphi)