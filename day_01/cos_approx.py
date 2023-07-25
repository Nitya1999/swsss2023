#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Nitya Agarwala'
__email__ = 'nityaagarwala@yahoo.in'

from math import factorial
from math import pi


def cos_approx(x, accuracy=10):
    """ Returns an approximate cosine using Taylor series
    """
<<<<<<< HEAD
    n = [((-1)**n)/(factorial(2*n))*(x**(2*n)) for n in range(accuracy)]
    
    s = sum(n)
    return s
=======
    """
    
    return 


>>>>>>> 96c453cc0d4b2ff9b2d3923dc2611bb17be576f6

# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
    
    

    
