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

R = func.hmax()

FP = R[0]
VFP = R[1]
H = R[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(VFP, FP, H)
ax.set_xlabel('end propultion velocity (m/s)')
ax.set_ylabel('propulsion force (N)')
ax.set_zlabel('max height (m)')
ax.set_title("height depending on end propulsion velocity and propulsion force [propergol rocket]")
plt.show()

print("empty rocket mass :          ", func.m, " (kg)")
print("fuel mass :                  ", func.mp, " (kg)")
print("upward force :               ", func.fp, " (N)")
print("propulsion time :            ", func.tp, " (s)")
print("coefficient of drag(z) :     ", func.Cz)
print("frontal area :               ", func.S, " (m^2)")
print("\n")
print("end propultion speed :       ", vfp, " (m/s)")
print("max height :                 ", ymax, " (m)")
print("duration of free flight :    ", dt*len(h), " (s)")

fig = plt.figure()

ax1 = plt.subplot(212)
ax1.plot(C_, HI_)
ax1.set_xlabel('drag coefficient')
ax1.set_ylabel('max height (m)')
ax1.set_title("hmax(Cz) [propergol rocket]")

ax2 = plt.subplot(221)
ax2.plot(t, h, color = 'blue')
ax2.set_xlabel("time (s)")
ax2.set_ylabel("height (m)")
ax2.set_title("height [propergol rocket]")

ax3 = plt.subplot(222)
ax3.plot(t, v, color = 'red')
ax3.set_xlabel("time (s)")
ax3.set_ylabel("speed (m/s)")
ax3.set_title("speed [propergol rocket]")

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
