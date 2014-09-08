'''
Created on Jun 7, 2014

@author: CJ

The HT function performs hypothesis testing involving the standard normal
random variable (SNRV) and returns a binary result: 0 for reject and 1 for accept
(please see the accompanying image 'Hypothesis Testing Rules.png').

In the equation shown in the picture, the Z value is calculated using several
inputs: 
    Y with overline is the sample mean;
    μ is the population mean under the null hypothesis (H0)
    μ0 is the population mean under the alternative hypothesis (H1)
    σ is the sample standard deviation
    n is the sample size
    
For the HT function, the arguments are:
    case: whether the hypothesis testing is case 1, 2 or 3
    ybar: the sample mean
    mu0:  the population mean under the null distribution
    sigma:the sample std. deviation
    n:    the sample size
    alpha:the level of significance (0.01 by default)
'''

import math
import zalpha

def HT(case, ybar, mu0, sigma, n, alpha = 0.01):
    
    # First, check for bad input:
    if n <= 2:
        raise Exception("Sample size must exceed 2")
    if case != 1 and case != 2 and case != 3:
        raise Exception("Invalid case number")
    if sigma <= 0:
        raise Exception("sigma must be strictly positive")
    
    # Next, calculate the Z value:
    Z = (ybar - mu0) / (sigma / math.sqrt(n))

    # Depending on the case number, return the appropriate answers:
    if case == 1:
        if Z >= zalpha.zalpha(alpha):
            return 0
        else:
            return 1
    elif case == 2:
        if Z <= -1 * zalpha.zalpha(alpha):
            return 0
        else:
            return 1
    else:                                                        # case 3
        if abs(Z) >= zalpha.zalpha(alpha/2.0):
            return 0
        else:
            return 1