import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sympy import *


y = np.arange(-150,180,0.00001)
plt.xlim(-150,150)
plt.ylim(-150,150)
plt.axis('equal')

x1 = (-1)*y
x2 = (2*y/3)-(7/3)
x3 = ((y*((-1/np.sqrt(2)) +(2/np.sqrt(13))))/((1/np.sqrt(2))+(-3/np.sqrt(13)))) +  (((10 -(7/np.sqrt(13))))/((1/np.sqrt(2))+(3/np.sqrt(13))))
x4 = ((y*((-1/np.sqrt(2)) +(-2/np.sqrt(13))))/((1/np.sqrt(2))+(3/np.sqrt(13)))) +  (((10 +(7/np.sqrt(13))))/((1/np.sqrt(2))+(-3/np.sqrt(13))))
x5 = ((y*((-1/np.sqrt(2)) +(2/np.sqrt(13))))/((1/np.sqrt(2))+(3/np.sqrt(13)))) -  (((10 +(7/np.sqrt(13))))/((1/np.sqrt(2))+(3/np.sqrt(13))))
x6 = ((y*((1/np.sqrt(2)) +(2/np.sqrt(13))))/((-1/np.sqrt(2))+(3/np.sqrt(13)))) +  (((10 -(7/np.sqrt(13))))/((-1/np.sqrt(2))+(3/np.sqrt(13))))


plt.plot(x1,y,label='l1')
plt.plot(x2,y,label='l2')
plt.plot(x3,y,label='L1')
plt.plot(x4,y,label='L2')
plt.plot(x5,y,label='L3')
plt.plot(x6,y,label='L4')



plt.legend()
plt.grid()
plt.show()