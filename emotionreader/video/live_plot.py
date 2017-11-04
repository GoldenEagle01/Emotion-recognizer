import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import plotly.plotly as py
import time
import datetime
import warnings
import matplotlib.cbook
import matplotlib.image as mpimg
import matplotlib.animation as animation
from matplotlib import style

time_display = time.time()

def init():
    plt.show()
    print "Starting plot window"
    time_display = time.time()

def plot(array, prediction):
    warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
    matplotlib.use("TkAgg")
    #normalize array
    array_percent = [ int(round(x * 100, 0)) for x in array]

    N = len(array)
    emotions = range(N)

#if len(array_percent) is not 0:
    #print array_percent
    #print emotions

    colors = ['red', 'purple', 'green', 'black', 'blue', 'yellow']

    # plot window 1 - graph 1
    #plt.figure(1)
    plt.rcParams["figure.figsize"] = [7.9, 9]
    plt.subplot(221)
    plt.bar(emotions, array_percent, color=colors, width=0.9)
    plt.ylim([0,100])
    plt.title("Live Feed Plot")
    plt.xlabel("   Anger       Disgust       Happy       Neutral      Sadness      Surprise")
    plt.ylabel("Percentage")

    # plot window 1 - graph 1
    plt.subplot(222)
    if prediction == 0:
        image = mpimg.imread("emoji/anger.png")
        plt.imshow(image)
    elif prediction == 1:
        image = mpimg.imread("emoji/disgust.png")
        plt.imshow(image)
    elif prediction == 2:
        image = mpimg.imread("emoji/happy.png")
        plt.imshow(image)
    elif prediction == 3:
        image = mpimg.imread("emoji/neutral.png")
        plt.imshow(image)
    elif prediction == 4:
        image = mpimg.imread("emoji/sad.png")
        plt.imshow(image)
    elif prediction == 5:
        image = mpimg.imread("emoji/surprise.png")
        plt.imshow(image)

#plt.subplot(224)
#plt.cla()

#plt.figure(2)
    plt.subplot(223)
    plt.ylim([0,100])
    time_2 = round(time.time() - time_display, 2)

    print time_2
    if len(array_percent) is not 0:
        print array_percent[prediction]
    
    # plot
    if len(array_percent) is not 0:
        plt.scatter(time_2, array_percent[prediction])
    plt.gcf().autofmt_xdate()
    
    # update plot
    plt.pause(.1)
    #plt.clf()

if __name__== "__main__":
    matplotlib.use("TkAgg")
    for x in range(0, 1000):
        plot()
        time.sleep(0.1)
        
