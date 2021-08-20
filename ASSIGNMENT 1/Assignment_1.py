#Import the libraries#
import numpy as np 
import matplotlib.pyplot as plt
from sympy import *

#To label the points  
X = [-1,2]
Y = [1,-1]
#To get the line 
X1 =[-1,2]
Y1 = [1,-1]
 
plt.scatter(X,Y,label = 'Points',color='skyblue')
plt.plot(X1,Y1,color = 'orange')
plt.annotate("P:[-1,1]", (-1,1)) 
plt.annotate("Q:[2,-1]",(2,-1))

plt.xlabel('X - axis')
plt.ylabel('Y - axis')
 
plt.legend()
plt.grid()
plt.show()