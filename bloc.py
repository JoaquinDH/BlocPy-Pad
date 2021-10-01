import threading
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

            if name != "":
                

                f = open(name, "r")
                leido = f.read()
                
                texto.setText(leido)
                f.close()
            else:
                x = pop.exec_()
        
        def guardar(self):   
            nombre = QFileDialog.getSaveFileName()
            str1 = ''.join(nombre)

            name = (os.path.basename(str1))
    
            name = (name.replace('All Files (*)', ''))
         
            if name != "":
                f = open(name, "w")
                
                escritura = texto.toPlainText()

                f.write(escritura)
            else:
                x = pop2.exec_()
                

    #Se crea el contenedor vertical
        contenedorVertical = QVBoxLayout()

    #Para que ande el contendeor vertical
        widgetPrincipal = QWidget()
        widgetPrincipal.setLayout(contenedorVertical)

        self.setCentralWidget(widgetPrincipal)

    #Contenedor horizontal
        contenedorHorizontal = QHBoxLayout()

    #PopUp
        pop = QMessageBox()
        pop.setWindowTitle("Oh no no no")
        pop.setText("Ningun archivo elegido, instalando Bonzi Buddy...")

    #PopUp2
        pop2 = QMessageBox()
        pop2.setWindowTitle("ok")
        pop2.setText("ok")


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
        

    #Selector de File para botonAbrir
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)

         
    #Parte del texto
        texto = QTextEdit()
        contenedorVertical.addWidget(texto)

    #Word Counter
        contador = QLabel()   
        contenedorVertical.addWidget(contador)
        contador.setText("")
        
        def printit():
            threading.Timer(1.0, printit).start()
            contadorPlain = texto.toPlainText()
            contadorLength = len(contadorPlain)
            contador.setText(str(contadorLength))

        printit()
        
            
    
app = QApplication(sys.argv)

ventana = VentanaPrincipal()
ventana.show()
app.exec()
