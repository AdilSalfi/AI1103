import numpy as np
from matplotlib import pyplot as plt
from fractions import Fraction

def F(x):
  if(x<0):
    return 0

  elif(x>=0 and x<1):
    return 1/4

  elif(x>=1 and x<2):
    return 1/3

  elif(x>=2 and x<11/3):
    return 1/2

  elif(x>=11/3):
    return 1

xlist = np.linspace(-1,4,100000)
ylist = [F(x) for x in xlist]

plt.xticks([1, 0, 1, 2,3, round(11/3, 1), 4])
plt.plot(xlist, ylist)
plt.title("CDF of Random Variable X")
plt.xlabel('$x$')
plt.ylabel('$F_Xx$')
plt.show()
