import os
from PyQt5 import QtGui
from PyQt5.QtCore import QFile, QFileInfo, QUrl
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

    #Funciones
        def abrir(self):
            dialog.exec() 
            seleccionado = dialog.selectedFiles()       

            str1 = ''.join(seleccionado)

            name = (os.path.basename(str1))

            f = open(name, "r")
            leido = f.read()
            
            texto.setText(leido)
            f.close()

        
        def guardar(self):
            nombre = QFileDialog.getSaveFileName()
            str1 = ''.join(nombre)

            name = (os.path.basename(str1))
    
            name = (name.replace('All Files (*)', ''))
         
            f = open(name, "w")
            
            escritura = texto.toPlainText()

            f.write(escritura)




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

        botonAbrir.clicked.connect(abrir)
       
    #Se prepara el contenedor horizontal
        contenedorVertical.addLayout(contenedorHorizontal)

    #Boton guardar
        botonGuardar = QPushButton()
        botonGuardar.setText("Guardar")
        contenedorHorizontal.addWidget(botonGuardar)

        botonGuardar.clicked.connect(guardar)

        

    #Boton Nuevo..
        botonNuevo = QPushButton("Nuevo..")
        contenedorHorizontal.addWidget(botonNuevo)

    #Selector de File para botonAbrir
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)

        
    #Selector de File para botonGuardar

        


    #Parte del texto
        texto = QTextEdit()
        contenedorVertical.addWidget(texto)

        
        
     
    
app = QApplication(sys.argv)

ventana = VentanaPrincipal()
ventana.show()
app.exec()
