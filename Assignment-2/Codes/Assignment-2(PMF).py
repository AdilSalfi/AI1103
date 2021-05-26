#Plot for PMF
import numpy as np
from matplotlib import pyplot as plt

plt.stem([0, 1, 2, round(11/3, 1)],[1/4, 1/12, 1/6, 1/2])
plt.title("Discrete Probability distribution of Random Variable X")
plt.xlabel('$X=x$')
plt.ylabel("Probability")
plt.xticks([0, 1, 2, round(11/3, 1)])
plt.yticks([1/4, 1/12, 1/6, 1/2])
plt.show()

