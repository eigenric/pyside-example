#!/usr/bin/python

# Importamos las clases de Pyside

import sys
from PySide.QtCore import *
from PySide.QtGui import *

# Creamos una aplicacion Qt

app = QApplication(sys.argv)

# Creamos una etiqueta y la mostramos

label = QLabel("<p style='color:red; font-size:40px;'>Hola Mundo</p>")
label.show()

app.exec_()
sys.exit()
