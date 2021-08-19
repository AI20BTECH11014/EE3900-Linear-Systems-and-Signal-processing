import numpy as np
from matplotlib import pyplot as plt

#Function to calucate the DFT of an 1D sequence of points
def IFT(X):
  N = len(X)
  k = np.arange(N)
  n = k.reshape((N,1))
  e = np.exp(2j*np.pi*k*n/N)
  x = (np.dot(e,X))/N
  return x

#Given X[k] = k+1 
X = np.array([1,2,3,4,5,6,7,8])
x_inbuilt = np.fft.ifft(X) 
x_simulated = IFT(X)
#The value of x[0] + x[2] + x[4] + x[6] using inbuilt function 
sum = 0 
for i in range(0,4):
  sum = sum + x_inbuilt[2*i]
#The value of x[0] + x[2] + x[4] + x[6] using defined function 
count = 0
for i in range(0,4):
   count= count + x_simulated[2*i]

print('Output using inbuilt function:',sum )
print('Output using DFT function:',count)
print('We can observe that both the results are close to each other.')

#Plotting
n = np.linspace(0,7,8)
plt.stem(n,abs(x_inbuilt),use_line_collection=True)
plt.xlabel('n')
plt.ylabel('$|x[n]|$')
plt.show()