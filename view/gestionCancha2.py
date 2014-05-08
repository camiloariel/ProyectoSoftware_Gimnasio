from PyQt4.QtGui import *
from PyQt4.QtCore import *
from view.tablaReserva import TablaReserva
from view.tablaCalendario import TablaCalendario
from view.calendario import Calendario
from controller.cancha import Cancha

from view.tablaCalendario import TablaCalendario
from menu import Menu 
import datetime
import sys


class GestionCancha2(QWidget):
	def __init__(self, main):
		super(GestionCancha2, self).__init__()
		self.main = main
		
		self.titulo = QLabel(' HORARIO Y RESERVA DE CANCHAS')
		self.titulo.setStyleSheet('background:#1E7907; font:25px; color:white;')
		self.titulo.setContentsMargins(0, 10, 0, 10)

		self.canchas_list = Cancha().findAll()
		self.canchas_len = len(self.canchas_list)
		self.canchas_cont = 0
		#DBDEE2
		self.fecha = QLabel('Fechaa 12-12-12')
		self.fecha.setStyleSheet('background:#E4E8EE; font:17px; color:black;  ')
		self.fecha.setAlignment(Qt.AlignCenter)
		self.fecha.setContentsMargins(10, 10, 10, 10)
		
		tRes = TablaReserva(main, self)
		self.panelCalendario = Calendario(tRes)
		with open("view/stilo2.css") as f:
			self.panelCalendario.setStyleSheet(f.read())



		self.imgCanchas = QLabel()
		self.imgCanchas.setContentsMargins(0, 0, 0, 0)
		self.setImagenCancha("images/Banner (2).png")
		
		

		self.NomCancha = QLabel()
		self.NomCancha.setStyleSheet('background:#E5E8F1; font:17px; color:black;')
		self.NomCancha.setAlignment(Qt.AlignCenter)
		self.NomCancha.setContentsMargins(10, 10, 10, 10)
		
		self.setCancha(0)
		
		self.buttonAnt = QPushButton()
		self.buttonAnt.setIcon(QIcon("images/icons/Copy of icono_flecha_verde.png"))  
		self.buttonAnt.setStyleSheet('background-color:#E5E8F1;')
		self.buttonAnt.setMaximumSize(200, 50)
		self.connect(self.buttonAnt, SIGNAL('clicked()'), self.event_canchaAnterior)
		
		self.buttonSig = QPushButton()
		self.buttonSig.setIcon(QIcon("images/icons/icono_flecha_verde - 2.png"))
		self.buttonSig.setStyleSheet('background-color:#E5E8F1;')
		self.buttonSig.setMaximumSize(200, 50)
		self.connect(self.buttonSig, SIGNAL('clicked()'), self.event_canchaSiguiente)


		self.layoutCanchafecha = QHBoxLayout()
		self.layoutCanchafecha.addWidget(self.buttonAnt)
		self.layoutCanchafecha.addWidget(self.NomCancha)
		self.layoutCanchafecha.addWidget(self.buttonSig)
		self.layoutCanchafecha.addWidget(self.fecha)		
		
		
		self.layoutTablaReserva =  QHBoxLayout()
		self.layoutTablaReserva.addWidget(tRes)
		self.layoutTablaReserva.setContentsMargins(50, 0, 50, 0)
		
		self.layoutPanelCancha = QVBoxLayout()
		self.layoutPanelCancha.addWidget(self.imgCanchas)		
		self.layoutPanelCancha.addLayout(self.layoutCanchafecha)
		self.layoutPanelCancha.addStretch(0)
		self.layoutPanelCancha.addLayout(self.layoutTablaReserva)
		self.layoutPanelCancha.addStretch(0)
		
		
		self.layoutContenedor = QHBoxLayout()
		self.layoutContenedor.setSpacing(0)
		self.layoutContenedor.addWidget(self.panelCalendario)
		self.layoutContenedor.setSpacing(0)
		self.layoutContenedor.addLayout(self.layoutPanelCancha)	
		self.layoutContenedor.setContentsMargins(0, 0, 0, 0)
		
		
		
		self.layoutGeneral = QVBoxLayout()
		
		self.layoutGeneral.addWidget(self.titulo)
		self.layoutGeneral.addWidget(Menu(self))
		self.layoutGeneral.setSpacing(0)
		self.layoutGeneral.addLayout(self.layoutContenedor)
		self.layoutGeneral.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.layoutGeneral)							

	

	def event_canchaAnterior(self):
		self.canchas_cont = (self.canchas_cont-1)%self.canchas_len
		self.setCancha(self.canchas_cont)

	def event_canchaSiguiente(self):
		self.canchas_cont = (self.canchas_cont+1)%self.canchas_len
		self.setCancha(self.canchas_cont)
		
		
		
	def setImagenCancha(self, img):
		myPixmap = QPixmap(img)
		width = int(self.main.width)
		if width> 1300:
			width = int(self.main.width)*0.88
		elif width >=1024:
			width = int(self.main.width)*0.85
		self.imgCanchas.setPixmap(myPixmap.scaled(width,768*0.25))
		
		
	def	setCancha(self, index):
		cancha = self.canchas_list[index]
		self.NomCancha.setText(cancha.descripcion)
		self.setImagenCancha("images/cancha_baby.png")
		
		
		