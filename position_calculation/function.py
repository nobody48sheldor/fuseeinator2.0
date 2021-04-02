from math import *
import numpy as np

g = 9.8
m = 1.2
mp = 0.8
fp = 500
tp = 1
Cz = 0.7
K = 0.5
rho = 1.293
rhoH = 1000
r = 0.025
h = 0.07
h_ = 0.4
S = (np.pi * r * np.sqrt((r*r) + (h*h)))
k = (Cz * K * rho * S)

Pr = 6*(10**5)
mp_ = 1
tpwr = (mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2))

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
        ho = ho + v* (tp/n)
        i = i + 1
    return(v)

def vfpc(n, fp, C):
    i = 1
    m_ = m + mp
    v = 0.00000001
    ho = 0
    k = (C * K * rho * S)
    while i < n+1:
        m_ = m_ - (mp/n)
        v = v + ((fp*(tp/(n))*i)/m_) * np.log(1 + (mp/n)/m_) + (tp/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (tp/n)
        i = i + 1
    return(v)

def vfpcwr(n, P, C):
    i = 1
    m_ = m + mp_
    v = 0.00000001
    ho = 0
    k = (C * K * rho * S)
    while i < n+1:
        m_ = m_ - (mp_/n)
        v = v + np.sqrt(2*P/rhoH) * np.log(1 + (mp_/n)/m_) + (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)
        i = i + 1
    return(v)

def vfpwr_(n, P):
    i = 1
    m_ = m + mp_
    v = 0.00000001
    ho = 0
    while i < n+1:
        m_ = m_ - (mp_/n)
        v = v + np.sqrt(2*P/rhoH) * np.log(1 + (mp_/n)/m_) + (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)
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
        ho = ho + v* (tp/n)
        i = i + 1
    return(ho)

def howr_(n):
    i = 1
    m_ = m + mp_
    v = 0.00000001
    ho = 0
    while i < n+1:
        m_ = m_ - (mp_/n)
        v = v + np.sqrt(2*Pr/rhoH) * np.log(1 + (mp_/n)/m_) + (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)
        i = i + 1
    return(ho)

ho = ho_(n)
howr = howr_(n)

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

def highwr(vfp, dt):
    t = tpwr
    h = howr
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

def highmaxC(vfp, dt, C):
    t = 0
    h = 0
    k = (C * K * rho * S)
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

def speedwr(vfp, dt):
    t = tpwr
    h = howr
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

def hmaxwr():
    H = []
    VFP = []
    P = []
    p = 100000
    while p < 2000000:
        v = vfpwr_(n, p)
        H.append(highmax(v, dt_))
        VFP.append(v)
        P.append(p)
        p = p + 2000
        if p%(20000) == 0:
            print(p/(20000), "%")
    R = []
    R.append(P)
    R.append(VFP)
    R.append(H)
    return(R)

def highC(n):
    dt = 1/n
    c = np.linspace(0, 1.5, n)
    R = []
    H = []
    i = 0
    while i < n:
        C = c[i]
        vfp = vfpc(n, fp, C)
        h = highmaxC(vfp, dt, C)
        H.append(h)
        i = i + 1
    R.append(c)
    R.append(H)
    return(R)

def highCwr(n):
    dt = 1/n
    c = np.linspace(0, 1.5, n)
    R = []
    H = []
    i = 0
    while i < n:
        C = c[i]
        vfp = vfpcwr(n, Pr, C)
        h = highmaxC(vfp, dt, C)
        H.append(h)
        i = i + 1
    R.append(c)
    R.append(H)
    return(R)
