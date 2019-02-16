import numpy as np
import matplotlib.pyplot as plt

dataMat = np.random.multivariate_normal([1,2],[[1,0],[0,10]],1000)

plt.scatter(dataMat[:,0],dataMat[:,1],s=15)
plt.show()