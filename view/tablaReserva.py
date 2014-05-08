# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from controller.reserva import Reserva
from controller.usuario import Usuario
from view.myCeld import MyCeld
import datetime
import time

class TablaReserva(QTableWidget):
	def __init__(self, main, gc):
		super(TablaReserva, self).__init__()
		self.main = main
		self.gc = gc
		self.setColumnCount(5)
		self.verticalHeader().setVisible(False)
		width = int(self.main.width)

		if width < 1300:
			self.setColumnWidth(0,  int(float(width)*0.03))
			self.setColumnWidth(1,  int(float(width)*0.176))
			self.setColumnWidth(2,  int(float(width)*0.176))
			self.setColumnWidth(3,  int(float(width)*0.176))
			self.setColumnWidth(4,  int(float(width)*0.176))
		else:
			self.setColumnWidth(0,  int(float(width)*0.03))
			self.setColumnWidth(1,  int(float(width)*0.184))
			self.setColumnWidth(2,  int(float(width)*0.184))
			self.setColumnWidth(3,  int(float(width)*0.184))
			self.setColumnWidth(4,  int(float(width)*0.184))

		width = int(self.main.width)
		if width > 1300:
			width = int(self.main.width)*0.777
		self.setFixedSize(width,300)
		self.setStyleSheet("QTableWidget { border:0px;color: white; font-size: 13px;}QHeaderView::section:Horizontal{   color: white;background-color: #1E7A08;} ")
		self.connect(self,SIGNAL("itemSelectionChanged()"),self.cellClicked)

		self.idCancha = "1"

		year = datetime.date.today().year
		month = datetime.date.today().month
		day = datetime.date.today().day
		self.fecha = "%s-%s-%s" % (year, month, day)
		self.cambiaFecha(self.fecha)

		self.refreshTable()

	def refreshTable(self):
		#QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
		r = Reserva()
		r.idCancha = self.idCancha
		r.fecha = self.fecha
		reserva = Reserva().findByIdCanchaAndFecha(r)
		self.setRowCount(14)



		eng = MyCeld(QIcon('images/icons/icono_engranajes.png'), self)
		eng.setIndex(0)
		#self.setCellWidget(0, 0, eng)
		self.setHorizontalHeaderItem(0, QTableWidgetItem(QIcon('images/icons/icono_engranajes.png'),""))
		self.setHorizontalHeaderItem(1, self.itemNoSelect("HORA"))
		self.setHorizontalHeaderItem(2, self.itemNoSelect("RUT"))
		self.setHorizontalHeaderItem(3, self.itemNoSelect("NOMBRES"))
		self.setHorizontalHeaderItem(4, self.itemNoSelect("APELLIDOS"))



		aux = []
		if reserva is not None:
			for res in reserva:
				aux.append(str(res.horaInicio))
				aux.append(str(res.idUsuario))
			for x in xrange(10,24):
				hora = '%s:00' % (str(x))
				hora_sig = '%s:59' % (str(x))
				if hora+":00" not in aux:
					item = QTableWidgetItem(self.itemNoSelect(str(str(hora)+" - "+str(hora_sig))))
					my=MyCeld(QIcon('images/icons/icono_agregarreserva.png'),self)
					my.table = self
					my.hora = hora
					my.tipo = "add"
					my.setIndex(x-10)
					self.setCellWidget(x-10, 0,my)
					self.setItem(x-10, 1, item)
					self.setItem(x-10, 2, self.itemNoSelect(""))
					self.setItem(x-10, 3, self.itemNoSelect(""))
					self.setItem(x-10, 4, self.itemNoSelect(""))
					for j in xrange(1,5):
						self.item(x-10,j).setBackground(QBrush(QColor(46,66,43)))
				else:
					self.setItem(x-10, 1, self.itemNoSelect(str(str(hora)+" - "+str(hora_sig))))
					user = Usuario().findByIdUsuario(int(aux[int(aux.index(hora+":00"))+1]))
					self.setItem(x-10, 2, self.itemNoSelect(str(user[0].run)))
					self.setItem(x-10, 3, self.itemNoSelect(str(user[0].nombre)))
					self.setItem(x-10, 4, self.itemNoSelect(str(user[0].apellido)))
					my=MyCeld(QIcon('images/icons/icono_eliminar.png'),self)
					my.table = self
					my.usuario = user[0].idUsuario
					my.fecha = self.fecha
					my.hora = hora
					my.tipo = "delete"
					my.setIndex(x-10)
					self.setCellWidget(x-10, 0,my)
					for j in xrange(1,5):
						self.item(x-10,j).setBackground(QBrush(QColor(33,53,30)))
		else:
			for x in xrange(10,24):
				hora = '%s:00' % (str(x))
				hora_sig = '%s:59' % (str(x))
				item = QTableWidgetItem(QTableWidgetItem(str(str(hora)+" - "+str(hora_sig))))
				my=MyCeld(QIcon('images/icons/icono_agregarreserva.png'),self)
				my.table = self
				my.hora = hora
				my.tipo = "add"
				my.setIndex(x-9)
				self.setCellWidget(x-10, 0,my)
				self.setItem(x-10, 1, item)
				self.setItem(x-10, 2, QTableWidgetItem(""))
				self.setItem(x-10, 3, QTableWidgetItem(""))
				self.setItem(x-10, 4, QTableWidgetItem(""))
				for j in xrange(1,5):
					self.item(x-10,j).setBackground(QBrush(QColor(46,66,43)))
		#QApplication.restoreOverrideCursor()


	def addReserva(self,index,usuario, fecha, hora):
		year = datetime.date.today().year
		month = datetime.date.today().month
		day = datetime.date.today().day
		actual = "%s-%s-%s" % (year, month, day)
		act=datetime.datetime(*time.strptime(actual, "%Y-%m-%d")[0:6])
		fec=datetime.datetime(*time.strptime(self.fecha, "%Y-%m-%d")[0:6])
		if act>fec:
			QMessageBox.about(self, "Agregar Reserva", "La reserva no puede ser anterior a la fecha actual")
		else:
			qid = QInputDialog()
			text, ok = qid.getText(self, 'Ingrese Usuario', 
				'Ingrese RUN Usuario:')

			if ok:
				user = Usuario().findByRun(str(text))
				if user == None:
					QMessageBox.about(self, "Agregar Reserva", "El usuario no se encuentra registrado")
				else:
					r = Reserva()
					r.idUsuario = user[0].idUsuario
					r.idCancha = self.idCancha
					r.fecha = self.fecha
					r.horaInicio = hora
					r.estado = "0"
					res = Reserva().add(r)
					if res == "esta":
						QMessageBox.about(self, "Agregar Reserva", "No se puede realizar la reserva, \n ya que se encuentra reservada")
					else:
						QMessageBox.about(self, "Agregar Reserva", "La reserva se agrego con exito")
					self.refreshTable()

	def deleteReserva(self,index,usuario, fecha, hora):
		reply = QMessageBox.question(self, 'Eliminar Reserva','Esta seguro de eliminar esta reserva?', 
			QMessageBox.Yes, QMessageBox.No)

		if reply == QMessageBox.Yes:
			r = Reserva()
			r.idUsuario = usuario
			r.fecha = fecha
			r.horaInicio = hora
			reserva = Reserva().deleteByUserHourAndDate(r)
			self.refreshTable()



	def cambiaFecha(self, fecha):
		self.fecha = fecha
		f = fecha.split("-")
		mesList = {'01':'ENERO','02':'FEBRERO','03':'MARZO',
       '04':'ABRIL','05':'MAYO','06':'JUNIO',
       '07':'JULIO','08':'AGOSTO','09':'SEPTIEMBRE',
       '1':'ENERO','2':'FEBRERO','3':'MARZO',
       '4':'ABRIL','5':'MAYO','6':'JUNIO',
       '7':'JULIO','8':'AGOSTO','9':'SEPTIEMBRE',
       '10':'OCTUBRE','11':'NOVIEMBRE','12':'DICIEMBRE'}
		self.gc.fecha.setText("%s DE %s DE %s" % (str(f[2]),mesList[str(f[1])],str(f[0])))
		self.refreshTable()


	def itemNoSelect(self, string):
		item =  QTableWidgetItem(string)
		item.setFlags(Qt.ItemIsEnabled |Qt.ItemIsSelectable )
		return item
