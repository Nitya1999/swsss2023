# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:15:58 2023

@author: nitya
"""

#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from tridiagonal import solve_tridiagonal

# ----------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------

if __name__ == "__main__":

    dx = 0.25    

    # set x with 1 ghost cell on both sides:
    x = np.arange(-dx, 10 + 2 * dx, dx)
    
    lam = 10
    
    t_lower = 200.0
    t_upper = 1000.0

    nPts = len(x)

    # set default coefficients for the solver:
    a = np.zeros(nPts) - 1
    b = np.zeros(nPts) + 2
    c = np.zeros(nPts) - 1
    d = np.zeros(nPts)
    Q = np.zeros(nPts)
    Q[3:-17] = 100
    d = Q*dx**2/lam

    # boundary conditions (bottom - fixed):
    a[0] = 0
    b[0] = 1
    c[0] = 0
    d[0] = t_lower

    # top - floating:
    a[-1] = 1
    b[-1] = -1
    c[-1] = 0
    d[-1] = 0

    # Add a source term:
    
    # solve for Temperature:
    t = solve_tridiagonal(a, b, c, d)

    # plot:
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(111)

    ax.plot(x, t)
    

    plotfile = 'conduction_v1.png'
    print('writing : ',plotfile)    
    fig.savefig(plotfile)
    plt.show()
    plt.close()
    
    
    
