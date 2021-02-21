import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from math import *

g = 9.8
m = 1.2
mp = 0.8
fp = 400
tp = 1
Cz = 0.75
K = 0.5
rho = 1.293
r = 0.05
h = 0.07
h_ = 0.3
S = (np.pi * r * np.sqrt((r*r) + (h*h))) + (np.pi * r**2 *h_)
k = (Cz * K * rho * S)

n = 100000
dt = 1/10000
dt_ = 1/25

def vfp_():
    i = 1
    m_ = m + mp
    v = 0.00000001
    ho = 0
    while i < n+1:
        m_ = m_ - (mp/n)
        v = v + ((fp*(tp/(n))*i)/m_) * np.log(1 + (mp/n)/m_) + (tp/n)*(-(k/m_)*(v**3/abs(v))-g)
        s = (fp*tp)/m * np.log((m+mp)/m) - g*tp
        ho = ho + v* (tp/n)
        i = i + 1
    return(v)

def ho():
    i = 1
    m_ = m + mp
    v = 0.00000001
    ho = 0
    while i < n+1:
        m_ = m_ - (mp/n)
        v = v + ((fp*(tp/(n))*i)/m_) * np.log(1 + (mp/n)/m_) + (tp/n)*(-(k/m_)*(v**3/abs(v))-g)
        s = (fp*tp)/m * np.log((m+mp)/m) - g*tp
        ho = ho + v* (tp/n)
        i = i + 1
    return(ho)

vfp = vfp_()
ho = ho()

def high(vfp, dt):
    t = tp
    h = ho
    H = []
    while h >= 0:
        vfp = vfp + dt*(-(k/m)*(vfp**3/abs(vfp))-g)
        h = h + vfp*dt
        H.append(h)
        t = t + dt
    return(H)

def highmax(vfp, dt):
    t = 0
    h = 0
    while vfp >= 0:
        vfp = vfp + dt*(-(k/m)*(vfp**3/abs(vfp))-g)
        h = h + vfp*dt
        t = t + dt
    return(h)

def speed(vfp, dt):
    t = tp
    h = ho
    V = []
    while h >= 0:
        vfp = vfp + dt*(-(k/m)*(vfp**3/abs(vfp))-g)
        h = h + vfp*dt
        V.append(vfp)
        t = t + dt
    return(V)

h = high(vfp, dt)
h_ = high(vfp, dt_)
v = speed(vfp, dt)
t = np.linspace(0, dt*len(h), len(h))
t_ = np.linspace(0, dt_*len(h_), len(h_))
zo = np.zeros(len(h_))

ymax = max(h)

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

H = []
VFP = []
FP = []
fp = 10
while fp < 1000:
    v = vfp_()
    H.append(highmax(v, dt_))
    VFP.append(v)
    FP.append(fp)
    fp = fp + 5

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(VFP, FP, H)
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
