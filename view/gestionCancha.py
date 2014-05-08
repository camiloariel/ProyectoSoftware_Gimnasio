from PyQt4.QtGui import *
from PyQt4.QtCore import *
from view.tablaReserva import TablaReserva
from view.tablaCalendario import TablaCalendario
from view.calendario import Calendario
from view.tablaCalendario import TablaCalendario
import datetime
import sys


from PyQt4 import QtGui

class GestionCancha(QtGui.QWidget):
	
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        with open("view/stilo2.css") as f:
			self.setStyleSheet(f.read())
        mygroupbox = QtGui.QGroupBox('this is my groupbox')
   
        mygroupbox = QGroupBox()
        myform = QFormLayout()
        fecha = datetime.date.today()
        fechas = self.calc_meses(fecha) 
        
        self.TablaCalendario1 = TablaCalendario(fechas[0],self) #Calendario 1
        self.TablaCalendario2 = TablaCalendario(fechas[1],self) #Calendario 2
        self.TablaCalendario3 = TablaCalendario(fechas[2],self) #calendario 3 
        self.TablaCalendario4 = TablaCalendario(fechas[3],self) #Calendario 1
        self.TablaCalendario5 = TablaCalendario(fechas[4],self) #Calendario 2
        self.TablaCalendario6 = TablaCalendario(fechas[5],self) #calendario 3 
        self.TablaCalendario7 = TablaCalendario(fechas[6],self) #Calendario 1
        self.TablaCalendario8 = TablaCalendario(fechas[7],self) #Calendario 2
        self.TablaCalendario9 = TablaCalendario(fechas[8],self) #calendario 3 
        self.TablaCalendario10 = TablaCalendario(fechas[9],self) #Calendario 2
        self.TablaCalendario11 = TablaCalendario(fechas[10],self)
        self.TablaCalendario12 = TablaCalendario(fechas[11],self) #Ca
        
       
        myform.addRow(self.TablaCalendario1)
        myform.addRow(self.TablaCalendario2)
        myform.addRow(self.TablaCalendario3)
        myform.addRow(self.TablaCalendario4)
        myform.addRow(self.TablaCalendario5)
        myform.addRow(self.TablaCalendario6)
        myform.addRow(self.TablaCalendario7)
        myform.addRow(self.TablaCalendario8)
        myform.addRow(self.TablaCalendario9)
        myform.addRow(self.TablaCalendario10)
        myform.addRow(self.TablaCalendario11)
        myform.addRow(self.TablaCalendario12)
        mygroupbox.setLayout(myform)
        
        scroll = QScrollArea()
        scroll.horizontalScrollBar()

        scroll.setWidget(mygroupbox)
        scroll.setFixedHeight(400)
        scroll.setFixedWidth(200)
     
 
        self.layoutVertical = QVBoxLayout()
        self.layoutVertical.addWidget(scroll)
        self.setLayout(self.layoutVertical)
        
      
    def calc_meses(self,fecha):
        
        print fecha
        mesprox =[]
        
        dia =fecha.day
        mes =fecha.month
        year =fecha.year
            
        for i in range(3):
            mesprox.append( datetime.date(year,mes+(i-1),dia))
        return mesprox 

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    GestionCancha = GestionCancha()
    GestionCancha.setGeometry(500, 300, 300, 400)
    GestionCancha.show()
    sys.exit(app.exec_())
		