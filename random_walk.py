import matplotlib.pyplot as plt 
import numpy as np 
import math
import random


N=50000

x = []
y = []

x.append(1)
y.append(1)

for j in range(N):
	if(random.randint(0,1)==1):
		x.append(x[j]+1)
	else:
		x.append(x[j]-1)
	if(random.randint(0,1)==1):
		y.append(y[j]+1)
	else:
		y.append(y[j]-1)

# print(x)



plt.plot(y,x)
plt.show()