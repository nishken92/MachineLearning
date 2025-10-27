
import numpy
import matplotlib.pyplot as plt

# Find the mean value using numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

# Find the standard deviation

y = numpy.std(speed)
print(y)

# Find the varience

z = numpy.var(speed)
print(z)

# Percentile

num = [30,30,30,40,50]
a = numpy.percentile(num, 75)
print(a)

num2 = [30,30,32,35,38,40,44]
b = numpy.percentile(num2,40)
print(b)
# Mathamatical Plotting Library
# Additional comments


b = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(b, 5)
plt.show()