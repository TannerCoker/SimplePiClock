# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
from datetime import datetime
import time as tmod


#pi screen is 720x576

class Ui_SimplePiClock(object):
    SCREEN_WIDTH = 720
    SCREEN_HEIGHT = 576

    def setupUi(self, SimplePiClock):
        SimplePiClock.setObjectName("SimplePiClock")

        SimplePiClock.setEnabled(True)
        SimplePiClock.resize(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        SimplePiClock.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(SimplePiClock)
        self.centralwidget.setObjectName("centralwidget")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)

        self.timeLabel.setGeometry(QtCore.QRect((int)(self.SCREEN_WIDTH/2 - (421/2)), (int)(self.SCREEN_HEIGHT/2 - 30), 421, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect((int)(self.SCREEN_WIDTH/2 - (421/2)), (int)(self.SCREEN_HEIGHT/2), 421, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        SimplePiClock.setCentralWidget(self.centralwidget)


        self.retranslateUi(SimplePiClock)
        QtCore.QMetaObject.connectSlotsByName(SimplePiClock)


    def retranslateUi(self, SimplePiClock):
        _translate = QtCore.QCoreApplication.translate
        SimplePiClock.setWindowTitle(_translate("SimplePiClock", "SimplePiClock"))
        
        if keyboard.is_pressed('esc'):
            sys.exit(app.exec_())

        curTime = datetime.now()

        time = curTime.strftime("%H:%M:%S")
        date = curTime.strftime("%m/%d/%y")

        self.timeLabel.setText(_translate("SimplePiClock", time))
        self.label.setText(_translate("SimplePiClock", date))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SimplePiClock = QtWidgets.QMainWindow()
    ui = Ui_SimplePiClock()
    ui.setupUi(SimplePiClock)
    SimplePiClock.show()

    def update_time():
        ui.retranslateUi(SimplePiClock)

    timer = QtCore.QTimer()
    timer.timeout.connect(update_time)
    timer.start(1000)

    sys.exit(app.exec_())