
from PyQt5.QtWidgets import *
import sys


class VentanaPrincipal(QMainWindow):
    #Propiedades de la ventana 
    def __init__(self):
        super().__init__()
        ancho = 800
        alto = 600
        posicionIzquierda = 100
        posicionDerecha = 100

        self.setGeometry(posicionIzquierda, posicionDerecha, ancho, alto)
        self.setWindowTitle("Blocpy Pad")

    #Se crea el contenedor vertical
        contenedorVertical = QVBoxLayout()

    #Para que ande el contendeor vertical
        widgetPrincipal = QWidget()
        widgetPrincipal.setLayout(contenedorVertical)

        self.setCentralWidget(widgetPrincipal)

    #Contenedor horizontal
        contenedorHorizontal = QHBoxLayout()
       
    #Boton abrir
        botonAbrir = QPushButton("Abrir")
        contenedorHorizontal.addWidget(botonAbrir)

    #Se prepara el contenedor horizontal
        contenedorVertical.addLayout(contenedorHorizontal)

    #Boton guardar
        botonGuardar = QPushButton()
        botonGuardar.setText("Guardar")
        contenedorHorizontal.addWidget(botonGuardar)

        def open(self):
            dialog.open() 

    #Boton Nuevo..
        botonNuevo = QPushButton("Nuevo..")
        contenedorHorizontal.addWidget(botonNuevo)

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        

        botonAbrir.clicked.connect(open)
        
          

    ###########################################################3
app = QApplication(sys.argv)

ventana = VentanaPrincipal()
ventana.show()
app.exec()
