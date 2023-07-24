# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:59:07 2023

@author: nitya
"""
"""A 3D plot script for spherical coordinates."""

__author__ = 'Nitya Agarwala'
__email__ = 'nityaagarwala@yahoo.in'

import numpy as np
import matplotlib.pyplot as plt

def convert_spherical_to_cartesian(radius, phi, theta): 
    #defining a function that will convert spherical co-ordinates to cartesian co-ordinates

    r = radius #assigning value of radius to r

    sin_theta = np.sin(theta) #calculating the value of sin theta
    cos_theta = np.cos(theta) #calculating the value of cos theta
    sin_phi = np.sin(phi) #calculating the value of sin phi
    cos_phi = np.cos(phi) #calculating the value of cos phi
    
    x = r*sin_phi*cos_theta #calculating the cartesian co-ordinate x from spherical co-ordinates
    y = r*sin_phi*sin_theta #calculating the cartesian co-ordinate y from spherical co-ordinates
    z = r*cos_phi #calculating the cartesian co-ordinate z from spherical co-ordinates
    
    return (x,y,z) #getting the value of the converted cartesian co-ordinates

output = convert_spherical_to_cartesian(1, np.pi*2, np.pi*2) #checking the function by putting in values
print (output)

fig = plt.figure()
#axes = fig.gca(projection = '3d')
axes = plt.axes(projection='3d')
r = np.linspace(0,1)
theta = np.linspace(0, 2*np.pi)
phi = np.linspace(0, 2*np.pi)
x, y, z = convert_spherical_to_cartesian(r, theta, phi)
axes.plot(x, y, z)

    