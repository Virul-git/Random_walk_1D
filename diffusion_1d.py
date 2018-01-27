import matplotlib.pyplot as plt 
import numpy as np 
import math
import random


def mod(x):
	if(x>=0):
		return x
	else:
		return -1*x;

N=50

x = []
y = []
z = []

for i in range(N/2):
	y = []
	y.append(0)
	for j in range(N):
		if(random.randint(0,1)==1):
			y.append(y[j]+1)
		else:
			y.append(y[j]-1)
	z.append(y[-1])
	x.append(y)


# l=np.zeros(len(z))
# for j in z:
# 	l[len(z)/2+j] = l[len(z)/2+j]+ 1

# plt.plot(range(len(z)),l)
for j in range(len(x)):
	if(j%5==0):
		plt.plot(range(len(x[j])),x[j])

plt.show()