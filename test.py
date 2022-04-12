import numpy as np
import matplotlib.pyplot as plt

array = [3,4,5]
array2= [1,2,1]

intercept = 0
for i in range(len(array)):
    plt.plot([intercept, intercept + array[i]/4], [0, array2[i]], color='green')
    plt.plot([intercept + array[i]/4, intercept + (3 * array[i] / 4)], [array2[i], -1 * array2[i]], color='green')
    plt.plot([intercept + (3 * array[i] / 4), intercept + array[i]], [-1 * array2[i],0], color ='green')
    intercept += array[i]
plt.show()