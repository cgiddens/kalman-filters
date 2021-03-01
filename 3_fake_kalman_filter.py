# A Kalman filter has two steps, the measurement step, and the prediction (motion) step.
# This is the measurement step.

# mu' = (1/(sigma2 + r2)) * (r2*mu + sigma2*nu)
# sigma2' = 1 / ((1/sigma2) + (1/r2))

import math

def update(mean1, var1, mean2, var2):
    mu_ = (1 / (var1 + var2)) * (var2*mean1 + var1*mean2)
    sigma2_ = 1 / ((1/var1) + (1/var2))
    return [mu_, sigma2_]

def predict(mean1, var1, mean2, var2):
    mu_ = mean1 + mean2
    sigma2_ = var1 + var2
    return [mu_, sigma2_]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)

print([mu, sig])
