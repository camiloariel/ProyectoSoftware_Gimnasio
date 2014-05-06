from PyQt4.QtGui import *
import sys
from view.gestionCancha2 import GestionCancha2
from menu import Menu

class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()         
                       
        
        screen_rect = app.desktop().screenGeometry()
        self.width, self.height = screen_rect.width(), screen_rect.height()
        with open("images/stilo.css") as f:
                    self.setStyleSheet(f.read()) 
        self.ventana = GestionCancha2(self)
        self.setWindowTitle('GIMNASIO')
        self.resize(self.width,self.height)
        self.setCentralWidget(self.ventana)
        


app = QApplication([])
main = Main()
main.showFullScreen()
sys.exit(app.exec_())