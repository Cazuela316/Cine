import sys
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox, QStackedWidget, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import Asientos as A

class AsientosVista(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.sala_actual = None  
        self.funcion_actual = None
        self.indice_funcion = None
        self.asientosSeleccionados = []
        self.botonesAsientos = []
        self.inicializar()

    def inicializar(self):
        self.titulo_label = QLabel(self)
        self.titulo_label.setText("Elija sus asientos")
        self.titulo_label.setFont(QFont('Belanosima', 30))
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titulo_label.setStyleSheet("color: #e46e2a;")
        self.titulo_label.setGeometry(400, 20, 650, 50)

        self.info_label = QLabel(self)
        self.info_label.setText("")
        self.info_label.setFont(QFont('Dosis', 22))
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setGeometry(400, 80, 650, 35)

        Cajita_extraña=QFrame(self)
        Cajita_extraña.setGeometry(1120, 300, 220, 130)
        Cajita_extraña.setStyleSheet("border: 2px solid #FFFFFF;")
        
        disponible_label = QLabel(Cajita_extraña)
        disponible_label.setText(" _ = Disponible")
        disponible_label.setFont(QFont('Courier New', 14))
        disponible_label.setStyleSheet("color: #d6def3;  border: none;")
        disponible_label.setGeometry(10, 10, 200, 30)

        ocupado_label = QLabel(Cajita_extraña)
        ocupado_label.setText(" x = Ocupado")
        ocupado_label.setFont(QFont('Courier New', 14))
        ocupado_label.setStyleSheet("color: #d6def3;  border: none;")
        ocupado_label.setGeometry(10, 90, 200, 30)

        seleccionado_label = QLabel(Cajita_extraña)
        seleccionado_label.setText(" o = Seleccionado")
        seleccionado_label.setFont(QFont('Courier New', 14))
        seleccionado_label.setStyleSheet("color: #d6def3; border: none;")
        seleccionado_label.setGeometry(10, 50, 200, 30)

        for j in range(5):
            columna_label = QLabel(str(j+1), self)
            columna_label.setFont(QFont('Courier New', 14))
            columna_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x_posicion = 550 + j*(70 + 5)
            columna_label.setGeometry(x_posicion, 170, 70, 30)
        
        filas = ['A', 'B', 'C', 'D', 'E']

        for i in range(5):
            fila_botones = []
            fila_label = QLabel(self)
            fila_label.setText(filas[i])
            fila_label.setFont(QFont('Courier New', 16))
            x_posicion = 550 - 40
            y_posicion = 210 + i*(70 + 5)
            fila_label.setGeometry(x_posicion, y_posicion, 30, 70)

            for j in range(5):
                Matriz_button = QPushButton(self)
                Matriz_button.setText("_")
                Matriz_button.setFont(QFont('Courier New', 24))
                x_posicion = 550 + j*(70 + 5)
                y_posicion = 210 + i*(70 + 5)
                Matriz_button.setGeometry(x_posicion, y_posicion, 70, 70)
                Matriz_button.clicked.connect(lambda checked, f=i, c=j: self.toggle_asiento(f,c))
                fila_botones.append(Matriz_button)   #
            self.botonesAsientos.append(fila_botones)

        self.total_label = QLabel(self)
        self.total_label.setText("Total: $0")
        self.total_label.setStyleSheet("color: #17c71a;")
        self.total_label.setFont(QFont('Dosis', 18))
        self.total_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.total_label.setGeometry(550, 610, 350, 40)

        volver_button = QPushButton(self)
        volver_button.setText("Volver a las funciones")
        volver_button.setFont(QFont('Lokeya', 12))
        volver_button.setGeometry(20, 20, 200, 50)
        volver_button.clicked.connect(self.volver_funciones)
        
        confirmar_button = QPushButton(self)
        confirmar_button.setText("Confirmar Compra")
        confirmar_button.setFont(QFont('Belanosima', 12))
        confirmar_button.setGeometry(625, 660, 200, 50)
        confirmar_button.clicked.connect(self.confirmar_compra)
    
    def set_funcion(self, sala, funcion, indice_funcion, main_objeto):
        self.sala_actual=sala
        self.funcion_actual=funcion
        self.indice_funcion=indice_funcion
        self.main_objeto = main_objeto
        self.asientosSeleccionados = []

        self.info_label.setText(f"Sala {sala.Numero} - {funcion.Pelicula} ({funcion.Horario})")
        self.actualizar_asientos()
        self.actualizar_total()

    def actualizar_asientos(self):
        for i in range(5):
            for j in range(5):
                Matriz_button = self.botonesAsientos[i][j]
                estado = self.funcion_actual.Asientos[i][j]
                
                if estado == 1:
                    Matriz_button.setText("x")
                else:
                    Matriz_button.setText("_")
    
    def toggle_asiento(self, fila, columna):
        Boton = self.botonesAsientos[fila][columna]
        estado = self.funcion_actual.Asientos[fila][columna]

        if estado == 1:
            QMessageBox.warning(self, "Asiento Ocupado", "Este asiento esta ocupado. Porfavor elija otro")
            return
        
        asiento_coord = (fila, columna) 
        if asiento_coord in self.asientosSeleccionados:
            self.asientosSeleccionados.remove(asiento_coord)
            Boton.setText("_")
        else:
            self.asientosSeleccionados.append(asiento_coord)
            Boton.setText("o")

        self.actualizar_total()

    def actualizar_total(self):
        total = len(self.asientosSeleccionados)*3000
        self.total_label.setText(f"Total: ${total}")

    def confirmar_compra(self):
        if len(self.asientosSeleccionados) == 0:  
            QMessageBox.warning(self, "Error", "Porfavor seleccione asientos")
            return
        
        import Ventas as V
        lista_asientos = []
        for fila, columna in self.asientosSeleccionados:
            asiento = A.Asientos(fila, columna, 0, self.sala_actual)
            lista_asientos.append(asiento)

        venta = V.Venta(None, None, None)
        venta.cantidad_boletos = len(self.asientosSeleccionados)

        for fila, columna in self.asientosSeleccionados:
            self.funcion_actual.Asientos[fila][columna] = 1

        total = len(self.asientosSeleccionados)*3000
        venta.Total = total
        venta.Funcion = self.funcion_actual
        venta.asientos = lista_asientos
        self.funcion_actual.EntradasVendidas+= len(self.asientosSeleccionados)
        self.main_objeto.Holi(venta)
        self.main_objeto.TotalVentasDia += total

        ventana_principal = self.window()
        if hasattr(ventana_principal, 'mostrar_resumen'):
            ventana_principal.mostrar_resumen(venta, self.sala_actual)

    def volver_funciones(self):
        ventana_principal = self.window()
        if hasattr(ventana_principal, 'mostrar_inicio'):
            ventana_principal.mostrar_inicio()