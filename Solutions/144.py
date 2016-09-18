import math

def getK(p, d):
    return -2 * (4*p[0]*d[0] + p[1]*d[1])/(4*d[0]**2 + d[1]**2)

def tangent(p):
    return -p[1], 4*p[0]

def getDirection(p, d0):
    t = tangent(p)
    norm = t[0]**2 + t[1]**2
    dot = (d0[0]*t[0]+d0[1]*t[1])/norm
    return -d0[0] + 2*dot*t[0], -d0[1] + 2*dot*t[1]

p0 = (0, 10.1)
p1 = (1.4, -9.6)
d0 = (p1[0]-p0[0], p1[1]-p0[1])

d = d0
p = p1
i = 0
while (0.01 < p[0]) | (p[0] < -0.01) | (p[1] < 0):
    d = getDirection(p, d)
    k = getK(p, d)
    p = (p[0] + k*d[0], p[1] + k*d[1])
    i += 1
print(i)
