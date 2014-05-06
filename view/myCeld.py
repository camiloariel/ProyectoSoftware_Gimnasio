from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyCeld(QPushButton):
	def __init__(self, icon, table):
		super(MyCeld,self).__init__()
		self.table = table
		self.clicked.connect(self.evento)
		self.index=0
		self.usuario = ""
		self.fecha = ""
		self.hora = ""
		self.tipo = ""
		self.setIcon(icon)

	def setIndex(self, index):
		self.index = index
		
		if self.tipo=="delete":
			self.setStyleSheet("QPushButton{border:0px;background-color:#21351e;}")
		else:
			self.setStyleSheet("QPushButton{border:0px;background-color:#2e422b;}")

	def evento(self):
		if self.tipo == "add":
			self.table.addReserva(self.index ,self.usuario ,self.fecha, self.hora)
		elif self.tipo == "delete":
			self.table.deleteReserva(self.index ,self.usuario ,self.fecha, self.hora)