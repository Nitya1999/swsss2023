from numpy.linalg import norm
import numpy as np

import time

def explicit_RK_stepper(f,x,t,h,a,b,c):
    """
        Implementation of generic explicit Runge-Kutta update for explicit ODEs
        
        inputs:
            x - current state 
            t - current time
            f - right-hand-side of the (explicit) ODE to be integrated
            h - step size 
            a - coefficients of Runge-Kutta method (organized as list-of-list (or vector-of-vector))
            b - weights of Runge-Kutta method (list/vector)
            c - nodes of Runge-Kutta method (including 0 as first node) (list/vector)

        outputs: 
            x_new - estimate of 
    """
    s = len(c)
    ks = [f(x,t)]
    x_new = x + h*b[0]*ks[0]
    for i in range(s-1):
        x_tilde = x + h*sum(a[i][j]*ks[j] for j in range(i+1))
        ks.append(f(x_tilde, t+h*c[i+1]))
        x_new += h*b[i+1]*ks[-1]
    return x_new

def integrate(f, x0, tspan, h, step):
    """
        Generic integrator interface

        inputs:
            f     - rhs of ODE to be integrated (signature: dx/dt = f(x,t))
            x0    - initial condition (numpy array)
            tspan - integration horizon (t0, tf) (tuple)
            h     - step size
            step   - integrator with signature: 
                        step(x,t,f,h) returns state at time t+h 
                        - x current state
                        - t current time 
                        - f rhs of ODE to be integrated
                        - h stepsize

        outputs: 
            ts - time points visited during integration (list)
            xs - trajectory of the system (list of numpy arrays)
    """
    t, tf = tspan
    x = x0
    trajectory = [x0]
    ts = [t]
    while t < tf:
        h_eff = min(h, tf-t)
        x = step(f,x,t,h_eff)
        t = min(t+h_eff, tf)
        trajectory.append(x)
        ts.append(t)
    return trajectory, ts

def adaptive_explicit_RK_stepper(f,x,t,h,a,b,c,b_control):
    """
        Implementation of generic explicit Runge-Kutta update for explicit ODEs
        
        inputs:
            x - current state at time t 
            t - current time
            f - right-hand-side of the (explicit) ODE to be integrated
            h - step size 
            a - coefficients of Runge-Kutta method (organized as list-of-list (or vector-of-vector))
            b - weights of Runge-Kutta method (list/vector)
            c - nodes of Runge-Kutta method (including 0 as first node) (list/vector)
            b - weights of control Runge-Kutta method (list/vector)

        outputs: 
            x_new - estimate of state at time t + h
            error - estimate of the accuracy
    """
    
    s = len(c)
    ks = [f(x,t)]
    x_new = x + h*b[0]*ks[0]
    error = h*(b_control[0] - b[0])*ks[0]
    
    for i in range(s-1):
        x_tilde = x + h*sum(a[i][j]*ks[j] for j in range(i+1))
        ks.append(f(x_tilde, t+h*c[i+1]))
        x_new += h*b[i+1]*ks[-1]
        error += h * (b_control[i+1]-b[i+1]) * ks[-1]
    
    return x_new, norm(error) 

def adaptive_integrate(f, x0, tspan, h, step, rtol = 1e-8, atol = 1e-8):
    """
        Generic integrator interface for adaptive integrators

        inputs:
            f     - rhs of ODE to be integrated (signature: dx/dt = f(x,t))
            x0    - initial condition (numpy array)
            tspan - integration horizon (t0, tf) (tuple)
            h0    - initial step size
            step   - integrator with signature: 
                        step(f,x,t,h) returns state, error at time t+h 
                        - x current state
                        - t current time 
                        - f rhs of ODE to be integrated
                        - h stepsize
            rtol  - relative tolerance for time step adaptation 
            atol  - absolute tolerance for time step adaptation

            Algorithm:
                If error <= rtol*norm(x) + atol => accept step and double step size
                If error > rtol*norm(x) + atol => reject step and half step size 

        outputs: 
            ts - time points visited during integration (list)
            xs - trajectory of the system (list of numpy arrays)
    """
    
    ts = []
    xs = []
    
    t0, tf = tspan
    
    xs.append(x0)
    ts.append(t0)
    
    x = x0
    t = t0
    
    while t < tf:
        x_new, error = step(f,x,t,h)
        
        if error > rtol * norm(x_new) + atol:
            h = h/2
        else:
            xs.append(x_new)
            ts.append(t+h)
            
            x = x_new
            t = t+h
            
            h = 2*h
    
    return xs, ts

                 