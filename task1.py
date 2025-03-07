import numpy as np
import scipy
import scipy.integrate

#part A
def integrandvarchanged(z):
    return ((z/(1-z))**3)/(np.exp(z/(1-z))-1)

k = 1.38064852*10**(-23)
h = 6.626*10**(-34)
c = 3*10**8
hbar = h/(2*np.pi)

integralvalue, blank = scipy.integrate.fixed_quad(integrandvarchanged, 0 ,1)
sigma = ((2*np.pi*k**4)/((c**2)*(h**3)))*integralvalue
print(sigma)

#part C
def integrand(x):
    return (x**3)/(np.exp(x)-1)
integralvalue, blank = scipy.integrate.quad(integrand, 0, np.inf)
sigma = ((2*np.pi*k**4)/((c**2)*(h**3)))*integralvalue
print(sigma)