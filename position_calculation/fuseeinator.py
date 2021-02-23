import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from math import *
import function as func

n = 100000
dt = 1/10000
dt_ = 1/25

vfp = func.vfp_(n, func.fp)
ho = func.ho_(n)

h = func.high(vfp, dt)
h_ = func.high(vfp, dt_)
v = func.speed(vfp, dt)
t = np.linspace(0, dt*len(h), len(h))
t_ = np.linspace(0, dt_*len(h_), len(h_))
zo = np.zeros(len(h_))

ymax = max(h)


W = func.highC(1000)
C_ = W[0]
HI_ = W[1]

plt.plot(C_, HI_)
plt.show()

R = func.hmax()

FP = R[0]
VFP = R[1]
H = R[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(VFP, FP, H)
plt.show()

print(vfp, ymax, dt*len(h))

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(t, h, color = 'blue')
ax1.set_xlabel("time (s)")
ax1.set_ylabel("hight")
ax1.set_title("position (m)")
ax2.plot(t, v, color = 'red')
ax2.set_xlabel("time (s)")
ax2.set_ylabel("speed (m/s)")
ax2.set_title("speed")
plt.show()

plt.figure()
plt.ion()
plt.scatter([], [])

i = 0
while i < len(h_):
    plt.clf()
    plt.xlim([-1, 1])
    plt.ylim([0, ymax + 50])
    plt.scatter(zo[i], h_[i])
    plt.title("time = {}" .format(t_[i]))
    i = i + 1
    plt.pause(dt)
