#!/usr/bin/env python
"""Space Weather Simulation Summer School
"""
__author__ = 'Nitya Agarwala'
__email__ = 'nityaagarwala@yahoo.in'

import numpy as np
import matplotlib.pyplot as plt

num_pts = 100
n_0_N2 = 1.e19
n_0_O2 = 0.3*10e19
n_0_O = 1*10e18
alt_0 = 100
alt_n = 500
temp_0 = 200
temp_n = 1000
m_N2 = 28*1.67e-27
k = 1.38e-23
radius_e = 6370  # km

def scale_height(temp, gravity, mass):
    """Returns scale height given temperature and accel. due to gravity
    """
    return k*temp/mass/gravity

def density_species(m,n_0,temp,alt):
     
     n = [n_0]
     g = 3.99e14 / ((radius_e+alt)*1000)**2
     sc_height = scale_height(temp=(temp[1:]+temp[:-1])/2,
                              gravity=(g[1:]+g[:-1])/2,mass=m)

     for h, t_0, t_1, dz in zip(sc_height,
                                temp[:-1], temp[1:],
                                (alt[1:]-alt[:-1])*1000):
         n += [t_0/t_1 * n[-1] * np.exp(-1*dz/h)]
     return n  

if __name__ == '__main__':
    # Set up problem
    alt = np.linspace(alt_0, alt_n, num_pts)
    temp = np.linspace(temp_0, temp_n, num_pts)
    m = m_N2
    n = n_0_N2 
    dens = density_species(m, n, temp, alt)
    
    # Plot
    plt.plot(alt, np.log(dens))
    plt.xlabel('Altitude [km]')
    plt.ylabel('Density [N2] [$m^{-3}$]')
    plt.show()
    
    m = m_O2
    n = n_0_O2
    dens = density_species(m, n, temp, alt)

    plt.plot(alt, np.log(dens))
    plt.xlabel('Altitude [km]')
    plt.ylabel('Density [O2] [$m^{-3}$]')
    plt.show()
    
    m = m_O2
    n = n_0_O2
    dens = density_species(m, n, temp, alt)

    plt.plot(alt, np.log(dens))
    plt.xlabel('Altitude [km]')
    plt.ylabel('Density [O2] [$m^{-3}$]')
    plt.show()