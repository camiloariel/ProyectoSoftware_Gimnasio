'''
Created on 19-04-2014
@author: Omar
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import datetime
import calendar





class TablaCalendario(QTableWidget):
    '''
    classdocs
    '''

    def __init__(self,fecha, table):
        '''
        Constructor
        '''      
        super(TablaCalendario, self).__init__()    
        self.calendarioTabla(fecha)
        self.main = table


    def calendarioTabla(self,fecha):
        self.setSortingEnabled(False)
        self.verticalHeader().setVisible(False)
        self.setGridStyle(False)    
        self.setColumnCount(7)
        self.setRowCount(6)
        self.setFixedHeight(160)
        for i in range(7):
            self.setColumnWidth(i,19)
            self.setRowHeight(i,19)
        
        self.setHorizontalHeaderLabels(['L', 'M', 'M', 'J', 'V', 'S', 'D'])
        self.llenatabla(fecha.year,fecha.month) 
        self.setFixedWidth(134)
        
       
        
        
    def llenatabla(self,year,mes):    

       
        self.setHorizontalHeaderLabels(['L', 'M', 'M', 'J', 'V', 'S', 'D'])
        diaMes = calendar.monthrange(year,mes) 
        if mes-1 <1:
            mes=11
            year = year-1
        else: mes = mes-1
        diaMesAnterior = calendar.monthrange(year,mes) 
        a = diaMes[0]  
        b = diaMesAnterior[1] #cantidad de dias del mes Anterior
        d = 0     # dias faltantes del mes anterior
   
   
        for s in range(0,6):
            for i in range(a,7):
                d = d + 1                  
                if (d <= diaMes[1]): 
                   item =  QTableWidgetItem(str(d))
                   item.setFlags(Qt.ItemIsEnabled |Qt.ItemIsSelectable )
                   self.setItem(s,i,item)
             #cambio      
                
            a=0
        b=0
        
    
    
    def limpiaTabla(self):
        self.clear()
        
        
    def selectFecha(self, mes,year):
        
        r= self.currentRow()
        c= self.currentColumn()
        mesList = {'Enero':'01','Febrero':'02','Marzo':'03',
       'Abril':'04','Mayo':'05','Junio':'06',
       'Julio':'07','Agosto':'08','Septiembre':'09',
       'Octubre':'10','Noviembre':'11','Diciembre':'12'}
        dia = self.item(r, c).text()
        self.main.cambiaFecha(year+"-"+mesList[str(mes)]+"-"+dia)
        