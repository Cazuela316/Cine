import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QBoxLayout, QLineEdit, QMessageBox, QCheckBox, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from Admin import AdminVista

class Ventana(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicializar() 
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        AdminVista_widget = AdminVista(self)
        #entrar_admin_button.clicked.connect(self.mostrar_mensaje)
        self.central_widget.addWidget(self.AdminVista_widget)   

    def crear_widget_inicio(self):
        widget = QWidget()
        layout = QVBoxLayout()
        button = QPushButton('Ir a Prueba')
        button.clicked.connect(self.entrar_Admin)
        layout.addWidget(button)
        widget.setLayout(layout)
        return widget

    def entrar_Admin(self):
        self.central_widget.setCurrentWidget(self.AdminVista_widget)

    def inicializar(self):  
        self.setWindowTitle("Cine")
        self.setGeometry(50, 50, 1450, 720)

        layout = QVBoxLayout()

        Hola_label = QLabel (self)
        Hola_label.setText("Bienvenido a Cinema")
        Hola_label.setFont(QFont('Times New Roman', 30))
        Hola_label.adjustSize()
        Hola_label.move(550, 15)
        
        inicio_label = QLabel(self)
        inicio_label.setText("Iniciar sesion como: ")
        inicio_label.setFont(QFont('Times New Roman', 15))
        inicio_label.adjustSize()
        inicio_label.move(650, 200)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        Cliente_button = QPushButton(self)
        Cliente_button.setText('Cliente')
        Cliente_button.setFont(QFont('Times New Roman', 10))
        Cliente_button.adjustSize()
        Cliente_button.resize(200, 50)
        Cliente_button.move(630, 220)

        Admin_button = QPushButton(self)
        Admin_button.setText('Administrador')
        Admin_button.setFont(QFont('Times New Roman', 10))
        Admin_button.adjustSize()
        Admin_button.resize(200, 50)
        Admin_button.move(630, 280)
        Admin_button.clicked.connect(self.entrar_Admin)

