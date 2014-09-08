'''
Created on Jan 1, 2014

@author: CJ

The CI function returns the 100(1 - alpha)% CI (Confidence Interval) 
when specified the population mean (mu), population standard deviation
(sigma), sample size (n) and significance level (alpha). Let the 
half-length of the interval be E = z-(alpha/2) * (sigma/sqrt(n)).
Then the CI is given by [mu - E, mu + E].

When sigma is unknown and n >= 30 and the population is not too 
nonnormal, the sample standard population can be used as an
approximation for sigma. When n < 30, we need the t-distribution.
The CDF function for the Student's t Distribution involves the gamma function 
and is therefore a much more complicated integration.
'''

from zalpha import zalpha2
import math

def ci(mu, sigma, n, alpha):
    if n < 2:
        raise Exception("No sampling distribution available")
    
    # the following value is actually z-(alpha/2)
    zalpha = zalpha2(alpha)
    E = zalpha * (sigma * 1.0 / math.sqrt(n))
    
    # return the left end-point and right end-point
    return mu - E, mu + E

