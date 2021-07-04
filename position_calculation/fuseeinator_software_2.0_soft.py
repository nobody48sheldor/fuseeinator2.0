from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from functools import cache
from matplotlib import style
import time
from math import *

style.use('dark_background')

Cz = 0.6
m = 1
mp = 1
fp = 500
tp = 1

rhoH = 1000
Pr = 60000
mp_ = 1

g = 9.8
K = 0.5
rho = 1.293
r = 0.025
h = 0.07
S = (np.pi * r * np.sqrt((r*r) + (h*h)))
k = (Cz * K * rho * S)

tpwr = (mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2))
n = 100000
dt = 1/n
dt_ = 1/25

def vfp_(n, fp, m, mp, tp):
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

@cache
def hvfp_(n, fp, m, mp, tp):
    i = 1
    m_ = m + mp
    v = 0.00000001
    ho = 0
    H = []
    while i < n+1:
        m_ = m_ - (mp/n)
        v = v + ((fp*(tp/(n))*i)/m_) * np.log(1 + (mp/n)/m_) + (tp/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (tp/n)
        H.append(ho)
        i = i + 1
    return(H)

@cache
def vvfp_(n, fp, m, mp, tp):
    i = 1
    m_ = m + mp
    v = 0.00000001
    ho = 0
    V = []
    while i < n+1:
        m_ = m_ - (mp/n)
        v = v + ((fp*(tp/(n))*i)/m_) * np.log(1 + (mp/n)/m_) + (tp/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (tp/n)
        V.append(v)
        i = i + 1
    return(V)


def vfpc(n, fp, C, m, mp, tp):
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

def vfpcwr(n, Pr, C, m, mp_, rhoH):
    i = 1
    m_ = m + mp_
    v = 0.00000001
    ho = 0
    k = (C * K * rho * S)
    while i < n+1:
        m_ = m_ - (mp_/n)
        v = v + np.sqrt(2*Pr/rhoH) * np.log(1 + (mp_/n)/m_) + (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2)))/n)
        i = i + 1
    return(v)

@cache
def vfpwr_(n, Pr, m, mp_, rhoH):
    i = 1
    m_ = m + mp_
    v = 0.00000001
    ho = 0
    while i < n+1:
        m_ = m_ - (mp_/n)
        v = v + np.sqrt(2*Pr/rhoH) * np.log(1 + (mp_/n)/m_) + (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2)))/n)
        i = i + 1
    return(v)

@cache
def hvfpwr_(n, Pr, m, mp_, rhoH):
    i = 1
    m_ = m + mp_
    v = 0.00000001
    ho = 0
    H = []
    while i < n+1:
        m_ = m_ - (mp_/n)
        v = v + np.sqrt(2*Pr/rhoH) * np.log(1 + (mp_/n)/m_) + (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2)))/n)
        H.append(ho)
        i = i + 1
    return(H)

def vvfpwr_(n, Pr, m, mp_, rhoH):
    i = 1
    m_ = m + mp_
    v = 0.00000001
    ho = 0
    V = []
    while i < n+1:
        m_ = m_ - (mp_/n)
        v = v + np.sqrt(2*Pr/rhoH) * np.log(1 + (mp_/n)/m_) + (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2)))/n)
        V.append(v)
        i = i + 1
    return(V)

def ho_(n, m, mp, tp, fp):
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

def howr_(n, m, mp_, rhoH, Pr):
    i = 1
    m_ = m + mp_
    v = 0.00000001
    ho = 0
    while i < n+1:
        m_ = m_ - (mp_/n)
        v = v + np.sqrt(2*Pr/rhoH) * np.log(1 + (mp_/n)/m_) + (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*1.4))/n)*(-(k/m_)*(v**3/abs(v))-g)
        ho = ho + v* (((mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2)))/n)
        i = i + 1
    return(ho)

@cache
def high(vfp, dt, m, mp, tp, fp):
    t = tp
    h = ho_(n, m, mp, tp, fp)
    H = []
    while h >= 0:
        vfp = vfp + dt*(-(k/m)*(vfp**3/abs(vfp))-g)
        h = h + vfp*dt
        H.append(h)
        t = t + dt
    return(H)

