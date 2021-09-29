
from PyQt5.QtWidgets import *
import sys

#Abrir
def leer(self, e):
    f = open("texto.txt", "r")
    self.leido = f.readline()
    
    self.texto.setText(self.leido)



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

    #Boton Nuevo..
        botonNuevo = QPushButton("Nuevo..")
        contenedorHorizontal.addWidget(botonNuevo)

    #Parte del texto
        self.texto = QTextEdit()
        contenedorVertical.addWidget(self.texto)
        
        botonAbrir.clicked.connect(leer(self))




app = QApplication(sys.argv)

ventana = VentanaPrincipal()
ventana.show()
app.exec()