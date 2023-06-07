#Imports
import numpy as np
import math
import matplotlib.pyplot as plt
from random import uniform
from vis import *

#Constants
pi = np.pi
e = math.e
step = 0.01

n_rep = 400
range_init = -10
range_end = 0
# 0 = not counting
# 1 = counting as positive
# 2 = counting as negative
include = 2


#Main_function
def f(x):
    return x**2 - 10

#Variables
x = np.arange(range_init, range_end+step, step)
y = f(x)
ind_below = []
ind_above = []
ind_rand = []
ind_neg = []
y_min, y_max = min(y), max(y)

if(y_min>0): y_min = 0
if(y_max<0):
	y_max = 0
	y_max, y_min = y_min, y_max

for i in range(n_rep):
  x_rand, y_rand = uniform(range_init, range_end+step), uniform(y_min, y_max+step)
  ind_rand.append([x_rand,y_rand])

  if(f(x_rand)<y_rand and y_rand<0 and include==1):
    ind_below.append([x_rand,y_rand])

  if(f(x_rand)<y_rand and y_rand<0 and include==2):
    ind_neg.append([x_rand,y_rand])

  if(f(x_rand)>y_rand and y_rand>=0):
    ind_below.append([x_rand,y_rand])

mean = sum([f(i[0]) for i in ind_rand])/len(ind_rand)
ind_above = [i for i in ind_rand if(i not in ind_below and i not in ind_neg)]

#Results
print("Predicted value (Marble approach):", (len(ind_below)-len(ind_neg))/len(ind_rand) * abs(range_init - range_end) * abs(y_max-y_min))
print("Predicted value  (Mean approach) :", mean * abs(range_init - range_end))

#Visualization
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Monte Carlo Simulation')
visualize_marble(ind_below, ind_above, ind_neg, range_init, range_end, x, y, ax1)
visualize_mean(ind_below, ind_above, range_init, range_end, x, y, mean, ind_rand, ax2)
plt.show()
