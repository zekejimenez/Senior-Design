# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Funct_Demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

from DEV1 import Feed_Now, Feed_Later

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Feed_Now = QtWidgets.QPushButton(self.centralwidget)
        self.Feed_Now.setGeometry(QtCore.QRect(60, 40, 131, 81))
        self.Feed_Now.setObjectName("Feed_Now")

        self.Feed_In_30 = QtWidgets.QPushButton(self.centralwidget)
        self.Feed_In_30.setGeometry(QtCore.QRect(250, 40, 131, 81))
        self.Feed_In_30.setObjectName("Feed_In_30")

        self.Check_Weight = QtWidgets.QPushButton(self.centralwidget)
        self.Check_Weight.setGeometry(QtCore.QRect(80, 160, 301, 51))
        self.Check_Weight.setObjectName("Check_Weight")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        ##Implementing Buttons
        self.Feed_Now.clicked.connect(Feed_Now)
        self.Feed_In_30.clicked.connect(lambda: Feed_Later(30))

        def update_voltage():
            ##read in pin voltages.
            self.Feed_Now.setText("update")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Feed_Now.setText(_translate("MainWindow", "Feed Now"))
        self.Feed_In_30.setText(_translate("MainWindow", "Feed In 30 Seconds"))
        self.Check_Weight.setText(_translate("MainWindow", "Check Weight"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    

    timer = QtCore.QTimer()
    timer.timeout.connect(update_voltage)
    timer.start(10000)


    sys.exit(app.exec_())
