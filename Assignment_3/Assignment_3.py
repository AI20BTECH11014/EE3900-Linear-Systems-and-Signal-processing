import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sympy import *

P = [7,1]

y = np.arange(-5,8,0.00001)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.axis('equal')
def circ_gen(C,r):
	len = 1000
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + C).T
	return x_circ

centre = [0,0]
r = 5
x_circ= circ_gen(centre,r)
q1 = [3,4]
q2 = [4,-3]
x1 = (25/3) - (4*y/3)
x2 = (3*y/4)+(25/4)

#figure(figsize=(5,7))
plt.plot(x_circ[0,:],x_circ[1,:])
plt.scatter(P[0],P[1],color='black')
plt.scatter(q1[0],q1[1],color='black')
plt.scatter(q2[0],q2[1],color='black')
plt.scatter(centre[0],centre[1],color='black')
plt.plot(x1,y,label='Tangent 1')
plt.plot(x2,y,label='Tangent 2')
plt.annotate("P[7,1]",(7,1))
plt.annotate("q1[3,4]",(3,4))
plt.annotate("q2[4,-3]",(4,-3))
plt.annotate("centre",(0,0))

plt.legend()
plt.grid()
plt.show()