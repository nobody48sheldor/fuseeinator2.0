import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from functools import cache
from matplotlib import style
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
import time
from math import *
import function as func

style.use('dark_background')

def main():
    time_0 = time.time()
    n = 100000
    dt = 1/n
    dt_ = 1/25

    vfp = func.vfpwr_(n, func.Pr)
    ho = func.howr_(n)

    token = "NzQ4MzMyNjU4MTQ0MTgyMzQz.X6chQA.JQvyyhi7toxdYrai8pnL-1i_9FY"
    id = '811258320467787828'

    executor = ProcessPoolExecutor(max_workers=10)

    p1 = executor.submit(func.hvfpwr_, n, func.Pr)
    p2 = executor.submit(func.highwr, vfp, dt)
    p3 = executor.submit(func.vvfpwr_, n, func.Pr)
    p4 = executor.submit(func.speedwr, vfp, dt)
    p5 = executor.submit(func.hmaxwr)

    hprop = p1.result()
    h = p2.result()
    h_ = func.highwr(vfp, dt_)
    vprop = p3.result()
    v = p4.result()
    tprop = np.linspace(0, func.tpwr, len(func.hvfpwr_(n, func.Pr)))
    t = np.linspace(func.tpwr, dt*len(h) + func.tpwr, len(h))
    t_ = np.linspace(func.tpwr, dt_*len(h_) + func.tpwr, len(h_))
    zo = np.zeros(len(h_))

    ymax = max(h)


    W = func.highCwr(1000)
    C_ = W[0]
    HI_ = W[1]

    R = p5.result()

    P = R[0]
    VFP = R[1]
    H = R[2]

    print("empty rocket mass :          ", func.m, " (kg)")
    print("fuel mass :                  ", func.mp_, " (kg)")
    print("pressure :                   ", func.Pr, " (Pa)")
    print("propulsion time :            ", func.tpwr, " (s)")
    print("coefficient of drag(z) :     ", func.Cz)
    print("frontal area :               ", func.S, " (m^2)")
    print("\n")
    print("end propultion speed :       ", vfp, " (m/s)")
    print("max height :                 ", ymax, " (m)")
    print("duration of free flight :    ", dt*len(h), " (s)")

    func.send_message(token, id, "calculation done for fuseeinator 2.0 at {0} and it took {1} seconds https://i.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif".format(datetime.now(), time.time() - time_0))
    input("\\\\")

    plt.ion()
    fig = plt.figure()

    ax1 = plt.subplot2grid((3,3), (0,0), rowspan=2, colspan= 2, projection = '3d')
    ax3 = plt.subplot2grid((3,3), (0,2), rowspan=1, colspan= 1)
    ax4 = plt.subplot2grid((3,3), (1,2), rowspan=1, colspan= 1)
    ax2 = plt.subplot2grid((3,3), (2,0), rowspan=1, colspan= 2)
    ax5 = plt.subplot2grid((3,3), (2,2), rowspan=1, colspan= 1)

    ax1.plot(VFP, P, H, color = 'yellow')
    ax1.set_xlabel('end propultion velocity (m/s)')
    ax1.set_ylabel('Pressure (Pa)')
    ax1.set_zlabel('max height (m)')
    ax1.set_title("height depending on end propulsion velocity and propulsion force [water rocket]")

    ax2.plot(C_, HI_, color = "red")
    ax2.set_xlabel('drag coefficient')
    ax2.set_ylabel('max height (m)')
    ax2.set_title("hmax(Cz) [water rocket]")

    ax3.plot(t, h, color = 'blue')
    ax3.plot(tprop, hprop, color = 'green')
    ax3.set_xlabel("time (s)")
    ax3.set_ylabel("height (m)")
    ax3.set_title("height [water rocket]")

    ax4.plot(t, v, color = 'red')
    ax4.plot(tprop, vprop, color = 'green')
    ax4.set_xlabel("time (s)")
    ax4.set_ylabel("speed (m/s)")
    ax4.set_title("speed [water rocket]")

    i = 0
    while i < len(h_):
        ax5.clear()
        ax5.set_xlim([-1, 1])
        ax5.set_ylim([0, ymax + 50])
        ax5.scatter(zo[i], h_[i], color = 'green')
        ax5.set_title("time = {}" .format(t_[i]))

        if i + 2 == len(h_):
            dt = 100000
        i = i + 1
        plt.pause(dt)
