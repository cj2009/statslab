'''
Created on Jan 1, 2014

@author: CJ

This function calculates the CDF (Cumulative Distribution Function) of a 
standard normal random variable, whose PDF (Probability Distribution Function) 
is given by f(x) = (1/c)*e^(-0.5x^2), where c = sqrt(2pi).

This program uses right rectangle approximation. 'step' is the width 
of the rectangles, and 'x' = the point up-to which you want to 
integrate. 'begin' is the left-most x-value from which the curve 
is be integrated. The smaller the width of the rectangles, the more
accurate the integration is.

For increased accuracy, we are integrating from right to left. The 
integration starts at the specified value of x and stops at 
x = -15.0 on the left by default, because the area beyond that is 
infinitesimal. Similarly, it is unnecessary to integrate beyond 
x = 15.0 to the right.

There are more efficient integration techniques which converge faster
but this is easy enough to be followed by someone who has taken only an
introductory course in integral calculus.
    
'''
import math
import matplotlib.pyplot as pyplot
import numpy

def cdf(x = 0.0, begin = -10.0, step = 0.0001):
    x = float(x)            # force conversion to float
    begin = float(begin)
   
    area = 0
    while x > begin:
        # height is the value of the function, or f(x)
        height = math.pow(math.e, -0.5*x*x)
        # step is the width of the rectangle, so multiply it by the
        # function value to get the area:
        areaIncrement = height * step
        # add this to the area variable
        area += areaIncrement
        # since we're integrating right-to-left, decrement x by
        # one step, or one width of the rectangle
        x -= step
    # divide by c = sqrt(2pi)
    return area / math.sqrt(2*math.pi)


# This function plots CDF(x) for a given value of x
def plot(x = 0):
    k = math.sqrt(2*math.pi)
    
    xvar = numpy.arange(-5.0, 5.0, 0.01)
    yvar = (1/k) * numpy.e**(-0.5 * xvar**2)
        
    pyplot.plot(xvar, yvar)
    
    pyplot.xlabel('x')
    pyplot.ylabel('f(x)')
    pyplot.title('The Standard Normal Distribution')
    pyplot.grid(True)
    
    # This does the shading of the curve:
    pyplot.fill_between(xvar, yvar, 0, where=xvar<x)
    
    # Let's display a message indicating the area, which is the value of the CDF:
    message = "Area of shaded region = \nCDF(" + str(x) + ") = " + str(cdf(x)) 
    pyplot.text(0.8, 0.35, s=message)
    
    pyplot.show()
    
    
def main():
    # As an example we plot the CDF of the standard normal distribution with 
    # x = 1.2. This means we intergrate the area under the curve from negative
    # infinity to 1.2.
    plot(1.2)

#main()
