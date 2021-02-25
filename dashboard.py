# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import dirname, abspath

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 690)
        MainWindow.setMinimumSize(QtCore.QSize(920, 690))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.up_button = QtWidgets.QPushButton(self.centralwidget)
        self.up_button.setEnabled(False)
        self.up_button.setGeometry(QtCore.QRect(130, 610, 61, 51))
        self.up_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/imgs/left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_button.setIcon(icon1)
        self.up_button.setObjectName("up_button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 0, 800, 600))
        self.widget.setMinimumSize(QtCore.QSize(800, 600))
        self.widget.setObjectName("widget")
        self.down_button = QtWidgets.QPushButton(self.centralwidget)
        self.down_button.setEnabled(False)
        self.down_button.setGeometry(QtCore.QRect(287, 610, 61, 51))
        self.down_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/imgs/right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_button.setIcon(icon2)
        self.down_button.setObjectName("down_button")
        self.openfile_button = QtWidgets.QPushButton(self.centralwidget)
        self.openfile_button.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.openfile_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/imgs/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openfile_button.setIcon(icon3)
        self.openfile_button.setIconSize(QtCore.QSize(30, 30))
        self.openfile_button.setObjectName("openfile_button")
        self.pagename = QtWidgets.QLabel(self.centralwidget)
        self.pagename.setGeometry(QtCore.QRect(194, 625, 91, 16))
        self.pagename.setAlignment(QtCore.Qt.AlignCenter)
        self.pagename.setObjectName("pagename")
        self.pagename.hide()
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setEnabled(False)
        self.search_button.setGeometry(QtCore.QRect(0, 50, 61, 51))
        self.search_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/imgs/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon4)
        self.search_button.setIconSize(QtCore.QSize(30, 30))
        self.search_button.setObjectName("search_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setEnabled(False)
        self.save_button.setGeometry(QtCore.QRect(0, 100, 61, 51))
        self.save_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/imgs/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon5)
        self.save_button.setIconSize(QtCore.QSize(30, 30))
        self.save_button.setObjectName("save_button")
        self.info_button = QtWidgets.QPushButton(self.centralwidget)
        self.info_button.setEnabled(True)
        self.info_button.setGeometry(QtCore.QRect(0, 150, 61, 51))
        self.info_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/imgs/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_button.setIcon(icon6)
        self.info_button.setIconSize(QtCore.QSize(30, 30))
        self.info_button.setObjectName("info_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.shortcut_open = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+S'), self)
        self.shortcut_open.activated.connect(self.save_shortcut)

    def save_shortcut(self):
        """
        :does: save df to file
        """
        path, ext = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', '', "CSV Files (*.csv);")
        if path != '':
            print(path)
            self.df_res.to_csv(path, index=False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart City"))
        self.up_button.setToolTip(_translate("MainWindow", "Back"))
        self.down_button.setToolTip(_translate("MainWindow", "Next"))
        self.openfile_button.setToolTip(_translate("MainWindow", "Choose a file"))
        self.pagename.setText(_translate("MainWindow", "0-10"))
        self.search_button.setToolTip(_translate("MainWindow", "Find a city"))
        self.save_button.setToolTip(_translate("MainWindow", "Save to a file"))
        self.info_button.setToolTip(_translate("MainWindow", "Info"))

