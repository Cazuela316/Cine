import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QBoxLayout, QLineEdit, QMessageBox, QCheckBox, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap

class Inicio(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.inicializar()

    def inicializar(self):

        Hola_label = QLabel (self)
        Hola_label.setText("Bienvenido a Cinema")
        Hola_label.setFont(QFont('Times New Roman', 30))
        Hola_label.adjustSize()
        Hola_label.move(520, 15)
        
        inicio_label = QLabel(self)
        inicio_label.setText("Iniciar sesion como: ")
        inicio_label.setFont(QFont('Times New Roman', 15))
        inicio_label.adjustSize()
        inicio_label.move(650, 200)

        Cliente_button = QPushButton(self)
        Cliente_button.setText('Cliente')
        Cliente_button.setFont(QFont('Times New Roman', 10))
        Cliente_button.adjustSize()
        Cliente_button.resize(200, 50)
        Cliente_button.move(630, 220)
        Cliente_button.clicked.connect(self.entrar_cliente)

        Admin_button = QPushButton(self)
        Admin_button.setText('Administrador')
        Admin_button.setFont(QFont('Times New Roman', 10))
        Admin_button.adjustSize()
        Admin_button.resize(200, 50)
        Admin_button.move(630, 280)
        Admin_button.clicked.connect(self.entrar_admin)

    def entrar_cliente(self):
        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):
            ventana_principal.mostrar_salas()   

    def entrar_admin(self):
        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):
            ventana_principal.mostrar_admin()

class AdminVista(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicio()

    def inicio(self):
        self.titulo_label = QLabel(self)
        self.titulo_label.setText("Ha entrado como Administrador ")
        self.titulo_label.setFont(QFont('Times New Roman', 30))
        self.titulo_label.adjustSize()
        self.titulo_label.move(500, 20)

        usuario_label = QLabel(self)
        usuario_label.setText("Usuario:")
        usuario_label.setFont(QFont('Times New Roman', 15))
        usuario_label.adjustSize()
        usuario_label.move(100, 250)

        self.usuario_input = QLineEdit(self)
        self.usuario_input.resize(250, 40)
        self.usuario_input.move(180, 240)

        contra_label = QLabel(self)
        contra_label.setText("Contraseña:")
        contra_label.setFont(QFont('Times New Roman', 15))
        contra_label.adjustSize()
        contra_label.move(100, 350)

        self.contra_input = QLineEdit(self)
        self.contra_input.resize(250, 40)
        self.contra_input.move(200, 340)

        ingresar_button = QPushButton(self)
        ingresar_button.setText('Ingresar')
        ingresar_button.setFont(QFont('Times New Roman', 12))
        ingresar_button.adjustSize()
        ingresar_button.resize(200, 50)
        ingresar_button.move(140, 450)
        ingresar_button.clicked.connect(self.validar_inicio)

        volver_button = QPushButton(self)
        volver_button.setText('Volver al inicio')
        volver_button.setFont(QFont('Times New Roman', 12))
        volver_button.adjustSize()
        volver_button.resize(200, 50)
        volver_button.move (10,15)
        volver_button.clicked.connect(self.volver_inicio)

    def validar_inicio(self):
        usuario = self.usuario_input.text()
        contra = self.contra_input.text()

        if usuario == "admin" and contra == "1234":
            QMessageBox.information(self, "Bienvenido al inicio como Administrador")
            #cambio vista
        elif usuario == "" or contra == "":
            QMessageBox.warning(self, "Error", "Faltan datos")
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def volver_inicio(self):
        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):
            ventana_principal.mostrar_inicio()

class SalasVista(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.inicializar()

    def inicializar(self):
        titulo_label = QLabel(self)
        titulo_label.setText("Selecciona una sala")
        titulo_label.setFont(QFont('Times New Roman', 30))
        titulo_label.adjustSize()
        titulo_label.move(550, 15)
        
        Sala1_button = QPushButton(self)
        Sala1_button.setText("Sala 1")
        Sala1_button.setFont(QFont('Times New Roman', 15))
        Sala1_button.adjustSize()
        Sala1_button.resize(200, 40)
        Sala1_button.move(630,220)
        Sala1_button.clicked.connect(lambda: self.seleccionar_sala(1))

        Sala2_button = QPushButton(self)
        Sala2_button.setText("Sala 2")
        Sala2_button.setFont(QFont('Times New Roman', 15))
        Sala2_button.adjustSize()
        Sala2_button.resize(200, 40)
        Sala2_button.move(630, 280)
        Sala2_button.clicked.connect(lambda: self.seleccionar_sala(2))

        Sala3_button = QPushButton(self)
        Sala3_button.setText("Sala 3")
        Sala3_button.setFont(QFont('Times New Roman', 15))
        Sala3_button.adjustSize()
        Sala3_button.resize(200, 40)
        Sala3_button.move(630, 350)
        Sala3_button.clicked.connect(lambda: self.seleccionar_sala(3))

        volver_button = QPushButton(self)
        volver_button.setText('Volver al inicio')
        volver_button.setFont(QFont('Times New Roman', 12))
        volver_button.adjustSize()
        volver_button.resize(200, 50)
        volver_button.move (10,15)
        volver_button.clicked.connect(self.volver_inicio)

    def seleccionar_sala(self, numero_sala):
        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):
            ventana_principal.mostrar_pelis(numero_sala)

    def volver_inicio(self):
        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):
            ventana_principal.mostrar_inicio()

