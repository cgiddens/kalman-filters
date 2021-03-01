# A Kalman filter has two steps, the measurement step, and the prediction (motion) step.
# This is the measurement step.

# mu' = (1/(sigma2 + r2)) * (r2*mu + sigma2*nu)
# sigma2' = 1 / ((1/sigma2) + (1/r2))

mu = 10.
sigma2 = 4.

nu = 12.
r2 = 4.

# find mu'
# find sigma2'

import math

def update(mean1, var1, mean2, var2):
    mu_ = (1 / (var1 + var2)) * (var2*mean1 + var1*mean2)
    sigma2_ = 1 / ((1/var1) + (1/var2))
    return mu_, sigma2_

def predict(mean1, var1, mean2, var2):
    mu_ = mean1 + mean2
    sigma2_ = var1 + var2
    return mu_, sigma2_

print(update(10., 4., 12., 4.))
print(update(10., 8., 13., 2.))

print(predict(10., 4., 12., 4.))
