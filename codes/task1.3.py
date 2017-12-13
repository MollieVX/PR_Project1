"""
Pattern Recognition - Project 1
Task 1.3
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    data = []
    with open('myspace.csv', 'rb') as f:
        for row in f.readlines():
            array = row.split(',')
            if array[1] != '0\n':
                data.append(array[1])
    
    h = np.array(data,dtype=float)
    N = np.sum(h)    
    
    n = len(h)
    x = np.array(range(1,n+1))
    
    k = 1.0
    a = 1.0
    
    for loop in range(20):
        xa = x/a
        xak = np.power(xa,k)
        xalog = np.log(xa)
    
        dLdk = (N/k) - N*np.log(a) + np.dot(h,np.log(x)) - np.dot(h,np.array([p*q for p,q in zip(xak,xalog)]))
       
        dLda = (k / a) * (np.dot(h,xak) - N)
        
        d2Ldk2 = (((-1)*N)/(k*k)) - np.dot(h,np.array([p*q for p,q in zip(xak,np.power(xalog,2))]))
        
        d2Lda2 = (k / (a * a)) * (N - ((k+1) * np.dot(h,xak)))
        
        d2Ldkda = (1 / (np.dot(h,xak)) ) + (k / (a * np.dot(h,np.array([p*q for p,q in zip(xak,xalog)]))) ) - (N/a)
        
        temp = np.array([[d2Ldk2, d2Ldkda], [d2Ldkda, d2Lda2]])
        
        temp = np.linalg.inv(temp)
        
        temp2 = np.dot(temp,np.array([(-1)*dLdk,(-1)*dLda]))
        
        k = k + temp2[0]
        a = a + temp2[1]
    
    print 'kappa = ' + k.astype(str)
    print 'alpha = ' + a.astype(str)
    
    weibull = (k/a) * np.power(x/a,k-1.0) * np.exp ( (-1)* np.power(x/a,k))

    weibull_scaled = weibull * N

    plt.plot(h)
    plt.plot(weibull_scaled)
    plt.xlim(1,n)
    plt.show()
    
    
if __name__ == '__main__':
    main()