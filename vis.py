import numpy as np
import math
import matplotlib.pyplot as plt

def sin(x): return np.sin(x)
def cos(x): return np.cos(x)
def tan(x): return np.tan(x)
def cot(x): return np.cot(x)


def visualize_marble(ind_below, ind_above, ind_neg, range_init, range_end, x, y, ax1):
	ax1.scatter([i[0] for i in ind_above], [i[1] for i in ind_above], color = "blue")
	ax1.scatter([i[0] for i in ind_below], [i[1] for i in ind_below], color = "green")
	ax1.scatter([i[0] for i in ind_neg], [i[1] for i in ind_neg], color = "red")
	ax1.plot(x, y, color = "black", label='Function', linewidth=2)
	ax1.plot([range_init, range_end], [0,0], color = "black", linewidth=2)
	ax1.legend()

def visualize_mean(ind_below, ind_above, range_init, range_end, x, y, mean, ind_rand, ax2):
	within_mean = []
	for i in ind_rand:
	  if(mean>=0 and i[1]<mean and i[1]>=0):
	    within_mean.append(i)
	  elif(mean<0 and i[1]>mean and i[1]<=0):
	    within_mean.append(i)
	outside_mean = [i for i in ind_rand if(i not in within_mean)]

	ax2.plot([range_init, range_end], [mean,mean], color = "red",  label='Mean', linewidth=2)
	ax2.plot(x, y, color = "black", label='Function', linewidth=2)
	ax2.plot([range_init, range_end], [0,0], color = "black", linewidth=2)
	ax2.scatter([i[0] for i in within_mean], [i[1] for i in within_mean], color = "green")
	ax2.scatter([i[0] for i in outside_mean], [i[1] for i in outside_mean], color = "blue")
	ax2.legend()