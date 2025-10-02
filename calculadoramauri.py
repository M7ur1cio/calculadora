import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
)

class Calculadora(QWidget):
    """Clase principal para la calculadora."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora con PyQt6")
        self.setGeometry(100, 100, 300, 400)
        self.ui_iniciada()

    def ui_iniciada(self):
        """Inicializa la interfaz de usuario de la calculadora."""
        
        grid = QGridLayout()

       
        self.display = QLineEdit()
        self.display.setReadOnly(True)  
        self.display.setFixedHeight(50)
        grid.addWidget(self.display, 0, 0, 1, 4)  

       
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 1, 4)  
        ]

       
        for texto, fila, col, *span in botones:
            boton = QPushButton(texto)
            boton.setFixedSize(50, 50)
            

            if texto == '=':
                boton.clicked.connect(self.calcular_resultado)
                grid.addWidget(boton, fila, col, *span)
            elif texto == 'C':
                boton.clicked.connect(self.limpiar_pantalla)
                grid.addWidget(boton, fila, col)
            else:
                boton.clicked.connect(self.agregar_texto_a_pantalla)
                grid.addWidget(boton, fila, col)

        self.setLayout(grid)

    def agregar_texto_a_pantalla(self):
        """Agrega el texto del botón presionado a la pantalla."""
       
        boton = self.sender()
        texto_actual = self.display.text()
        nuevo_texto = texto_actual + boton.text()
        self.display.setText(nuevo_texto)

    def calcular_resultado(self):
        """Evalúa la expresión en la pantalla y muestra el resultado."""
        try:
            expresion = self.display.text()

            resultado = str(eval(expresion))
            self.display.setText(resultado)
        except Exception:
            
            self.display.setText("Error")

    def limpiar_pantalla(self):
        """Limpia la pantalla de la calculadora."""
        self.display.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec())
