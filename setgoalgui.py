# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondgui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_goalgui(object):
    def setupUi(self, goalgui):
        goalgui.setObjectName("goalgui")
        goalgui.resize(400, 300)
        self.addBtn = QtWidgets.QPushButton(goalgui)
        self.addBtn.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.addBtn.setObjectName("addBtn")
        self.listWidget = QtWidgets.QListWidget(goalgui)
        self.listWidget.setGeometry(QtCore.QRect(110, 61, 256, 141))
        self.listWidget.setObjectName("listWidget")
        self.myTextInput = QtWidgets.QLineEdit(goalgui)
        self.myTextInput.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.myTextInput.setObjectName("myTextInput")
        self.lineEdit = QtWidgets.QLineEdit(goalgui)
        self.lineEdit.setGeometry(QtCore.QRect(170, 9, 111, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.buttonBox = QtWidgets.QDialogButtonBox(goalgui)
        self.buttonBox.setGeometry(QtCore.QRect(210, 240, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dateEdit = QtWidgets.QDateEdit(goalgui)
        self.dateEdit.setGeometry(QtCore.QRect(170, 30, 111, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(goalgui)
        QtCore.QMetaObject.connectSlotsByName(goalgui)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addBtn.setText(_translate("Dialog", "Goal Set !"))
        self.lineEdit.setText(_translate("Dialog", "             Goals"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    goalgui = QtWidgets.QDialog()
    ui = Ui_goalgui()
    ui.setupUi(goalgui)
    goalgui.show()
    sys.exit(app.exec_())

