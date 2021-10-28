import numpy as np
import matplotlib.pyplot as plt

N = 500000
x = np.linspace(-25,25, N)

#theoretical def of rect function
def rectFunction(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] >= -0.5 and t[i] <= 0.5:
            y[i] = 1
    return y
#implementing sinc(x)
def sinc(x):
  x_t = np.sin((2 * np.pi * x))/((2 * np.pi * x))
  return x_t
#Computing the fourier function
y = sinc((3*x)+2)
#Computing the rectangular transform
y_rect = [50*np.mean(y * np.exp(-1j * 2 * np.pi * f * x)) for f in x]
#Comparing it with the theoretical result
y_t = (1/6) * np.exp(-1j * 2 * np.pi * (2/3) * x) * rectFunction(x/(6))

#Plotting sinc(3t+2)
plt.plot(x,y)
plt.xlabel('$t$')
plt.ylabel('$x(3t+2)$')
plt.grid()
plt.xlim(-5,5)
plt.show()

fig1, ax1 = plt.subplots(2,1)
#Plotting the signals of amplitude
ax1[0].plot(x, np.absolute(y_rect), label="Simulation")
ax1[0].plot(x, np.absolute(y_t), label="Theoretical")
ax1[0].set_ylabel("$A$")
ax1[0].legend(loc = "best")
ax1[0].grid()

#Plotting the phase
ax1[1].plot(x, np.angle(y_rect), label="Simulation")
ax1[1].plot(x, np.angle(y_t), label="Theoretical")
plt.xlabel("$f$")
ax1[1].set_ylabel("$\phi$")
ax1[1].legend(loc = "best")
ax1[1].grid()
plt.show()