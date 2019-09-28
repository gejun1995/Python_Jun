import pandas as pd
import matplotlib.pyplot as plt

info="""
----------------------------------------------------
Purpose: Matrix data plots in 2D image in jet mode
Version 1.0
    
Jun Ge
Plant Nutrient, Ph.D.
Zhejiang University
E-mail: gejun@zju.edu.cn or gejun1995@gmail.com
Personal website: www.gejunsci.com

All rights reserved.
    
By Jun Ge
Updated 9/18/2019
----------------------------------------------------


"""
print(info)

filename_temp = input("Input filename: \n\n")
filename = filename_temp + ".txt"
print("Loading: "+filename)

image_array = pd.read_table(filename)
print(image_array)

vmin = input("Input vmin: ")
vmax = input("Input vmax: ")
plt.figure()
img = plt.imshow(image_array, vmin=vmin, vmax=vmax, cmap=plt.cm.jet)
plt.colorbar()
plt.savefig(str(filename) + ".png", dpi=600)
