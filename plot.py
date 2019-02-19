#!/usr/bin/python3
import re, sys
from matplotlib import pyplot

plotSlope = False

def centeredMovingAverage(values, order):
    if (order % 2) != 1:
        raise ValueError('Order has to be an odd number!')
    result = []
    for i in range(len(values)):
        s = values[i]
        n = 1
        for j in range(int(order/2)):
            if (i - j) >= 0:
                s += values[i-j]
                n += 1
            if (i + j) < len(values):
                s += values[i+j]
                n += 1
        result.append(s/n)
    return result

values = []
first = True
with open(sys.argv[1], 'r') as f:
    for l in f:
        if re.match(r'^[0-9]+\.[0-9]+$', l) is not None:
            if first:
                first = False
                # Skip first value, it may be corrupted.
            else:
                val = float(l)
                values.append(val)

if plotSlope:
    slope = [0]
    for i in range(len(values)):
        if i != 0:
            slope.append(values[i] - values[i-1])
        if i == 1:
            slope[0] = slope[1]

if plotSlope:
    pyplot.subplot(2, 1, 1)

pyplot.plot(values)
pyplot.grid(which='both')
pyplot.xlabel('time (seconds)')
pyplot.ylabel('temperature (centigrade)')

if plotSlope:
    pyplot.subplot(2, 1, 2)
    pyplot.plot(slope)
    pyplot.grid(which='both')
    pyplot.xlabel('time (seconds)')
    pyplot.ylabel('temperature slope (K/s)')

pyplot.show()
