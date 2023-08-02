# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:26:40 2023

@author: nitya
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -2*x

def analytic_sol(t):
    return 3*np.exp(-2*t)

x0 = 3.0

#time step soze
h = 0.01

T = 2

#number of steps needed
N = int(np.ceil(T/h))

xs = np.zeros(N+1)
ts = np.zeros(N+1)

xs[0] = x0
ts[0] = 0.0

for i in range(N):
    xs[i+1] = xs[i] + h*f(xs[i])
    ts[i+1] = ts[i] +h

fig, ax = plt.subplots()
ax.scatter(ts, xs, linewidth=2, color='black', label="Explicit Euler")

trange = np.linspace(0, T, 1000)
ax.plot(trange, analytic_sol(trange), linewidth=2, color='red', linestyle="dashed", label="analytic")

ax.legend()








