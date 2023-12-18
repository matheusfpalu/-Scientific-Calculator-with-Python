# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 262)
        Dialog.setStyleSheet("color: white;\n"
"border: 1px solid white;\n"
"background-color: black;\n"
"")
        self.T = QtWidgets.QPushButton(Dialog)
        self.T.setGeometry(QtCore.QRect(140, 60, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(15)
        self.T.setFont(font)
        self.T.setObjectName("T")
        self.C = QtWidgets.QPushButton(Dialog)
        self.C.setGeometry(QtCore.QRect(140, 160, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(15)
        self.C.setFont(font)
        self.C.setObjectName("C")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.T.setText(_translate("Dialog", "Tradicional"))
        self.C.setText(_translate("Dialog", "Científica"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cambria\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Selecione o modo da calculadora:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

