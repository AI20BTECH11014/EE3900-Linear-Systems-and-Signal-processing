import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

time = np.linspace(-3,5,10000)
e = (np.exp(time)) -1
def unit(time):
  x=[]
  for i in time:
    if i<0:
      x.append(0)
    else:
      x.append(1)
  return x      
x = e*unit(time)

fig, ax = plt.subplots(figsize = (6,6))

ax.set_xlim([-5,5])
ax.set_ylim([-5,5])

pole, = plt.plot(1,0, 'rx',label = 'Poles')


legend = plt.legend(handles =[pole], loc = 'lower right')
fig.gca().add_artist(legend)

circle = plt.Circle([0,0],10,color = 'g')
fig.gca().add_artist(circle)

circle = plt.Circle([0,0],1,edgecolor = 'b',fill = 0,linestyle = '--')
fig.gca().add_artist(circle)

circle = plt.Circle([0,0],1,color = 'w')
fig.gca().add_artist(circle)

patches = mpatches.Patch(color="g", label="ROC")
plt.legend(handles=[patches], loc = 'upper right')

plt.grid()
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()

plt.plot(time,x,label='x(t)')
plt.xlabel('Time')
plt.grid()
plt.legend()
