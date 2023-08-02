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
    
    #backgraound source
    Q = np.zeros(nPts)
    Q[12:28] = 100
    
    #Qeuv source
    Qeuv = np.zeros(nPts)
    local_time = 12
    sunheat = 100
    #adding time dependence
    def fac(time):
        factorial = -np.cos((time/24)*2*np.pi)
        if factorial<0:
            factorial=0
        return factorial
    
    ndays = 3
    dt = 1
    times = np.arange(0,ndays*24,dt)
    #plt.plot(time, [fac(i) for i in time])
    #plt.show()
    
    temp2d = np.zeros((len(times),nPts))
    fig,axs = plt.subplots(1, figsize=(10,10), sharex=True)
 
    lon = 0.0   
 
    for i,hour in enumerate(times):
        ut = hour%24
        local_time = lon/15 +ut
        
        Qeuv[12:28] = sunheat*fac(local_time)
        d = (Q+Qeuv)*dx**2/lam
    
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
        temp2d[i] = t
       
    
    plotfile = 'conduction_v1.png'
    print('writing : ',plotfile)
    [times2d,alts2d] = np.meshgrid(times,x)
    cs = axs.contourf(times2d,alts2d,temp2d.T)
    cbar = fig.colorbar(cs)    
    plt.xlabel('altitude', fontsize=18)    
    plt.ylabel('temperature', fontsize=18)
    plt.title('Time-tependent temperature variation in the thermosphere', fontsize=18)
    fig.savefig(plotfile)
    plt.show()
    plt.close()
    
    
    
