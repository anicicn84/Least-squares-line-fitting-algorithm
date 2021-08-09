import matplotlib.pyplot as plt
import numpy as np

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
y = [0.99, 2.3, 2.9, 4.01, 4.85, 5.80, 7.2]
size = 7

plt.plot(x, y, 'go')
plt.ylabel('some numbers')

# Algorithm goes here
xsum = 0
x2sum = 0
ysum = 0
xysum = 0    
slope = 0
intercept = 0

for i in range(size):
    xsum = xsum + x[i]
    ysum = ysum + y[i]
    x2sum = x2sum + x[i]**2
    xysum = xysum + x[i] * y[i]

slope = (size * xysum - xsum * ysum) / (size * x2sum - xsum * xsum)
intercept = (x2sum * ysum - xsum * xysum) / (x2sum * size - xsum * xsum)
y_fit = []

for i in range(size):
    y_fit.append(slope * x[i] + intercept)

plt.plot(x, y_fit, 'r')

plt.show()


#t = np.arange(0., 5., 0.2)
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()

