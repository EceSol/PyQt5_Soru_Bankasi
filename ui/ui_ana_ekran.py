# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ana_ekran.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnYeniSoru = QtWidgets.QPushButton(self.centralwidget)
        self.btnYeniSoru.setObjectName("btnYeniSoru")
        self.verticalLayout.addWidget(self.btnYeniSoru)
        self.btnSoruSec = QtWidgets.QPushButton(self.centralwidget)
        self.btnSoruSec.setObjectName("btnSoruSec")
        self.verticalLayout.addWidget(self.btnSoruSec)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow - ana.ui"))
        self.btnYeniSoru.setText(_translate("MainWindow", "Yeni Soru Ekle"))
        self.btnSoruSec.setText(_translate("MainWindow", "Soru Seç"))
