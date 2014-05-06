from PyQt4.QtGui import *
from PyQt4.QtCore import *
from view.tablaReserva import TablaReserva
from view.tablaCalendario import TablaCalendario
from view.calendario import Calendario

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

		
        
		
		"""
		self.botonExit = QPushButton(' CERRAR ')
		self.botonExit.setIcon(QIcon("images/icons/botonCerrar.png"))
		self.botonExit.clicked.connect(QCoreApplication.instance().quit)
		self.botonExit.setIconSize(QSize(0,50))
		self.botonExit.setStyleSheet('background:#1E7A08; font:25px')
			
		
		
		"""
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
		myPixmap = QPixmap('images/banner2.png')
		width = int(self.main.width)
		if width> 1300:
			width = int(self.main.width)*0.88
		elif width >=1024:
			width = int(self.main.width)*0.85
		myScaledPixmap = myPixmap.scaled(width,768*0.25)
		self.imgCanchas.setPixmap(myScaledPixmap)
		self.imgCanchas.setContentsMargins(0, 0, 0, 0)


		self.NomCancha = QLabel('CAMPO SINTETICO NUMERO 1')
		self.NomCancha.setStyleSheet('background:#E5E8F1; font:17px; color:black;')
		self.NomCancha.setAlignment(Qt.AlignCenter)
		self.NomCancha.setContentsMargins(10, 10, 10, 10)
		
		self.buttonAnt = QPushButton()
		self.buttonAnt.setIcon(QIcon("images/icons/Copy of icono_flecha_verde.png"))  
		self.buttonAnt.setStyleSheet('background-color:#E5E8F1;')
		self.buttonAnt.setMaximumSize(200, 50)
		#self.connect(self.buttonAnt, SIGNAL('clicked()'), self.event_canchaAnterior)
		
		self.buttonSig = QPushButton()
		self.buttonSig.setIcon(QIcon("images/icons/icono_flecha_verde - 2.png"))
		self.buttonSig.setStyleSheet('background-color:#E5E8F1;')
		self.buttonSig.setMaximumSize(200, 50)
		#self.connect(self.buttonSig, SIGNAL('clicked()'), self.event_canchaSiguiente)


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
		myPixmap = QPixmap('images/cancha_basquetball.png')
		myScaledPixmap = myPixmap.scaled(self.imgCanchas.size(), Qt.KeepAspectRatio)
		self.imgCanchas.setPixmap(myScaledPixmap)

	def event_canchaSiguiente(self):
		myPixmap = QPixmap('images/cancha_baby.png')
		myScaledPixmap = myPixmap.scaled(self.imgCanchas.size(), Qt.KeepAspectRatio)
		self.imgCanchas.setPixmap(myScaledPixmap)
		