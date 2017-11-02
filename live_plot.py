import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import plotly.plotly as py

#array = np.random.rand([[ 0.09436784  0.10402838  0.09374937  0.35026402  0.28324831  0.07434209]])
array = [[ 0.09436784  0.10402838  0.09374937  0.35026402  0.28324831  0.07434209]]
array_percent = [ round(x * 100, 0) for x in array]
#array_percent = array

N = len(array)
emotions = range(N)

print array_percent
print emotions

colors = ['#624ea7', 'g', 'yellow', 'k', 'maroon', 'blue', 'green']

plt.bar(emotions, array_percent, color=colors)
plt.title("Live Feed Plot")
plt.xlabel("Emotions")
plt.ylabel("Percentage")

red_patch = mpatches.Patch(color='#624ea7', label='Happy')
g_patch = mpatches.Patch(color='g', label='Anger')
yellow_patch = mpatches.Patch(color='yellow', label='Disgust')
k_patch = mpatches.Patch(color='k', label='Neutral')
maroon_patch = mpatches.Patch(color='maroon', label='Sad')
blue_patch = mpatches.Patch(color='blue', label='Surprised')
green_patch = mpatches.Patch(color='green', label='Fear')
plt.legend(bbox_to_anchor=(1, 0.7), loc=10, borderaxespad=0.,
           handles=[red_patch, g_patch, yellow_patch, k_patch, maroon_patch, blue_patch, green_patch])
plt.show()
