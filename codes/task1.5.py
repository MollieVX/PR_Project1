# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:40:33 2017

@author: mayes
"""

import numpy as np
import scipy.misc as msc
import scipy.ndimage as img
import matplotlib.pyplot as plt

FIG_COUNT = 0

def foreground2BinImg(f):
    d = img.filters.gaussian_filter(f, sigma=0.50, mode='reflect') - \
    img.filters.gaussian_filter(f, sigma=1.00, mode='reflect')
    d = np.abs(d)
    m = d.max()
    d[d< 0.1*m] = 0
    d[d>=0.1*m] = 1
    return img.morphology.binary_closing(d)
    
def countN(img, s):
    count = 0
    width, height = img.shape
    for i in range(1, int(1/s) + 1):
        for j in range(1, int(1/s) + 1):
            startRow = int((i - 1) * s * height)
            endRow = int((i * s * height))
            startColumn = int((j - 1) * s * width)
            endColumn = int((j * s * width))
            if(np.any(img[startRow : endRow , startColumn : endColumn])):
                count = count + 1
    return count
    
def fractalDimension(img, fig):
    f = msc.imread(imgName+'.png', flatten=True).astype(np.float)
    g = foreground2BinImg(f)
    plt.figure(fig)
    plt.imshow(g, cmap="binary")
    ni = []
    si = []
    for i in range(1,8):
        s = 1 / float(2**i)
        n = countN(g,s)
        ni.append(n)
        si.append(s)
        
    ni = np.asarray(ni)
    si = np.asarray(si)
    print(ni)
    print(si)
        
    y = np.log(ni)
    x = np.log(1/si)
    
    plt.figure(fig+1)
    plt.plot(x,y,'ks')
    
    X = np.vstack((x, np.ones((x.shape), dtype=x.dtype)))
    X = X.T
    w = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T,y))
    
    xl = np.linspace(0,5)
    yl = w[1] + (w[0] * xl)
    plt.plot(xl,yl)
    plt.show()
    
    return w[0]
    

imgName = 'lightning-3'
D1 = fractalDimension(imgName, 1)
print(D1)
imgName = 'tree-2'
D2 = fractalDimension(imgName, 3)
print(D2)
imgName = 'pattern'
D3 = fractalDimension(imgName, 5)
print(D3)
imgName = 'cat'
D4 = fractalDimension(imgName, 7)
print(D4)




