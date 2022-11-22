import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap


"""
  A previous, much simpler, but less flexible script
"""

# colors = [
#     (0,0,0),
#     (0,0,0.5),
#     (0,0.5,1),
#     (1,1,1)
# ]

colors = [
    (1,1,1),
    (0,0,0.5),
    (1,0,0),
    (1,1,0)
]

# colors.reverse()

my_cmap = LinearSegmentedColormap.from_list('cool', colors, N=100)


def draw(data, time, limits, cmap):
	ax = plt.subplot(111)
	# plt.title(title, fontsize=16, y=1.0, pad=-18)
	plt.title('t = '+time+' yr', fontsize=16, y=1.0, pad=-18)
	im = plt.imshow(data, cmap=cmap, vmin=limits[0], vmax=limits[1])
	cb = plt.colorbar(im, ax=ax, pad=0.02)
	cb.ax.tick_params(labelsize=16)
	cb.ax.yaxis.get_offset_text().set(size=16)
	ax.set(xticks=[], yticks=[])
	plt.plot([150], [150], 'wo', markersize=5)
	plt.savefig('a45s003m07_'+t+'.png')
	plt.close()


for i in range(50):
	if (i+1)%10==0:
		print(i, end='\n')
	else:
		print(i, end=' ')
	data = np.genfromtxt('syn_'+str(100+i)+'.dat')
	time = (100+i)/10.0
	t = str(time)
	draw(data, t, (0,0.2), my_cmap)
