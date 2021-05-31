import numpy as np
from matplotlib import pyplot as plt
#Theoretical Expected Value
TheoreticalE=2.25

simlen = 100000
x=[0, 1, 2, 11/3]
arr = np.random.choice(x, p = [1/4, 1/12, 1/6, 1/2], size = simlen)
count=0
i=0

while i<simlen:
  count+=arr[i]
  i+=1

#Simulated Expected Value
SimulatedE = count/simlen

print("Theoretical Expected Value is {}".format(TheoreticalE))
print("Simulated Expected Value is {}".format(SimulatedE))

y=np.array([SimulatedE])
z=np.array([TheoreticalE])

#Plotting
plt.stem(y, markerfmt = 'o', use_line_collection=True, label = 'Simulation')
plt.stem(z, markerfmt = 'o', use_line_collection=True, label = 'Theoretical')
plt.ylim(2.2 , 2.3)
plt.ylabel('E(X)')
plt.grid()
