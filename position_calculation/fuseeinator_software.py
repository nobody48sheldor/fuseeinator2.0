from PyQt5 import QtCore, QtGui, QtWidgets
import os


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

        self.actionLoad_File = QtWidgets.QAction(MainWindow)
        self.actionLoad_File.setObjectName("actionLoad_File")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(lambda: self.install_packages())

        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_2.triggered.connect(lambda: self.exit())

        self.menuSettings.addAction(self.actionupdate)
        self.menuSettings.addAction(self.actiongit_push)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionLoad_File)
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
        self.label.setText(_translate("MainWindow", "Propergol Rocket"))
        self.label_2.setText(_translate("MainWindow", "Type"))
        self.label_3.setText(_translate("MainWindow", "empty mass"))
        self.label_4.setText(_translate("MainWindow", "propellant mass"))
        self.label_5.setText(_translate("MainWindow", "propulsion force kN"))
        self.label_6.setText(_translate("MainWindow", "propulsion time"))
        self.checkBox.setText(_translate("MainWindow", "Use Setting"))

        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionupdate.setText(_translate("MainWindow", "git git pull"))
        self.actionupdate.setStatusTip(_translate("MainWindow", "get the last version of the code"))
        self.actionupdate.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actiongit_push.setText(_translate("MainWindow", "git push"))
        self.actiongit_push.setStatusTip(_translate("MainWindow", "push to the github repository your parametters"))
        self.actiongit_push.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionLoad_File.setText(_translate("MainWindow", "Load File"))
        self.actionLoad_File.setStatusTip(_translate("MainWindow", "Load a File for setting (not yet implemented)"))
        self.actionExit.setText(_translate("MainWindow", "Install Packages"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))

    def Run(self):
        if self.checkBox.isChecked() == True:
            if self.comboBox.currentIndex() == 0:
                with open("fi.txt", "w+") as propergol:
                    propergol.write("{}/".format(self.doubleSpinBox.value()))
                    propergol.write("{}/".format(self.doubleSpinBox_2.value()*10000))
                    propergol.write("{}/".format(self.doubleSpinBox_3.value()))
                    propergol.write("{}/0.6".format(self.doubleSpinBox_4.value()))
            if self.comboBox.currentIndex() == 1:
                with open("wr.txt", "w+") as waterrocket:
                    waterrocket.write("{}/".format(self.doubleSpinBox.value()))
                    waterrocket.write("{}/".format(self.doubleSpinBox_2.value()))
                    waterrocket.write("{}/".format(self.doubleSpinBox_3.value())*1000)
                    waterrocket.write("{}/0.6".format(self.doubleSpinBox_4.value()))

        if self.comboBox.currentIndex() == 0:
            os.startfile("fuseeinator_runner.py")

        if self.comboBox.currentIndex() == 1:
            os.startfile("waterrocket_runner.py")


    def type(self):
        if self.comboBox.currentIndex() == 0:
            self.label_4.setText("propellant mass")
            self.label_4.setGeometry(QtCore.QRect(310, 360, 400, 51))
            self.label_5.setText("propulsion force kN")
            self.label_6.setText("propulsion time")
            self.label_5.setGeometry(QtCore.QRect(235, 470, 475, 51))

        if self.comboBox.currentIndex() == 1:
            self.label_4.setText("pressure (hPa)")
            self.label_4.setGeometry(QtCore.QRect(345, 360, 400, 51))
            self.label_5.setText("rho (kg/m^3)")
            self.label_6.setText("Cz aerodynamic")
            self.label_5.setGeometry(QtCore.QRect(350, 470, 450, 51))

    def git_pull(self):
        os.startfile("git_pull.bat")

    def git_push(self):
        os.startfile("git_push.bat")

    def install_packages(self):
        os.startfile("packages.bat")

    def exit(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