class FuncionesVista(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.sala_actual = 1
        self.funciones_porSala = {
            1: ["Peli 1 - matine", "Peli 2 - vermut", "Peli 3 - vespertino"], 
            2: ["Peli 4 - matine", "Peli 5 - vermut", "Peli 6 - vespertino"], 
            3: ["Peli 7 - matine", "Peli 8 - vermut", "Peli 9 - vespertino"]
        }
        self.inicializar()

    def inicializar(self):
        self.titulo_label = QLabel(self)
        self.titulo_label.setText("Funciones - Sala 1")
        self.titulo_label.setFont(QFont('Times New Roman', 30))
        self.titulo_label.adjustSize()
        self.titulo_label.move(550, 15)

        self.Peli1_button = QPushButton(self)
        self.Peli1_button.setText("Funcion 1 - Matine")
        self.Peli1_button.setFont(QFont('Times New Roman', 15))
        self.Peli1_button.adjustSize()
        self.Peli1_button.resize(200, 40)
        self.Peli1_button.move(630,220)
        self.Peli1_button.clicked.connect(lambda: self.seleccionar_funcion(0))

        self.Peli2_button = QPushButton(self)
        self.Peli2_button.setText("Funcion 2 - Vermut")
        self.Peli2_button.setFont(QFont('Times New Roman', 15))
        self.Peli2_button.adjustSize()
        self.Peli2_button.resize(200, 40)
        self.Peli2_button.move(630, 280)
        self.Peli2_button.clicked.connect(lambda: self.seleccionar_funcion(1))

        self.Peli3_button = QPushButton(self)
        self.Peli3_button.setText("Funcion 3 - Vespertino")
        self.Peli3_button.setFont(QFont('Times New Roman', 15))
        self.Peli3_button.adjustSize()
        self.Peli3_button.resize(200, 40)
        self.Peli3_button.move(630, 350)
        self.Peli3_button.clicked.connect(lambda: self.seleccionar_funcion(2))

        volver_button = QPushButton(self)
        volver_button.setText('Volver a las salas')
        volver_button.setFont(QFont('Times New Roman', 12))
        volver_button.adjustSize()
        volver_button.resize(200, 50)
        volver_button.move (10,15)
        volver_button.clicked.connect(self.volver_salas)

    def set_sala(self, numero_sala):  #metodo setter, para que cambien las pelis segun la sala que eliga
        self.sala_actual = numero_sala
        self.titulo_label.setText(f'Funciones - Sala {numero_sala}')
        pelis = self.funciones_porSala[numero_sala]
        self.Peli1_button.setText(pelis[0])
        self.Peli2_button.setText(pelis[1])
        self.Peli3_button.setText(pelis[2])

    def seleccionar_funcion(self, indice):
        Funcion = self.funciones_porSala[self.sala_actual][indice]
        QMessageBox.warning(self, "Desarrollo")

    def volver_salas(self):
        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):
            ventana_principal.mostrar_salas()
        


class VentanaP(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicializar() 

    def inicializar(self):  
        self.setWindowTitle("Cine")
        self.setGeometry(50, 50, 1450, 720)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.vista_inicio = Inicio(self)
        self.vista_salas = SalasVista(self)
        self.vista_pelis = FuncionesVista(self)
        self.vista_admin = AdminVista(self)

        self.central_widget.addWidget(self.vista_inicio)
        self.central_widget.addWidget(self.vista_salas)
        self.central_widget.addWidget(self.vista_pelis)
        self.central_widget.addWidget(self.vista_admin)

        self.central_widget.setCurrentWidget(self.vista_inicio)

    def mostrar_inicio(self):
        self.central_widget.setCurrentWidget(self.vista_inicio)

    def mostrar_salas(self):
        self.central_widget.setCurrentWidget(self.vista_salas)

    def mostrar_pelis(self, numero_sala):
        self.vista_pelis.set_sala(numero_sala)
        self.central_widget.setCurrentWidget(self.vista_pelis)
        
    def mostrar_admin(self):
        self.central_widget.setCurrentWidget(self.vista_admin)