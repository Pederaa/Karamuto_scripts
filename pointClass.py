import cmath
import numpy as np

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
