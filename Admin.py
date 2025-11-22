from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QVBoxLayout
from PyQt6.QtGui import QFont

class AdminVista(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicio()
        layout = QVBoxLayout()
        label = QLabel('¡Estás en la ventana Prueba!')
        layout.addWidget(label)
        self.setLayout(layout)

    def inicio(self):
        self.setGeometry(50, 50, 1450, 720)
        self.setWindowTitle("Inicio Admin")

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