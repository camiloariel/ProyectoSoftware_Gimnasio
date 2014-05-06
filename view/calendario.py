'''
Created on 19-04-2014

@author: Omar
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import  *
from view.tablaCalendario import TablaCalendario
import datetime

class Calendario(TablaCalendario):
    '''
    classdocs
    '''
    def __init__(self,main):
        '''
        Constructor
        '''
        super(TablaCalendario, self).__init__()
        self.main = main
        
        mes = {'JANUARY':'Enero','FEBRUARY':'Febrero','MARCH':'Marzo',
                'APRIL':'Abril','MAY':'Mayo','JUNE':'Junio',
                'JULY':'Julio','AUGUST':'Agosto','SEPTEMBER':'Setiembre',
                'OCTOBER':'Octubre','NOVEMBER':'Noviembre','DECEMBER':'Diciembre'}
        
        self.btnYearSig =QPushButton()
        self.btnYearSig.setIcon(QIcon("images/icons/icono_flechablancaLeft.png"))
        self.btnYearSig.clicked.connect(self.changeYear(1))
       
        self.btnYearAnt =QPushButton()
        self.btnYearAnt.setIcon(QIcon("images/icons/icono_flechablancaRigth.png"))
        self.btnYearAnt.clicked.connect(self.changeYear(-1))  
        
        
        
             
        year = datetime.date.today().year
        self.yeartext = QLineEdit(str(year))
        self.yeartext.setStyleSheet('color: black;')
        self.yeartext.setAlignment(Qt.AlignCenter)
        
        
        self.cambioYear = QHBoxLayout()
        self.cambioYear.addWidget(self.btnYearAnt)
        self.cambioYear.addWidget(self.yeartext)
        self.cambioYear.addWidget(self.btnYearSig)
        
        
        
        mesV = datetime.date.today().month
        self.mestext = QLineEdit(str(mesV))
        self.mestext.setVisible(False)
        
        self.cambioMes = QHBoxLayout()
        self.cambioMes.addWidget(self.mestext)
        
        
        fecha = datetime.date(datetime.date.today().year,1,1)
        fechas = self.calc_meses(fecha) 
        
        self.verde1 = QLabel() 
        self.verde1.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde1.setFixedSize(130,10)
        
        self.name1 = QLineEdit(mes[fechas[0].strftime('%B').upper()])  #nombre Mes
        self.name1.setAlignment(Qt.AlignCenter)
        self.name1.setContentsMargins(10, 0,16,0)
        self.name1.setFixedWidth(130)
        
        self.verde2 = QLabel() 
        self.verde2.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde2.setFixedSize(130,10)
        self.name2 = QLineEdit(mes[fechas[1].strftime('%B').upper()])  #nombre Mes
        self.name2.setAlignment(Qt.AlignCenter)
        self.name2.setContentsMargins(10, 0,16,0)
        self.name2.setFixedWidth(130)
        
        self.verde3 = QLabel() 
        self.verde3.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde3.setFixedSize(130,10)
        self.name3 = QLineEdit(mes[fechas[2].strftime('%B').upper()])  #nombre Mes
        self.name3.setAlignment(Qt.AlignCenter)
        self.name3.setContentsMargins(10, 0,16,0)
        self.name3.setFixedWidth(130)
        
        self.verde4 = QLabel() 
        self.verde4.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde4.setFixedSize(130,10)
        self.name4 = QLineEdit(mes[fechas[3].strftime('%B').upper()])  #nombre Mes
        self.name4.setAlignment(Qt.AlignCenter)
        self.name4.setContentsMargins(10, 0,16,0)
        self.name4.setFixedWidth(130)
        
        self.verde5 = QLabel() 
        self.verde5.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde5.setFixedSize(130,10)
        self.name5 = QLineEdit(mes[fechas[4].strftime('%B').upper()])  #nombre Mes
        self.name5.setAlignment(Qt.AlignCenter)
        self.name5.setContentsMargins(10, 0,16,0)
        self.name5.setFixedWidth(130)
        
        self.verde6 = QLabel() 
        self.verde6.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde6.setFixedSize(130,10)
        self.name6 = QLineEdit(mes[fechas[5].strftime('%B').upper()])  #nombre Mes
        self.name6.setAlignment(Qt.AlignCenter)
        self.name6.setContentsMargins(10, 0,16,0)
        self.name6.setFixedWidth(130)
        
        self.verde7 = QLabel() 
        self.verde7.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde7.setFixedSize(130,10)
        self.name7 = QLineEdit(mes[fechas[6].strftime('%B').upper()])  #nombre Mes
        self.name7.setAlignment(Qt.AlignCenter)
        self.name7.setContentsMargins(10, 0,16,0)
        self.name7.setFixedWidth(130)
        
        self.verde8 = QLabel() 
        self.verde8.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde8.setFixedSize(130,10)
        self.name8 = QLineEdit(mes[fechas[7].strftime('%B').upper()])  #nombre Mes
        self.name8.setAlignment(Qt.AlignCenter)
        self.name8.setContentsMargins(10, 0,16,0)
        self.name8.setFixedWidth(130)
        
        self.verde9 = QLabel() 
        self.verde9.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde9.setFixedSize(130,10)
        self.name9 = QLineEdit(mes[fechas[8].strftime('%B').upper()])  #nombre Mes
        self.name9.setAlignment(Qt.AlignCenter)
        self.name9.setContentsMargins(10, 0,16,0)
        self.name9.setFixedWidth(130)
        
        self.verde10= QLabel() 
        self.verde10.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde10.setFixedSize(130,10)
        self.name10 = QLineEdit(mes[fechas[9].strftime('%B').upper()])  #nombre Mes
        self.name10.setAlignment(Qt.AlignCenter)
        self.name10.setContentsMargins(10, 0,16,0)
        self.name10.setFixedWidth(130)
        
        self.verde11 = QLabel() 
        self.verde11.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde11.setFixedSize(130,10)
        self.name11 = QLineEdit(mes[fechas[10].strftime('%B').upper()])  #nombre Mes
        self.name11.setAlignment(Qt.AlignCenter)
        self.name11.setContentsMargins(10, 0,16,0)
        self.name11.setFixedWidth(130)
        
        
        self.verde12 = QLabel() 
        self.verde12.setStyleSheet("background-color:#1E7A08;color:red;");
        self.verde12.setFixedSize(130,10)
        self.name12 = QLineEdit(mes[fechas[11].strftime('%B').upper()])  #nombre Mes
        self.name12.setAlignment(Qt.AlignCenter)
        self.name12.setContentsMargins(10, 0,16,0)
        self.name12.setFixedWidth(130)
        
        
        
        self.TablaCalendario1 = TablaCalendario(fechas[0],self.main) #Calendario 1
        self.TablaCalendario2 = TablaCalendario(fechas[1],self.main) #Calendario 2
        self.TablaCalendario3 = TablaCalendario(fechas[2],self.main) #calendario 3 
        self.TablaCalendario4 = TablaCalendario(fechas[3],self.main) #Calendario 1
        self.TablaCalendario5 = TablaCalendario(fechas[4],self.main) #Calendario 2
        self.TablaCalendario6 = TablaCalendario(fechas[5],self.main) #calendario 3 
        self.TablaCalendario7 = TablaCalendario(fechas[6],self.main) #Calendario 1
        self.TablaCalendario8 = TablaCalendario(fechas[7],self.main) #Calendario 2
        self.TablaCalendario9 = TablaCalendario(fechas[8],self.main) #calendario 3 
        self.TablaCalendario10 = TablaCalendario(fechas[9],self.main) #Calendario 2
        self.TablaCalendario11 = TablaCalendario(fechas[10],self.main)
        self.TablaCalendario12 = TablaCalendario(fechas[11],self.main) #Calendario 2
  
        
        mygroupbox = QGroupBox()
        myform = QFormLayout()
        
        myform.addRow(self.verde1)
        myform.addRow(self.name1)
        myform.addRow(self.TablaCalendario1)
        myform.addRow(self.verde2)
        myform.addRow(self.name2)
        myform.addRow(self.TablaCalendario2)
        myform.addRow(self.verde3)
        myform.addRow(self.name3)
        myform.addRow(self.TablaCalendario3)
        myform.addRow(self.verde4)
        myform.addRow(self.name4)
        myform.addRow(self.TablaCalendario4)
        myform.addRow(self.verde5)
        myform.addRow(self.name5)
        myform.addRow(self.TablaCalendario5)
        myform.addRow(self.verde6)
        myform.addRow(self.name6)
        myform.addRow(self.TablaCalendario6)
        myform.addRow(self.verde7)
        myform.addRow(self.name7)
        myform.addRow(self.TablaCalendario7)
        myform.addRow(self.verde8)
        myform.addRow(self.name8)
        myform.addRow(self.TablaCalendario8)
        myform.addRow(self.verde9)
        myform.addRow(self.name9)
        myform.addRow(self.TablaCalendario9)
        myform.addRow(self.verde10)
        myform.addRow(self.name10)
        myform.addRow(self.TablaCalendario10)
        myform.addRow(self.verde11)
        myform.addRow(self.name11)
        myform.addRow(self.TablaCalendario11)
        myform.addRow(self.verde12)
        myform.addRow(self.name12)
        myform.addRow(self.TablaCalendario12)
        mygroupbox.setLayout(myform)
        
        scroll = QScrollArea()


        scroll.setWidget(mygroupbox)
        scroll
        scroll.setFixedHeight(650)
        scroll.setFixedWidth(164)
        scroll.setContentsMargins(0, 0, 0, 0)
        scroll.setStyleSheet('QScrollArea{border:0px; }QScrollBar:vertical{width: 10px;border:0;} QScrollBar::handle:vertical{height: 30px;border:none;}')
     
        
       
       
        self.layoutVertical = QVBoxLayout()
        self.layoutVertical.addLayout(self.cambioYear)
        self.layoutVertical.setSpacing(0)   
        self.layoutVertical.setMargin(0)
        self.layoutVertical.addWidget(scroll)
        self.layoutVertical.setMargin(0)
        self.layoutVertical.setSpacing(0)
        self.setLayout(self.layoutVertical)
        self.FechaR()
        
        #self.TablaCalendario1.cellClicked.connect(self.selecFecha1(self.TablaCalendario1))
               
      
        #self.connect(self.TablaCalendario4, SIGNAL("cellPressed(int,int)"), self.selecFecha4)
     
    def FechaR(self):
        self.connect(self.TablaCalendario1, SIGNAL("cellPressed(int,int)"), self.selecFecha1)
        self.connect(self.TablaCalendario2, SIGNAL("cellPressed(int,int)"), self.selecFecha2)
        self.connect(self.TablaCalendario3, SIGNAL("cellPressed(int,int)"), self.selecFecha3)
        self.connect(self.TablaCalendario4, SIGNAL("cellPressed(int,int)"), self.selecFecha4)
        self.connect(self.TablaCalendario5, SIGNAL("cellPressed(int,int)"), self.selecFecha5)  
        self.connect(self.TablaCalendario6, SIGNAL("cellPressed(int,int)"), self.selecFecha6)
        self.connect(self.TablaCalendario7, SIGNAL("cellPressed(int,int)"), self.selecFecha7)  
        self.connect(self.TablaCalendario8, SIGNAL("cellPressed(int,int)"), self.selecFecha8)
        self.connect(self.TablaCalendario9, SIGNAL("cellPressed(int,int)"), self.selecFecha9)  
        self.connect(self.TablaCalendario10, SIGNAL("cellPressed(int,int)"), self.selecFecha10)
        self.connect(self.TablaCalendario11, SIGNAL("cellPressed(int,int)"), self.selecFecha11)  
        self.connect(self.TablaCalendario12, SIGNAL("cellPressed(int,int)"), self.selecFecha12)
  
    

    
    def changeYear(self,indice):
        def calluser():
          self.yearSiguiente(indice)
        return calluser
    
   
        
    
    def selecFecha1(self):        
        mes = self.name1.text()  
        year = self.yeartext.text()      
        self.TablaCalendario1.selectFecha(mes,year)
        
    
    
    def selecFecha2(self):        
        mes = self.name2.text()  
        year = self.yeartext.text()      
        self.TablaCalendario2.selectFecha(mes,year)
    
    
    def selecFecha3(self):        
        mes = self.name3.text()  
        year = self.yeartext.text()      
        self.TablaCalendario3.selectFecha(mes,year)
    
    
    def selecFecha4(self):        
        mes = self.name4.text()  
        year = self.yeartext.text()      
        self.TablaCalendario4.selectFecha(mes,year)
    
    
    def selecFecha5(self):        
        mes = self.name5.text()  
        year = self.yeartext.text()      
        self.TablaCalendario5.selectFecha(mes,year)
    
    def selecFecha6(self):        
        mes = self.name6.text()  
        year = self.yeartext.text()      
        self.TablaCalendario6.selectFecha(mes,year)
    
    def selecFecha7(self):        
        mes = self.name7.text()  
        year = self.yeartext.text()      
        self.TablaCalendario7.selectFecha(mes,year)
    
    def selecFecha8(self):        
        mes = self.name8.text()  
        year = self.yeartext.text()      
        self.TablaCalendario8.selectFecha(mes,year)
    
    def selecFecha9(self):        
        mes = self.name9.text()  
        year = self.yeartext.text()      
        self.TablaCalendario9.selectFecha(mes,year)
                                          
    def selecFecha10(self):        
        mes = self.name10.text()  
        year = self.yeartext.text()      
        self.TablaCalendario10.selectFecha(mes,year)
    
    
    def selecFecha11(self):        
        mes = self.name12.text()  
        year = self.yeartext.text()      
        self.TablaCalendario11.selectFecha(mes,year)
        
    def selecFecha12(self):        
        mes = self.name12.text()  
        year = self.yeartext.text()      
        self.TablaCalendario12.selectFecha(mes,year)
        
        
    

    def yearSiguiente(self,indice):
        
        mesList = {'Enero':1,'Febrero':2,'Marzo':3,
                    'Abril':3,'Mayo':5,'Junio':6,
                    'Julio':7,'Agosto':8,'Septiembre':9,
                    'Octubre':10,'Noviembre':11,'Diciembre':12}
        
        self.TablaCalendario1.limpiaTabla()
        self.TablaCalendario2.limpiaTabla()
        self.TablaCalendario3.limpiaTabla()
        #self.TablaCalendario4.limpiaTabla()
        
        year2 = self.yeartext.text() 
        year2=int(year2)+indice
     
        self.yeartext.setText(str(year2))
       
        mes = self.name2.text()  
        year = self.yeartext.text()  
        print mesList[str(mes)]
        fecha = datetime.date(int(year),mesList[str(mes)], 1)
        fecha = self.calc_meses(fecha)
         
        self.TablaCalendario1.llenatabla(year2,fecha[0].month)
        self.TablaCalendario2.llenatabla(year2,fecha[1].month)
        self.TablaCalendario3.llenatabla(year2,fecha[2].month)
        
        
        
    def calc_meses(self,fecha):
        
        print fecha
        mesprox =[]
        
        dia =fecha.day
        mes =fecha.month
        year =fecha.year
            
        for i in range(1,13):
            mesprox.append( datetime.date(year,i,dia))
        return mesprox 
    
    
    
      