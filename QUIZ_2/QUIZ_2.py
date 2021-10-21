import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

fig, ax = plt.subplots(figsize = (6,6))

ax.set_xlim([-5,5])
ax.set_ylim([-5,5])

pole, = plt.plot(1/6,0, 'rx',label = 'Poles')


legend = plt.legend(handles =[pole], loc = 'lower right')
fig.gca().add_artist(legend)

circle = plt.Circle([0,0],10,color = 'g')
fig.gca().add_artist(circle)

circle = plt.Circle([0,0],1,edgecolor = 'black',fill = 0,linestyle = '--')
fig.gca().add_artist(circle)

circle = plt.Circle([0,0],1/6,color = 'w')
fig.gca().add_artist(circle)

patches = mpatches.Patch(color="g", label="ROC")
dotted_line = mlines.Line2D([],[],color = 'black',label='Unit circle')
dotted_line.set_linestyle('--')
plt.legend(handles=[patches,dotted_line], loc = 'upper right')

plt.grid()
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()