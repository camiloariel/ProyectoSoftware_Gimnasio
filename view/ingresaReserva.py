from PyQt4.QtGui import *
from PyQt4.QtCore import *
from controller.usuario import Usuario
from controller.tipoCancha import TipoCancha
from controller.cancha import Cancha
from controller.reserva import Reserva

class IngresaReserva(QWidget):
	def __init__(self, main):
		super(IngresaReserva, self).__init__()
		self.main = main
		self.hbox = QHBoxLayout()
		self.setLayout(self.hbox)

		self.CB_usuarios = QComboBox()
		users = Usuario().findAll()
		self.CB_usuarios.addItem('SELECCIONE UN USUARIO',QVariant(0))
		for user in users:
			self.CB_usuarios.addItem(user.nombre+' '+user.apellido,QVariant(int(user.idUsuario)))
		self.hbox.addWidget(self.CB_usuarios)

		self.CB_deporte = QComboBox()
		deportes = TipoCancha().findAll()
		self.CB_deporte.addItem('SELECCIONE UN DEPORTE',QVariant(0))
		for deporte in deportes:
			self.CB_deporte.addItem(deporte.nombre,QVariant(int(deporte.idTipoCancha)))
		self.hbox.addWidget(self.CB_deporte)

		self.CB_cancha = QComboBox()
		self.CB_cancha.addItem('SELECCIONE CANCHA',QVariant(0))
		self.hbox.addWidget(self.CB_cancha)

		self.CB_fecha = QComboBox()
		self.CB_fecha.addItem('SELECCIONE FECHA',QVariant(0))
		self.hbox.addWidget(self.CB_fecha)

		self.CB_horario = QComboBox()
		self.CB_horario.addItem('SELECCIONE HORARIO',QVariant(0))
		self.hbox.addWidget(self.CB_horario)

		self.connect(self.CB_usuarios, SIGNAL('activated(QString)'), self.event_CB_usuarios)
		self.connect(self.CB_deporte, SIGNAL('activated(QString)'), self.event_CB_deporte)
		self.connect(self.CB_cancha, SIGNAL('activated(QString)'), self.event_CB_cancha)
		self.connect(self.CB_fecha, SIGNAL('activated(QString)'), self.event_CB_fecha)

		self.CB_usuarios.setEnabled(True)
		self.CB_deporte.setEnabled(False)
		self.CB_cancha.setEnabled(False)
		self.CB_fecha.setEnabled(False)
		self.CB_horario.setEnabled(False)

	def event_CB_usuarios(self):
		id = self.CB_usuarios.itemData(self.CB_usuarios.currentIndex()).toInt()[0]
		if id == 0:
			self.CB_usuarios.setEnabled(True)
			self.CB_deporte.setEnabled(False)
			self.CB_cancha.setEnabled(False)
			self.CB_fecha.setEnabled(False)
			self.CB_horario.setEnabled(False)
		else:
			self.CB_usuarios.setEnabled(True)
			self.CB_deporte.setEnabled(True)
			self.CB_cancha.setEnabled(False)
			self.CB_fecha.setEnabled(False)
			self.CB_horario.setEnabled(False)
	def event_CB_deporte(self):
		id = self.CB_deporte.itemData(self.CB_deporte.currentIndex()).toInt()[0]
		if id == 0:
			self.CB_usuarios.setEnabled(True)
			self.CB_deporte.setEnabled(True)
			self.CB_cancha.setEnabled(False)
			self.CB_fecha.setEnabled(False)
			self.CB_horario.setEnabled(False)
			self.eraseComboBox(self.CB_cancha)
		else:
			canchas = Cancha().findByIdTipoCancha(id)
			if canchas is not None:
				self.eraseComboBox(self.CB_cancha)
				for cacha in canchas:
					self.CB_cancha.addItem(cacha.descripcion,QVariant(int(cacha.idCancha)))
			else:
				self.eraseComboBox(self.CB_cancha)

			self.CB_usuarios.setEnabled(True)
			self.CB_deporte.setEnabled(True)
			self.CB_cancha.setEnabled(True)
			self.CB_fecha.setEnabled(False)
			self.CB_horario.setEnabled(False)

	def event_CB_cancha(self):
		self.idCancha = self.CB_cancha.itemData(self.CB_cancha.currentIndex()).toInt()[0]
		if self.idCancha == 0:
			self.CB_usuarios.setEnabled(True)
			self.CB_deporte.setEnabled(True)
			self.CB_cancha.setEnabled(True)
			self.CB_fecha.setEnabled(False)
			self.CB_horario.setEnabled(False)
			self.eraseComboBox(self.CB_fecha)
		else:
			self.CB_usuarios.setEnabled(True)
			self.CB_deporte.setEnabled(True)
			self.CB_cancha.setEnabled(True)
			self.CB_fecha.setEnabled(True)
			self.CB_horario.setEnabled(False)
			self.eraseComboBox(self.CB_fecha)
			self.CB_fecha.addItem('13/04/2014',QVariant("2014-04-13"))

	def event_CB_fecha(self):
		id = self.CB_fecha.itemData(self.CB_fecha.currentIndex()).toString()
		if id == "0":
			self.CB_usuarios.setEnabled(True)
			self.CB_deporte.setEnabled(True)
			self.CB_cancha.setEnabled(True)
			self.CB_fecha.setEnabled(True)
			self.CB_horario.setEnabled(True)
			self.eraseComboBox(self.CB_horario)
		else:
			r = Reserva()
			r.idCancha = self.idCancha
			r.fecha = id
			reserva = Reserva().findByIdCanchaAndFecha(r)
			aux = []
			if reserva is not None:
				self.eraseComboBox(self.CB_horario)
				for res in reserva:
					aux.append(str(res.horaInicio))
				for x in xrange(10,23):
					hora = '%s:00' % (str(x))
					hora_sig = '%s:59' % (str(x))
					if hora+":00" not in aux:
						self.CB_horario.addItem(str(hora)+" - "+str(hora_sig),QVariant(str(hora)))
			else:
				self.eraseComboBox(self.CB_horario)
			self.CB_usuarios.setEnabled(True)
			self.CB_deporte.setEnabled(True)
			self.CB_cancha.setEnabled(True)
			self.CB_fecha.setEnabled(True)
			self.CB_horario.setEnabled(True)

	def eraseComboBox(self, cbox):
		for x in range(1,cbox.count()):
			cbox.removeItem(1)