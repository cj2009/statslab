'''
Created on Jun 7, 2014

@author: CJ

This is a more generalized version of the CDF.py module. Here, we are able to 
deal with any normal distribution, instead of just the standard normal dist.

The generalized formula is given below:
    f(x, mu, sigma) = k * e^[-((x-mu)^2)/(2*sigma^2)]
    where k = 1/(sigma * sqrt(2*pi))
    (see en.wikipedia.org/wiki/Normal_distribution for the formula)
    
'''
import math
import matplotlib.pyplot as pyplot
import numpy


def cdf(x = 0.0, mu = 0, sigma = 1, begin = -10.0, step = 0.0001):
    x = float(x)            # force conversion to float
    begin = float(begin)
    mu = float(mu)
    sigma = float(sigma)
   
    area = 0
    while x > begin:
        # calculate the value of the exponent first, for simplicity:
        exponent = (x-mu)**2 / (-2*sigma**2)
        # height is the value of the function, or f(x)
        height = math.pow(math.e, exponent)
        # step is the width of the rectangle, so multiply it by the
        # function value to get the area:
        areaIncrement = height * step
        # add this to the area variable
        area += areaIncrement
        # since we're integrating right-to-left, decrement x by
        # one step, or one width of the rectangle
        x -= step
        
    # Finally, multiply area by k = 1/(sigma * sqrt(2*pi)) and return the answer:
    k = 1 / (sigma * math.sqrt(2 * math.pi))
    return area * k


# This function returns f(x,mu,sigma), which is simply the probability density
# function.
def pdf(x, mu, sigma):
    x = float(x)
    mu = float(mu)
    sigma = float(sigma)
    
    exponent = (x-mu)**2 / (-2 * sigma**2)
    k = 1 / (sigma * math.sqrt(2 * math.pi))
    
    return k * math.e**exponent


# This function plots CDF(x) for a given value of x
def plot(x = 0, mu = 0, sigma = 1):
    x = float(x)                    # force conversion to floats
    mu = float(mu)
    sigma = float(sigma)
    
    # Define the x variable and its range:
    xvar = numpy.arange(mu-8, mu+8, 0.01)
    
    # Create some constants to simplify the PDF function:
    k = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = (xvar - mu)**2 / (-2 * sigma**2)
    
    yvar = k * numpy.e**exponent        # define the y variable
        
    pyplot.plot(xvar, yvar)
    
    pyplot.xlabel('x')
    pyplot.ylabel('f(x)')
    titleMsg = 'The Normal Distribution (mu = ' + str(mu) + ', sigma = ' + str(sigma) + ')'
    pyplot.title(titleMsg)
    pyplot.grid(True)
    
    # This does the shading of the curve:
    pyplot.fill_between(xvar, yvar, 0, where = xvar<x)
    
    # Let's display a message indicating the area, which is the value of the CDF:
    message = "Area of shaded region = \nCDF(" + str(x) + ") = " + str(cdf(x, mu, sigma, begin = mu-15)) 
    pyplot.text(mu, 0.9*pdf(mu, mu, sigma), s=message)
    
    pyplot.show()
    
    
def main():
    # As an example, let's plot the CDF of a normal distribution with mu = -1.5
    # and sigma = 3. We expect the curve to be centered around mu and be 
    # wider than what it is normally, because of the higher value of sigma.
    # We'll do x = 1, so it's the accumulated area from x = -infinity to x = 1.
    plot(1, -1.5, 3)
    
main()