@cache
def highwr(vfp, dt, m, mp_, rhoH, Pr):
    tpwr = (mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2))
    t = tpwr
    h = howr_(n, m, mp_, rhoH, Pr)
    H = []
    while h >= 0:
        vfp = vfp + dt*(-(k/m)*(vfp**3/abs(vfp))-g)
        h = h + vfp*dt
        H.append(h)
        t = t + dt
    return(H)

def highmax(vfp, dt, m, mp, tp):
    t = 0
    h = 0
    while vfp >= 0:
        vfp = vfp + dt*(-(k/m)*(vfp**3/abs(vfp))-g)
        h = h + vfp*dt
        t = t + dt
    return(h)

def highmaxC(vfp, dt, C, m, mp, tp):
    t = 0
    h = 0
    k = C * K * rho * S
    while vfp >= 0:
        vfp = vfp + dt*(-((k/m)*(vfp**3/abs(vfp)))-g)
        h = h + vfp*dt
        t = t + dt
    return(h)

def speed(vfp, dt, m, mp, tp, fp):
    t = tp
    h = ho_(n, m, mp, tp, fp)
    V = []
    while h >= 0:
        vfp = vfp + dt*(-(k/m)*(vfp**3/abs(vfp))-g)
        h = h + vfp*dt
        V.append(vfp)
        t = t + dt
    return(V)

def speedwr(vfp, dt, m, mp_, rhoH, Pr):
    tpwr = (mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2))
    t = tpwr
    h = howr_(n, m, mp_, rhoH, Pr)
    V = []
    while h >= 0:
        vfp = vfp + dt*(-(k/m)*(vfp**3/abs(vfp))-g)
        h = h + vfp*dt
        V.append(vfp)
        t = t + dt
    return(V)

@cache
def hmax(m, mp, tp):
    H = []
    VFP = []
    FP = []
    fp = 10
    while fp < 1000:
        v = vfp_(n, fp, m, mp, tp)
        H.append(highmax(v, dt_, m, mp, tp))
        VFP.append(v)
        FP.append(fp)
        fp = fp + 5
        if fp%(10) == 0:
            print(fp/(10), "%")
            #ui.label_7.setText("{} %".format(fp/(10)))
    R = []
    R.append(FP)
    R.append(VFP)
    R.append(H)
    #ui.label_7.setText("")
    return(R)

@cache
def hmaxwr(m, mp_, rhoH):
    H = []
    VFP = []
    P = []
    p = 100000
    while p < 2000000:
        v = vfpwr_(n, p, m, mp_, rhoH)
        H.append(highmax(v, dt_, m, mp_, rhoH))
        VFP.append(v)
        P.append(p)
        p = p + 20000
        if p%(20000) == 0:
            print(p/(20000), "%")
            #ui.label_7.setText("{} %".format(p/20000))
    R = []
    R.append(P)
    R.append(VFP)
    R.append(H)
    #ui.label_7.setText("")
    return(R)

def highC(n, m, mp, tp):
    dt = 1/n
    c = np.linspace(0, 1.5, n)
    R = []
    H = []
    i = 0
    while i < n:
        C = c[i]
        vfp = vfpc(n, fp, C, m, mp, tp)
        h = highmaxC(vfp, dt, C, m, mp, tp)
        H.append(h)
        i = i + 1
    R.append(c)
    R.append(H)
    return(R)

def highCwr(n, m, mp_, rhoH, Pr):
    dt = 1/n
    c = np.linspace(0, 1.5, n)
    R = []
    H = []
    i = 0
    while i < n:
        C = c[i]
        vfp = vfpcwr(n, Pr, C, m, mp_, rhoH)
        h = highmaxC(vfp, dt, C, m, mp_, rhoH)
        H.append(h)
        i = i + 1
    R.append(c)
    R.append(H)
    return(R)


