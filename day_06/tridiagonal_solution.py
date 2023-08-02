# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:18:30 2023

@author: nitya
"""


import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Taken from:
# https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
# BUT - they go from 1 -> n and python goes from 0 -> n-1
# ----------------------------------------------------------------------

def solve_tridiagonal(a, b, c, d):

    """ Function that solves a tridiagonal matrix

    Parameters
    ----------
    a - i-1 coefficient
    b - i coefficient
    c - i+1 coefficient
    d - source term

    Returns
    -------
    x - solution to tri-diagonal matrix

    Notes
    -----
    Solve system of equation

    """
    
    nPts = len(a)

    cp = np.zeros(nPts)
    dp = np.zeros(nPts)
    x = np.zeros(nPts)

    # calculate c':
    i = 0
    cp[i] = c[i]/b[i]
    for i in range(1, nPts-1):
        cp[i] = c[i] / (b[i] - a[i] * cp[i-1])

    # calculate d':
    i = 0
    dp[i] = d[i]/b[i]
    for i in range(1, nPts):
        dp[i] = (d[i] - a[i] * dp[i-1]) / (b[i] - a[i] * cp[i-1])

    # calculate x:
    i = nPts - 1
    x[i] = dp[i]
    for i in range(nPts-2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]

    return x

if __name__ == "__main__":

    # get figures:
    fig = plt.figure(figsize = (10,10))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    
    # define dx:
    
    x = [0,10]
    dx = 0.25
    

    # plot:

    ax1.plot(x, f)

    # plot first derivatives:
    error = np.sum(np.abs(n_dfdx - a_dfdx)) / len(n_dfdx)
    sError = ' (Err: %5.1f)' % error
    ax2.plot(x, a_dfdx, color = 'black', label = 'Analytic')
    ax2.plot(x, n_dfdx, color = 'red', label = 'Numeric'+ sError)
    ax2.scatter(x, n_dfdx, color = 'red')
    ax2.legend()

    # plot second derivatives:
    error = np.sum(np.abs(n_d2fdx2 - a_d2fdx2)) / len(n_d2fdx2)
    sError = ' (Err: %5.1f)' % error
    ax3.plot(x, a_d2fdx2, color = 'black', label = 'Analytic')
    ax3.plot(x, n_d2fdx2, color = 'red', label = 'Numeric'+ sError)
    ax3.scatter(x, n_d2fdx2, color = 'red')
    ax3.legend()

    
    plotfile = 'plot.png'
    print('writing : ',plotfile)    
    fig.savefig(plotfile)
    plt.close()