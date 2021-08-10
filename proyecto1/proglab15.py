
"""
Creado por
Mag. Leonardo Alvarez V.
Mag. Luis Fernando Alvarez V.
Mag. Hernando Alvarez R.
Fecha: Octubre 13 de 2019
"""
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
x = []
y = []
z = []
t = []
class Tridimensional():        
    def __init__(self,tope,dt,t0):        
        self.tope=tope
        self.dt = dt
        self.t0 = t0   
    def graficar(self):
        d = 0
        e = 0
        j = 1        
        def f(a,b,c):  
            return -10*a+10*b
        def g(a,b,c): 
            return 28*a-b-a*c
        def h(a,b,c): 
            return (-8/3)*c+a*b
        for i in range(1,self.tope):
            self.t0 = self.t0+self.dt
            x.append(d)
            y.append(e)
            z.append(j)
            t.append(self.t0)
            d = d + f(d,e,j)*self.dt
            e = e + g(d,e,j)*self.dt
            j = j + h(d,e,j)*self.dt
        fig=plt.figure()
        ax=fig.gca(projection='3d')
        ax.plot(x,y,z)
        ax.plot(x,y,z,'o-')
        plt.show()
def main():
    tridi=Tridimensional(10,0.10,0)
    tridi.graficar()
if __name__ == '__main__':
    main()
