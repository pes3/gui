#Python

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from firstgui import Ui_myfirstgui

class MyFirstGuiProgram(Ui_goalgui):
	def __init__(self, dialog):
		Ui_goalgui.__init__(self)
		self.setupUi(dialog)

		# Connect "add" button with a custom function (addInputTextToListbox)
		self.addBtn.clicked.connect(self.addInputTextToListbox)

	def addInputTextToListbox(self):
		txt = self.myTextInput.text()
		self.listWidget.addItem(txt)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = MyFirstGuiProgram(dialog)

	dialog.show()
	sys.exit(app.exec_())
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from firstgui import Ui_myfirstgui
 
class MyFirstGuiProgram(Ui_myfirstgui):
	def __init__(self, dialog):
		Ui_myfirstgui.__init__(self)
		self.setupUi(dialog)
 
		# Connect "add" button with a custom function (addInputTextToListbox)
		self.addBtn.clicked.connect(self.addInputTextToListbox)
 
	def addInputTextToListbox(self):
		txt = self.myTextInput.text()
		self.listWidget.addItem(txt)
 
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
 
	prog = MyFirstGuiProgram(dialog)
 
	dialog.show()
	sys.exit(app.exec_())
