# Gaussian formula:

# f(x) = (1/sqrt(2*pi*sigma^2)) * exp(-0.5 * (x - mu)^2 / sigma^2)

# Givens:
# mu = 10
# sigma^2 = 4
# x = 8

import math

mu = 10
sigma = 2

x = range(0,20)
gaussian = []

def f(mu, sigma, x):
    return (1/math.sqrt(2*math.pi*(sigma**2))) * math.exp(-0.5 * (i - mu)**2 / sigma**2)

for i in x:
    gaussian.append(f(mu, sigma, i))

print(gaussian)
