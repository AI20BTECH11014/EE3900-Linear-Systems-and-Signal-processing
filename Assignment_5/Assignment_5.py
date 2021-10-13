import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

V=np.reshape([1,0,0,0],(2,2))
u=np.reshape([0,-2],(2,1))
f=0
q=np.reshape([-2,0],(2,1))


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 5
y = np.linspace(-4,4,len)

x=np.linspace(-3,3)
x1=np.linspace(-3,3)
y1=4
#Generating the Standard parabola
y =(x*x)
xStandardparab = np.vstack((x,y))


#Plotting all lines
plt.axhline(y=0,color='gray')
plt.axhline(y=4,color='g',label = 'y=$4$')
plt.axvline(x=2,color='blue',label = 'x=$2$' ,linestyle='--')
plt.axvline(x=-2,color='orange',label ='x=$-2$',linestyle='--')

#Plotting the actual parabola
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='x^2 = y',color='r')

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()