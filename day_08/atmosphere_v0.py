#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from tridiagonal import solve_tridiagonal
from hydrostatic import scale_height,density_species

# ----------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------

if __name__ == "__main__":
    
    dx = 4.0   

    # set x with 1 ghost cell on both sides and the altitude goes from 100 to 500 km:
    x = 100 + np.arange(-dx, 400 + 2*dx, dx) 

    lam = 80 #lambda
    
    nPts = len(x)

    # set default coefficients for the solver:
    a = np.zeros(nPts) - 1
    b = np.zeros(nPts) + 2
    c = np.zeros(nPts) - 1
    d = np.zeros(nPts)
    
    #backgraound source
    Q = np.zeros(nPts)
    Q[27:77] = 0.4
    
    #Qeuv source
    Qeuv = np.zeros(nPts)
    local_time = 12
    #adding time dependence
    def fac(time):
        factorial = -np.cos((time/24)*2*np.pi)
        if factorial<0:
            factorial=0
        return factorial
    
    #getting the plot for 3 days
    ndays = 3
    dt = 1
    times = np.arange(0,ndays*24,dt)
    #plt.plot(time, [fac(i) for i in time]) , this will plot how of time dependence looks as a plot
    #plt.show()
    
    #creating a 2D array for storing temperature values
    temp2d = np.zeros((len(times),nPts))
    dens2dN2 = np.zeros((len(times),nPts))
    dens2dO2 = np.zeros((len(times),nPts))
    dens2dO = np.zeros((len(times),nPts))
 
    lon = 0.0 #defining longitutde
    f107 = 100 + (50/(24*365)*times) + 25*np.sin((times/27*24)*2*np.pi)
    
    #need variables to add tides
    ampDi = 50 # Diurnal amplitude
    ampSd = 25 #semi-diurnal amplitude, because tides occur twice a day
    phaseDi = np.pi/2 #phase of the amp
    phaseSd = 3*np.pi/2 #phase of the amp, slightly dephase it from diurnal. 
    
    n_0_N2 = 1.e19
    n_0_O2 = 0.3*10e19
    n_0_O = 1*10e18
    m_N2 =28*1.67e-27
    m_O2 = 32*1.67e-27
    m_O =16*1.67e-27
    
 
    for i,hour in enumerate(times):
        
        #getting Greenwich Meantime
        ut = hour%24
        local_time = lon/15 + ut
        
        #calculating Qeuv
        sunheat = f107[i]*(0.4/100)
        Qeuv[22:77] = sunheat*fac(local_time)
        
        #calculating d values 
        d = (Q+Qeuv)*dx**2/lam
    
        t_lower = 200.0 + ampDi*np.sin((local_time/24)*2*np.pi + phaseDi) + ampSd*np.sin((local_time/24)*2*np.pi*2 + phaseSd)
        #t_upper = 1000.0, dont need anymore because the upper BC is floating
    
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
        dens2dN2[i] = density_species(m_N2,n_0_N2,t,x)
        dens2dO2[i] = density_species(m_O2,n_0_O2,t,x)
        dens2dO[i] = density_species(m_O,n_0_O,t,x)
        
       
    #plotting and saving the temperature contour plot 
    plotfile = 'conduction_v1.png'
    print('writing : ',plotfile)
    [times2d,alts2d] = np.meshgrid(times,x) #getting a 2D array for times and altitude using meshgrid function
    fig,axs = plt.subplots(nrows=2,ncols=2, figsize=(10,10), sharex=True, sharey=True)
    
    cs = axs[0,0].contourf(times2d,alts2d,temp2d.T)
    axs[0,0].set_title('Time-tependent temperature variation in the thermosphere', fontsize=18)
    axs[0,0].set_ylabel('altitude(km)', fontsize=16)  
    cbar = fig.colorbar(cs)
    cbar.set_label('temperature', rotation=270, fontsize=18)
    
    cs = axs[1,0].contourf(times2d,alts2d,np.log(dens2dN2.T)) #creating the contour plot
    cbar = fig.colorbar(cs) #getting the colourbar
    axs[1,0].set_ylabel('altitude(km)', fontsize=16)
    cbar.set_label('density N2', rotation=270, fontsize=18)
    
    cs = axs[0,1].contourf(times2d,alts2d,np.log(dens2dO2.T)) #creating the contour plot
    cbar = fig.colorbar(cs) #getting the colourbar
    axs[0,1].set_ylabel('altitude(km)', fontsize=16)
    cbar.set_label('density O2', rotation=270, fontsize=18)
    
    cs = axs[1,1].contourf(times2d,alts2d,np.log(dens2dO.T)) #creating the contour plot
    axs[1,1].set_ylabel('altitude(km)', fontsize=16)
    axs[1,1].set_xlabel("Time", fontsize=18)  
    cbar = fig.colorbar(cs) #getting the colourbar
    cbar.set_label('density O', rotation=270, fontsize=18)
    
    fig.savefig(plotfile)
    
    
    plt.show()
    plt.close()
    
    
    
