from streamplot import LivePlotter
import numpy as np
import time

# Create instance of PlotManager with

live = LivePlotter(name='hello', y_min= -100, frequency = 0.2, y_max = 100)

# Send data to the plot

length = 10000
costs  = np.random.rand(length)*100

for i in range(length):
	cost = costs[i]
	live.add(cost, i)
	live.update()
	time.sleep(live.frequency)

live.close()