from numpy import array 
from numpy.linalg import norm  
import matplotlib.pyplot as plt
from sympy import *

def D(A,B):
  Z = A-B
  sum=0
  for i in range(0,2):
    sum=sum + pow(Z[i],2)
  return sum
P = np.array([-1,1]).reshape((2,1))
Q = np.array([2,-1]).reshape((2,1))
l_1= pow(D(P,Q),0.5)
l_2= np.linalg.norm(P-Q)
print('length using inbuilt function:',l_2 )
print('length using D function:',l_1)
print('We can observe that both the results are close to each other.')

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
