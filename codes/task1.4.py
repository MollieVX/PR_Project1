import pylab
from numpy import array, linalg, random, sqrt, inf
import matplotlib.pyplot as plt

def plotUnitCircle(p):
 """ plot some 2D vectors with p-norm < 1 """
 for i in range(5000):
  x = array([random.rand()*2-1,random.rand()*2-1])
  if linalg.norm(x,p) < 1:
    pylab.plot(x[0],x[1],'ro')
 pylab.axis([-1, 1, -1, 1])
 pylab.show()

plotUnitCircle(0.5)