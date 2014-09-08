'''
Created on Jan 1, 2014

@author: CJ

The z-alpha value is defined such that P(Z >= z-alpha) = alpha. The 
function 'zalpha' in this module calculates the value of z-alpha for a 
given value of alpha. This is done by integration, which starts at 
x = 0 and proceeds to the right until the accumulated area equals 
(or just exceeds) the desired area. Let's call the stopping point 
x = b. 

The desired area is then CDF(b) - CDF(0). This area is either 
plus or minus (1 - alpha), depending on whether alpha is greater than 
or less than 0.5. The value b is actually z-alpha or -z-alpha; you can 
verify this by drawing a graph of the standard normal distribution and 
observing the symmetry.

The function zalpha2 calculates the value of z-(alpha/2) for a given 
value of alpha. It takes advantage of the fact that finding z-(alpha/2) for a 
given alpha is equivalent to finding the absolute value of z-(2alpha) for a 
given value of alpha. Therefore it uses the first function as a helper method.

'''

import math

def zalpha(a, step = 0.00001):
    # with step = 0.00001, answers are accurate up to 3 decimal places
    # for more precision, decrease the step
    
    a = float(a)        # force conversion to float
    if a < 0.0 or a > 1.0:
        raise Exception("Invalid alpha value")
    if (abs(a-0.5)) * 1000 < 1:
        # this is a way of checking if a == 0.5, since floats can't be 
        # compared directly
        return 0
    
    desiredArea = 0.5 - a
    if a > 0.5:
        desiredArea *= -1.0
    currentArea = 0.0
    zalpha = 0.0
    # zalpha is the value b that is mentioned above in the comments
    # it may need to be negated before returning the final answer
    
    # the test condition in the while header is checking if the area
    # accumulated so far is less than desiredArea. Note that we need to
    # divide by sqrt(2pi) to get the 
    while (currentArea/math.sqrt(2*math.pi) < desiredArea):
        increment = math.e**(-0.5*zalpha*zalpha) * step
        currentArea += increment
        zalpha += step
    
    # negate the value of z-alpha, if necessary:
    if a > 0.5:
        zalpha *= -1.0
    return zalpha

'''
As explained above, this function simply calls the above function with a 
different parameter.
'''
def zalpha2(a):
    return abs(zalpha(2*a))