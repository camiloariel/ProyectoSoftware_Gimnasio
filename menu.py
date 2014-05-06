from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class Menu(QMenuBar):
     
    def __init__(self, main):
        super(Menu,self).__init__()
        self.main = main
        self.setObjectName("menubar")
        #DBDEE2
        #20351E
        #calendario : #C9CCD1 
        ##20281F
        archivoMenu=self.addMenu('&ARCHIVO')
        exitAction = QAction('&Salir', self)        
        exitAction.setStatusTip('Salir de la aplicacion')
        exitAction.triggered.connect(self.prueba)
        
        canchaMenu=self.addMenu('&CANCHAS')
        gimnasioMenu=self.addMenu('&GIMNASIO')
        pagoMenu=self.addMenu('&PAGOS')
        informesMenu=self.addMenu('&INFORMES')
        acercaMenu=self.addMenu('&ACERCA DE')
        archivoMenu.addAction(exitAction)

        
         

    def prueba(self):
        sys.exit(0)