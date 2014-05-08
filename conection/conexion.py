import urllib 
import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
class Conexion():
	
	

		def __init__(self,url = "162.243.51.179:69",controller = "", accion = "", id = "", json = ""):
			self.url = url
			self.controller = controller
			self.accion = accion
			self.id = id
			self.json = json
	
		def execute(self):
			QApplication.setOverrideCursor(QCursor(QPixmap("images/icons/loading.gif").scaled(40,40)))
			f=None 
			try:
				f = urllib.urlopen("http://%s/controller/%s?accion=%s&id=%s&json=%s" % (self.url,self.controller,self.accion,self.id,self.json))
			except IOError:
				QMessageBox.about(QWidget(),"Error de Conexion", "Existe un error de conexion, porfavor, revisar red de Internet")
				sys.exit()
			rl = f.readline()
			decoded = json.loads(rl)
			QApplication.restoreOverrideCursor()
			return decoded
	
		def executeCUD(self):
			QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
			f=None
			try:
				f = urllib.urlopen("http://%s/controller/%s?accion=%s&id=%s&json=%s" % (self.url,self.controller,self.accion,self.id,self.json))
			except IOError:
				QMessageBox.about(QWidget(),"Error de Conexion", "Existe un error de conexion, porfavor, revisar red de Internet")
				sys.exit()
			rl = f.readline()
			QApplication.restoreOverrideCursor()
			return rl
	