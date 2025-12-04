import sys
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QStackedWidget, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class ResumenVista(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.inicializar()

    def inicializar(self):
        titulo_label = QLabel(self)
        titulo_label.setText("¡Boletos comprados!")
        titulo_label.setFont(QFont('Belanosima', 35))
        titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_label.setGeometry(400, 30, 650, 60)

        self.resumen_text = QTextEdit(self) 
        self.resumen_text.setReadOnly(True)
        self.resumen_text.setFont(QFont('Times New Roman', 14))
        self.resumen_text.setGeometry(300, 120, 850, 450)

        volver_button = QPushButton(self)
        volver_button.setText("Volver al inicio")
        volver_button.setFont(QFont('Belanosima', 12))
        volver_button.setGeometry(20, 20, 300, 50)
        volver_button.clicked.connect(self.volver_inicio)
    
    def mostrar_resumen(self, venta, sala):
        filas = ['A', 'B', 'C', 'D', 'E']
        resumen = "ღ"*124+"\n\n"
        resumen+= "~ Resumen ~\n"
        resumen+= f"    Sala: {sala.Numero}\n"
        resumen+= f"    Pelicula: {venta.Funcion.Pelicula}\n"
        resumen+= f"    Horario: {venta.Funcion.Horario}\n"
        resumen+= f"    Cantidad de entradas: {len(venta.asientos)}\n"
        resumen+= f"    Precio por entrada: $3000\n"
        resumen+= f"    Asientos comprados: "
        for asiento in venta.asientos:
            resumen += f" {filas[asiento.Fila]}{asiento.Columna+1} "
        resumen += "ღ"*62+"\n\n"
        resumen += f"Total: ${venta.Total}\n\n\n"
        resumen += "ღ"*124+"\n"

        self.resumen_text.setPlainText(resumen)

    def volver_inicio(self):
        ventana_principal = self.window()
        if hasattr(ventana_principal, 'mostrar_inicio'):
            ventana_principal.mostrar_inicio()

class MenuAdminVista(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.inicializar()

    def inicializar(self):
        titulo_label = QLabel(self)
        titulo_label.setText("Has entrado como Administrador")
        titulo_label.setFont(QFont('Tektur', 35))
        titulo_label.setStyleSheet("color: #41E329;")
        titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_label.setGeometry(370, 50, 760, 60)

        subtitulo_label = QLabel(self)
        subtitulo_label.setText("Elija el resumen que quiera ver: ")
        subtitulo_label.setFont(QFont('Tektur', 16))
        subtitulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitulo_label.setGeometry(400, 130, 650, 40)

        sala_button = QPushButton(self)
        sala_button.setText("Resumen de Ventas por Sala")
        sala_button.setFont(QFont('Tektur', 14))
        sala_button.setGeometry(525, 210, 400, 60)
        sala_button.clicked.connect(lambda: self.ver_reporte('sala'))

        funcion_button = QPushButton(self)
        funcion_button.setText("Resumen de Ventas por Función")
        funcion_button.setFont(QFont('Tektur', 14))
        funcion_button.setGeometry(525, 210 + 80, 400, 60)
        funcion_button.clicked.connect(lambda: self.ver_reporte('funcion'))

        horario_button = QPushButton(self)
        horario_button.setText("Resumen de Ventas por Horario")
        horario_button.setFont(QFont('Tektur', 14))
        horario_button.setGeometry(525, 210 + 80*2, 400, 60)
        horario_button.clicked.connect(lambda: self.ver_reporte('horario'))

        general_button = QPushButton(self)
        general_button.setText("Resumen General del Dia")
        general_button.setFont(QFont('Tektur', 14))
        general_button.setGeometry(525, 210 + 80*3, 400, 60)
        general_button.clicked.connect(lambda: self.ver_reporte('general'))

        cerrar_button = QPushButton(self)
        cerrar_button.setText("Cerrar Sesion")
        cerrar_button.setFont(QFont('Tektur', 12))
        cerrar_button.setGeometry(20, 20, 200, 50)
        cerrar_button.clicked.connect(self.cerrar_sesion)

    def ver_reporte(self, tipo_reporte):
        ventana_principal = self.window()
        if hasattr(ventana_principal, 'mostrar_reportes'):
            ventana_principal.mostrar_reportes(tipo_reporte)
    
    def cerrar_sesion(self):
        ventana_principal = self.window()
        if hasattr(ventana_principal, 'mostrar_inicio'):
            ventana_principal.mostrar_inicio()