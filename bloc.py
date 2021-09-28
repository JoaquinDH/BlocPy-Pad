
from PyQt5.QtWidgets import *
import sys

f = open("texto.txt", "r")
leido = f.readlines()
    

class VentanaPrincipal(QMainWindow):
    def __init__(self,):
        super().__init__()
        ancho = 800
        alto = 600
        posicionIzquierda = 200
        posicionDerecha = 100

        self.setGeometry(posicionIzquierda, posicionDerecha, ancho, alto)
        self.setWindowTitle("Mi Hijo")

        contenedorVertical = QVBoxLayout()
        boton = QPushButton()
        

        widgetPrincipal = QWidget()
        widgetPrincipal.setLayout(contenedorVertical)

        

        self.setCentralWidget(widgetPrincipal)

        contenedorHorizontal = QHBoxLayout()
       
        botonSaludar = QPushButton("Cargar")
        contenedorHorizontal.addWidget(botonSaludar)

        contenedorVertical.addLayout(contenedorHorizontal)


        boton4 = QPushButton()
        boton4.setText("Guardar")
        contenedorHorizontal.addWidget(boton4)

        texto = QTextEdit()
        texto.setText(leido)
        contenedorVertical.addWidget(texto)





app = QApplication(sys.argv)

ventana = VentanaPrincipal()
ventana.show()
app.exec()