# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/UI_800x480.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 641, 431))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(540, 50, 81, 281))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButtonRFon = QtGui.QPushButton(self.tab)
        self.pushButtonRFon.setEnabled(True)
        self.pushButtonRFon.setGeometry(QtCore.QRect(20, 240, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRFon.setFont(font)
        self.pushButtonRFon.setCheckable(True)
        self.pushButtonRFon.setFlat(False)
        self.pushButtonRFon.setObjectName(_fromUtf8("pushButtonRFon"))
        self.progressBar_2 = QtGui.QProgressBar(self.tab)
        self.progressBar_2.setGeometry(QtCore.QRect(450, 50, 81, 281))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.progressBar_3 = QtGui.QProgressBar(self.tab)
        self.progressBar_3.setGeometry(QtCore.QRect(360, 50, 81, 281))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setInvertedAppearance(False)
        self.progressBar_3.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(550, 340, 68, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(470, 340, 68, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(390, 340, 68, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBar_4 = QtGui.QProgressBar(self.tab)
        self.progressBar_4.setGeometry(QtCore.QRect(270, 50, 81, 281))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_4.setInvertedAppearance(False)
        self.progressBar_4.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar_4.setObjectName(_fromUtf8("progressBar_4"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(290, 340, 68, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButtonRFon_2 = QtGui.QPushButton(self.tab)
        self.pushButtonRFon_2.setEnabled(False)
        self.pushButtonRFon_2.setGeometry(QtCore.QRect(20, 150, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRFon_2.setFont(font)
        self.pushButtonRFon_2.setCheckable(True)
        self.pushButtonRFon_2.setFlat(False)
        self.pushButtonRFon_2.setObjectName(_fromUtf8("pushButtonRFon_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label_Status = QtGui.QLabel(self.centralwidget)
        self.label_Status.setGeometry(QtCore.QRect(0, 0, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Status.setFont(font)
        self.label_Status.setObjectName(_fromUtf8("label_Status"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.progressBar.setFormat(_translate("MainWindow", "%p kW", None))
        self.pushButtonRFon.setText(_translate("MainWindow", "RF on", None))
        self.progressBar_2.setFormat(_translate("MainWindow", "%p kW", None))
        self.progressBar_3.setFormat(_translate("MainWindow", "%p kW", None))
        self.label.setText(_translate("MainWindow", "RF-out\n"
"FWD", None))
        self.label_2.setText(_translate("MainWindow", "VSWR", None))
        self.label_3.setText(_translate("MainWindow", "Idd", None))
        self.progressBar_4.setFormat(_translate("MainWindow", "%p kW", None))
        self.label_4.setText(_translate("MainWindow", "Temp", None))
        self.pushButtonRFon_2.setText(_translate("MainWindow", "RF off", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Status", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "System", None))
        self.label_Status.setText(_translate("MainWindow", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
