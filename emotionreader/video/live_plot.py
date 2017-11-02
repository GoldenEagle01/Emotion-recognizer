import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import time

def init():
    plt.get_backend()
    plt.show()
    print "starting plot"

def plot(array):
    #normalize array
    array_percent = [ round(x * 100, 0) for x in array]

    N = len(array)
    emotions = range(N)

    print array_percent
    #print emotions

    colors = ['red', 'purple', 'green', 'black', 'blue', 'yellow']

    plt.bar(emotions, array_percent, color=colors, width=0.9)
    plt.ylim([0,100])
    plt.title("Live Feed Plot")
    plt.xlabel("   Anger       Disgust       Happy       Neutral      Sadness      Surprise")
    plt.ylabel("Percentage")
    
    plt.pause(.001)
    plt.clf()      

if __name__== "__main__":
    
    for x in range(0, 1000):
        plot()
        time.sleep(0.1)
        