@cache
def fuseeinator_run(m, mp, tp, fp):
    n = 100000
    dt = 1/n
    dt_ = 1/25
    vfp = vfp_(n, fp, m, mp, tp)
    ho = ho_(n, m, mp, tp, fp)

    hprop = hvfp_(n, fp, m, mp, tp)
    h = high(vfp, dt, m, mp, tp, fp)
    h_ = high(vfp, dt_, m, mp, tp, fp)
    vprop = vvfp_(n, fp, m, mp, tp)
    v = speed(vfp, dt, m, mp, tp, fp)
    tprop = np.linspace(0, tp, len(hvfp_(n, fp, m, mp, tp)))
    t = np.linspace(tp, dt*len(h) + tp, len(h))
    t_ = np.linspace(tp, dt_*len(h_) + tp, len(h_))
    zo = np.zeros(len(h_))

    ymax = max(h)


    W = highC(1000, m, mp, tp)
    C_ = W[0]
    HI_ = W[1]

    R = hmax(m, mp, tp)

    FP = R[0]
    VFP = R[1]
    H = R[2]

    #plt.ion()
    fig = plt.figure()

    ax1 = plt.subplot2grid((3,3), (0,0), rowspan=2, colspan= 2, projection = '3d')
    ax3 = plt.subplot2grid((3,3), (0,2), rowspan=1, colspan= 1)
    ax4 = plt.subplot2grid((3,3), (1,2), rowspan=1, colspan= 1)
    ax2 = plt.subplot2grid((3,3), (2,0), rowspan=1, colspan= 2)
    ax5 = plt.subplot2grid((3,3), (2,2), rowspan=1, colspan= 1)

    ax1.plot(VFP, FP, H, color = 'yellow')
    ax1.set_xlabel('end propultion velocity (m/s)')
    ax1.set_ylabel('propulsion force (N)')
    ax1.set_zlabel('max height (m)')
    ax1.set_title("height depending on end propulsion velocity and propulsion force [propergol rocket]")

    ax2.plot(C_, HI_, color = 'red')
    ax2.set_xlabel('drag coefficient')
    ax2.set_ylabel('max height (m)')
    ax2.set_title("hmax(Cz) [propergol rocket]")

    ax3.plot(t, h, color = 'blue')
    ax3.plot(tprop, hprop, color = 'green')
    ax3.set_xlabel("time (s)")
    ax3.set_ylabel("height (m)")
    ax3.set_title("height [propergol rocket]")

    ax4.plot(t, v, color = 'red')
    ax4.plot(tprop, vprop, color = 'green')
    ax4.set_xlabel("time (s)")
    ax4.set_ylabel("speed (m/s)")
    ax4.set_title("speed [propergol rocket]")

    #i = 0
    #while i < len(h_):
        #ax5.clear()
    ax5.set_xlim([-1, 1])
    ax5.set_ylim([0, ymax + 50])
    ax5.scatter(zo[int(len(zo)/2)], h_[int(len(h_)/2)], color = 'green')
    ax5.set_title("time = {}" .format(t_[int(len(h_)/2)]))
    plt.tight_layout()
    plt.show()

        #if i + 2 == len(h_):
        #    dt = 100000

        #i = i + 1
        #plt.pause(dt)


