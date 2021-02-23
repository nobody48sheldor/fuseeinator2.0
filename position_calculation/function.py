from math import *
import numpy as np

g = 9.8
m = 1.2
mp = 0.8
fp = 400
tp = 1
Cz = 0.7
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

def vfp_(n, fp):
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

def vfpc(n, fp, Cz):
    i = 1
    m_ = m + mp
    v = 0.00000001
    ho = 0
    k = (Cz * K * rho * S)
    while i < n+1:
        m_ = m_ - (mp/n)
        v = v + ((fp*(tp/(n))*i)/m_) * np.log(1 + (mp/n)/m_) + (tp/n)*(-(k/m_)*(v**3/abs(v))-g)
        s = (fp*tp)/m * np.log((m+mp)/m) - g*tp
        ho = ho + v* (tp/n)
        i = i + 1
    return(v)

def ho_(n):
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

vfp = vfp_(n, fp)
ho = ho_(n)

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

def highmaxC(vfp, dt, Cz):
    t = 0
    h = 0
    k = (Cz * K * rho * S)
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

def hmax():
    H = []
    VFP = []
    FP = []
    fp = 10
    while fp < 1000:
        v = vfp_(n, fp)
        H.append(highmax(v, dt_))
        VFP.append(v)
        FP.append(fp)
        fp = fp + 5
        if fp%(10) == 0:
            print(fp/(10), "%")
    R = []
    R.append(FP)
    R.append(VFP)
    R.append(H)
    return(R)

def highC(n):
    dt = 1/n
    c = np.linspace(0, 1.1, n)
    R = []
    H = []
    i = 0
    while i < n:
        C = c[i]
        vfp = vfpc(n, 400, C)
        h = highmaxC(vfp, dt, C)
        H.append(h)
        i = i + 1
    R.append(c)
    R.append(H)
    return(R)
print("debug")