def waterrocket_run(m, mp_, rhoH, Pr):
    n = 100000
    dt = 1/n
    dt_ = 1/25
    tpwr = (mp_/rhoH)/(np.sqrt(2*Pr/rhoH)*np.pi*((r/2)**2))
    vfp = vfpwr_(n, Pr, m, mp_, rhoH)
    ho = howr_(n, m, mp_, rhoH, Pr)

    hprop = hvfpwr_(n, Pr, m, mp_, rhoH)
    h = highwr(vfp, dt, m, mp_, rhoH, Pr)
    h_ = highwr(vfp, dt_, m, mp_, rhoH, Pr)
    vprop = vvfpwr_(n, Pr, m, mp_, rhoH)
    v = speedwr(vfp, dt, m, mp_, rhoH, Pr)
    tprop = np.linspace(0, tpwr, len(hvfpwr_(n, Pr, m, mp_, rhoH)))
    t = np.linspace(tpwr, dt*len(h) + tpwr, len(h))
    tv = np.linspace(tpwr, dt*len(v) + tpwr, len(v))
    t_ = np.linspace(tpwr, dt_*len(h_) + tpwr, len(h_))
    zo = np.zeros(len(h_))

    ymax = max(h)


    W = highCwr(1000, m, mp_, rhoH, Pr)
    C_ = W[0]
    HI_ = W[1]
    R = hmaxwr(m, mp_, rhoH)


    P = R[0]
    VFP = R[1]
    H = R[2]

    #plt.ion()
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

    ax4.plot(tv, v, color = 'red')
    ax4.plot(tprop, vprop, color = 'green')
    ax4.set_xlabel("time (s)")
    ax4.set_ylabel("speed (m/s)")
    ax4.set_title("speed [water rocket]")

    #i = 0
    #while i < len(h_):
        #ax5.clear()
    ax5.set_xlim([-1, 1])
    ax5.set_ylim([0, ymax + 50])
    ax5.scatter(zo[int(len(zo)/2)], h_[int(len(h_)/2)], color = 'green')
    ax5.set_title("time = {}" .format(t_[int(len(h_)/2)]))
    plt.tight_layout()
    plt.show()

        #if i + 2 == len(h_):
        #    dt = 100000

        #i = i + 1
        #plt.pause(dt)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 960)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_software.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(227, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.RunButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunButton.setGeometry(QtCore.QRect(135, 700, 450, 200))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(72)
        self.RunButton.setFont(font)
        self.RunButton.setStyleSheet("background-color: rgb(10, 10, 10);\n"
"selection-background-color: rgb(4, 4, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(170, 0, 0);")
        self.RunButton.setObjectName("RunButton")
        self.RunButton.clicked.connect(self.Run)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(35, 30, 650, 65))
        font = QtGui.QFont()
        font.setFamily("Insaniburger")
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 150, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Insaniburger")
        font.setPointSize(18)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("propergol")
        self.comboBox.addItem("water")
        self.comboBox.activated.connect(self.type)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 147, 120, 51))
        font = QtGui.QFont()
        font.setFamily("Insaniburger")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(375, 250, 270, 51))
        font = QtGui.QFont()
        font.setFamily("Insaniburger")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 360, 400, 51))
        font = QtGui.QFont()
        font.setFamily("Insaniburger")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(235, 470, 475, 51))
        font = QtGui.QFont()
        font.setFamily("Insaniburger")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 580, 380, 51))
        font = QtGui.QFont()
        font.setFamily("Insaniburger")
        font.setPointSize(28)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(640, 780, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Insaniburger")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(90, 254, 100, 45))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(90, 363, 100, 45))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")

        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(90, 475, 100, 45))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")

        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(90, 585, 100, 45))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QtCore.QRect(30, 652, 155, 40))
        font6 = QtGui.QFont()
        font6.setFamily(u"Impact")
        font6.setPointSize(16)
        self.checkBox.setFont(font6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionupdate = QtWidgets.QAction(MainWindow)
        self.actionupdate.setObjectName("actionupdate")
        self.actionupdate.triggered.connect(lambda: self.git_pull())

        self.actiongit_push = QtWidgets.QAction(MainWindow)
        self.actiongit_push.setObjectName("actiongit_push")
        self.actiongit_push.triggered.connect(lambda: self.git_push())

        self.actionSave_Figure = QtWidgets.QAction(MainWindow)
        self.actionSave_Figure.setObjectName("actionSave_Figure")
        self.actionSave_Figure.triggered.connect(lambda: plt.savefig("figure_fuseeinator_{}.png".format(time.time())))

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(lambda: self.install_packages())

        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_2.triggered.connect(lambda: self.exit())

        self.menuSettings.addAction(self.actionupdate)
        self.menuSettings.addAction(self.actiongit_push)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionSave_Figure)
        self.menuSettings.addAction(self.actionExit)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fuseeinator"))
        self.RunButton.setText(_translate("MainWindow", "RUN"))
        self.RunButton.setShortcut(_translate("MainWindow", "e, e"))
        self.label.setText(_translate("MainWindow", "Propergol Rocket"))
        self.label_2.setText(_translate("MainWindow", "Type"))
        self.label_3.setText(_translate("MainWindow", "empty mass"))
        self.label_4.setText(_translate("MainWindow", "propellant mass"))
        self.label_5.setText(_translate("MainWindow", "propulsion force kN"))
        self.label_6.setText(_translate("MainWindow", "propulsion time"))
        self.label_7.setText(_translate("MainWindow", " . "))
        self.checkBox.setText(_translate("MainWindow", "Use Setting"))

        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionupdate.setText(_translate("MainWindow", "git git pull"))
        self.actionupdate.setStatusTip(_translate("MainWindow", "get the last version of the code"))
        self.actionupdate.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actiongit_push.setText(_translate("MainWindow", "git push"))
        self.actiongit_push.setStatusTip(_translate("MainWindow", "push to the github repository your parametters"))
        self.actiongit_push.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionSave_Figure.setText(_translate("MainWindow", "Save Figure"))
        self.actionSave_Figure.setShortcut(_translate("MainWindow", "Ctrl+R, Ctrl+F"))
        self.actionSave_Figure.setStatusTip(_translate("MainWindow", "When the plot is displayed, hit this button to save the figure"))
        self.actionExit.setText(_translate("MainWindow", "Install Packages"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+i, Ctrl+p"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionExit_2.setShortcut(_translate("MainWindow", "Escape, Escape"))

    def Run(self):
        self.label_7.setText("...")
        if self.checkBox.isChecked() == True:
            if self.comboBox.currentIndex() == 0:
                m = self.doubleSpinBox.value()
                mp = self.doubleSpinBox_2.value()
                fp = self.doubleSpinBox_3.value()*1000
                tp = self.doubleSpinBox_4.value()
                Cz = 0.6
                fuseeinator_run(m, mp, tp, fp)
            if self.comboBox.currentIndex() == 1:
                m = self.doubleSpinBox.value()
                mp_ = self.doubleSpinBox_2.value()
                Pr = self.doubleSpinBox_3.value()*100000
                rhoH = self.doubleSpinBox_4.value()*1000
                Cz = 0.7
                waterrocket_run(m, mp_, rhoH, Pr)
        if self.checkBox.isChecked() == False:
            if self.comboBox.currentIndex() == 0:
                m = 1.2
                mp = 1
                fp = 500
                tp = 1
                Cz = 0.6
                fuseeinator_run(m, mp, tp, fp)
                self.label_7.setText(" . ")
            if self.comboBox.currentIndex() == 1:
                m = 0.8
                mp_ = 1
                rhoH = 1000
                Pr = 600000
                Cz = 0.7
                waterrocket_run(m, mp_, rhoH, Pr)
                self.label_7.setText(" . ")


    def type(self):
        if self.comboBox.currentIndex() == 0:
            self.label_4.setText("propellant mass")
            self.label_5.setText("propulsion force kN")
            self.label_6.setText("propulsion time")
            self.label_5.setGeometry(QtCore.QRect(235, 470, 475, 51))
            self.label_6.setGeometry(QtCore.QRect(310, 580, 380, 51))
            type = 0

        if self.comboBox.currentIndex() == 1:
            self.label_4.setText("mass propellant")
            self.label_5.setText("pressure (bar)")
            self.label_6.setText("rho (kg/dm^3)")
            self.label_5.setGeometry(QtCore.QRect(350, 470, 450, 51))
            self.label_6.setGeometry(QtCore.QRect(350, 580, 380, 51))
            type = 1

    def git_pull(self):
        os.startfile("position_calculation\git_pull.bat")

    def git_push(self):
        os.startfile("position_calculation\git_push.bat")

    def install_packages(self):
        os.startfile("position_calculation\packages.bat")

    def exit(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
