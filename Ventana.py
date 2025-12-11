import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from AsientosVista import AsientosVista
from ReporteVista import ReporteVista
from Resumenes import ResumenVista, MenuAdminVista

class InicioVista(QWidget):
    def __init__(self, salas, parent = None):
        super().__init__(parent)
        self.salas = salas
        self.inicializar()

    def inicializar(self):
        self.NombredePelis = {
        # Esto sirve para "Etiquetar" las peliculas, para que tengan nombre
        "Shrek": "Peli1",
        "Five Nights At Freddy's": "Peli2", 
        "Five Nights At Freddy's 2": "Peli3",
        "Interestelar": "Peli4",
        "Avengers: Endgame": "Peli5",
        "El Señor De Los Anillos": "Peli6",
        "Zootopia 2": "Peli7",
        "Project Sekai: Miku No Puede Cantar": "Peli8",
        "Chiikawa: El Secreto de la Isla Marina": "Peli9"
    }
        Hola_label = QLabel (self)
        Hola_label.setText("¡Bienvenido a Cinema!")
        Hola_label.setFont(QFont('Belanosima', 30))
        #El "SetSytleSheet" sirve para decorar usando CSS, todos los comandos de css sirven para PyQt6
        Hola_label.setStyleSheet("color: #e46e2a;")
        Hola_label.adjustSize()
        Hola_label.move(520, 15)
        
        Admin_button = QPushButton(self)
        Admin_button.setText('Administrador')
        Admin_button.setFont(QFont('Tektur', 10))
        Admin_button.setGeometry(1330, 10, 100, 35)
        Admin_button.clicked.connect(self.entrar_admin)

        sala1_label = QLabel(self)
        sala1_label.setText("Sala 1")
        sala1_label.setFont(QFont('Lokeya', 18))
        sala1_label.setGeometry(100, 150, 150, 40)
    #   Este for sirve para poner las imagenes, junto con el boton para poder comprar la entrada 
        for i, funcion in enumerate(self.salas[0].Funciones): 
            if funcion:
                asientos_disponibles = sum(1 for fila in funcion.Asientos for asiento in fila if asiento == 0)
                imagen_label = QLabel(self)
                nombre_archivo = self.NombredePelis.get(funcion.Pelicula, funcion.Pelicula)
                # Este if sirve para verificar si la pelicula esta disponible (Si es que tiene asientos disponibles)
                # Si es que no, se reemplaza la imagen del poster con una señal de "Sold Out"
                if asientos_disponibles == 0:
                    pixmap = QPixmap(f"img/{nombre_archivo}x.png")
                else:
                    pixmap = QPixmap(f"img/{nombre_archivo}.png")
                pixmap = pixmap.scaled(100, 140)
                imagen_label.setPixmap(pixmap)
                imagen_label.setGeometry(390 + i*350, 70, 100, 140)
                seleccion_button = QPushButton(self)
                seleccion_button.setText(f"{funcion.Pelicula}\n({funcion.Horario})")
                seleccion_button.setFont(QFont('Dosis', 12))
                seleccion_button.setGeometry(280 + i*350, 220, 320, 50)
                seleccion_button.clicked.connect(lambda checked, s=self.salas[0], iax=i: self.seleccionar_funcion(s,iax))

        sala2_label = QLabel(self)
        sala2_label.setText("Sala 2")
        sala2_label.setFont(QFont('Lokeya', 18))
        sala2_label.setGeometry(100, 340, 150, 40)
        

        for i, funcion in enumerate(self.salas[1].Funciones):
            if funcion:
                asientos_disponibles = sum(1 for fila in funcion.Asientos for asiento in fila if asiento == 0)
                imagen_label2 = QLabel(self)
                nombre_archivo = self.NombredePelis.get(funcion.Pelicula, funcion.Pelicula)
                if asientos_disponibles == 0:
                    pixmap = QPixmap(f"img/{nombre_archivo}x.png")
                else:
                    pixmap = QPixmap(f"img/{nombre_archivo}.png")
                pixmap = pixmap.scaled(100, 140)
                imagen_label2.setPixmap(pixmap)
                imagen_label2.setGeometry(390 + i*350, 290, 100, 140)
                seleccion2_button = QPushButton(self)
                seleccion2_button.setText(f"{funcion.Pelicula}\n({funcion.Horario})")
                seleccion2_button.setFont(QFont('Dosis', 12))
                seleccion2_button.setGeometry(280 + i*350, 440, 320, 50)
                seleccion2_button.clicked.connect(lambda checked, s=self.salas[1], iax=i: self.seleccionar_funcion(s,iax))

        sala3_label = QLabel(self)
        sala3_label.setText("Sala 3")
        sala3_label.setFont(QFont('Lokeya', 18))
        sala3_label.setGeometry(100, 550, 150, 40)

        for i, funcion in enumerate(self.salas[2].Funciones):
            if funcion:
                asientos_disponibles = sum(1 for fila in funcion.Asientos for asiento in fila if asiento == 0)
                imagen_label3 = QLabel(self)
                nombre_archivo = self.NombredePelis.get(funcion.Pelicula, funcion.Pelicula)
                if asientos_disponibles == 0:
                    pixmap = QPixmap(f"img/{nombre_archivo}x.png")
                else:
                    pixmap = QPixmap(f"img/{nombre_archivo}.png")
                pixmap = pixmap.scaled(100, 140)
                imagen_label3.setPixmap(pixmap)
                imagen_label3.setGeometry(390 + i*350, 510, 100, 140)
                seleccion3_button = QPushButton(self)
                seleccion3_button.setText(f"{funcion.Pelicula}\n({funcion.Horario})")
                seleccion3_button.setFont(QFont('Dosis', 12))
                seleccion3_button.setGeometry(280 + i*350, 660, 320, 50)
                seleccion3_button.clicked.connect(lambda checked, s=self.salas[2], iax=i: self.seleccionar_funcion(s,iax))

    def seleccionar_funcion(self, sala, indice):
        funcion = sala.Funciones[indice]

        asientos_disponibles = 0
        for i in range (5):
            for j in range (5):
                if funcion.Asientos[i][j] == 0:
                    asientos_disponibles +=1

        if asientos_disponibles == 0: 
            QMessageBox.warning (self, "Sala llena", f"Lo sentimos, la funcion de {funcion.Pelicula} ({funcion.Horario}) esta llena\n\n" f"Por lo tanto no quedan asientos disponibles. Porfavor eliga otra funcion")
            ventana_principal = self.window()
            if hasattr(ventana_principal, 'mostrar_inicio'):
                    ventana_principal.mostrar_inicio()
            return
        
        ventana_principal = self.window()
        if hasattr(ventana_principal, 'mostrar_asientos'):
            ventana_principal.mostrar_asientos(sala, indice)

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
        self.titulo_label.setText("Ingrese sus datos de administrador: ")   
        self.titulo_label.setFont(QFont('Tektur', 30))
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_label.setGeometry(400, 50, 730, 50)

        usuario_label = QLabel(self)
        usuario_label.setText("Usuario:")
        usuario_label.setFont(QFont('Tektur', 15))
        usuario_label.setGeometry(500, 200, 100, 30)

        self.usuario_input = QLineEdit(self)
        self.usuario_input.setFont(QFont('Times New Roman', 12))
        self.usuario_input.setGeometry(600, 195, 300, 40)

        contra_label = QLabel(self)
        contra_label.setText("Contraseña:")
        contra_label.setFont(QFont('Tektur', 15))
        contra_label.setGeometry(500, 270, 120, 30)

        self.contra_input = QLineEdit(self)
        self.contra_input.setEchoMode(QLineEdit.EchoMode.Password)   
        self.contra_input.setFont(QFont('Times New Roman', 12))
        self.contra_input.setGeometry(620, 265, 280, 40)

        ingresar_button = QPushButton(self)
        ingresar_button.setText('Ingresar')
        ingresar_button.setFont(QFont('Tektur', 12))
        ingresar_button.setGeometry(600, 340, 200, 50)
        ingresar_button.clicked.connect(self.validar_inicio)

        volver_button = QPushButton(self)
        volver_button.setText('Volver al inicio')
        volver_button.setFont(QFont('Tektur', 12))
        volver_button.setGeometry(20, 20, 120, 40)
        volver_button.clicked.connect(self.volver_inicio)

    def validar_inicio(self):
        usuario = self.usuario_input.text()
        contra = self.contra_input.text()

        if usuario == "admin" and contra == "1234":
            ventana_principal = self.window()
            if isinstance(ventana_principal, VentanaP):
                ventana_principal.mostrar_menu_admin()
        elif usuario == "" or contra == "":
            QMessageBox.warning(self, "Error", "¡Faltan datos!")
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

    def volver_inicio(self):
        self.usuario_input.clear()
        self.contra_input.clear()

        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):
            ventana_principal.mostrar_inicio()

class VentanaP(QMainWindow):
    def __init__(self, main_objeto, salas, parent=None):
        super().__init__(parent)
        self.main_objeto = main_objeto
        self.salas = salas
        self.inicializar() 

    def inicializar(self):  
        self.setWindowTitle("Cinema -1")
        self.setGeometry(50, 50, 1450, 720)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.vista_inicio = InicioVista(self.salas, self)
        self.vista_admin = AdminVista(self)
        self.vista_asientos = AsientosVista(self)
        self.vista_resumen = ResumenVista(self)
        self.vista_menu_admin = MenuAdminVista(self)
        self.vista_reportes = ReporteVista(self)
        
        self.vista_reportes.set_datos(self.main_objeto, self.salas)

        self.central_widget.addWidget(self.vista_inicio)
        self.central_widget.addWidget(self.vista_admin)
        self.central_widget.addWidget(self.vista_asientos)
        self.central_widget.addWidget(self.vista_resumen)
        self.central_widget.addWidget(self.vista_menu_admin)
        self.central_widget.addWidget(self.vista_reportes)

        self.central_widget.setCurrentWidget(self.vista_inicio)

    def mostrar_inicio(self):
        self.central_widget.setCurrentWidget(self.vista_inicio)
        
        #Elimina la vista anterior
        self.central_widget.removeWidget(self.vista_inicio)
    
        #Crea una nueva vista con los datos actualizados
        self.vista_inicio = InicioVista(self.salas, self)
    
        #Agrega la nueva vista en la misma posición (en el indice 0)
        self.central_widget.insertWidget(0, self.vista_inicio)
    
        #Muestra la nueva vista
        self.central_widget.setCurrentWidget(self.vista_inicio)

    def mostrar_admin(self):
        self.central_widget.setCurrentWidget(self.vista_admin)

    def mostrar_asientos(self, sala_obj, indice_funcion):
        funcion = sala_obj.Funciones[indice_funcion]
        self.vista_asientos.set_funcion(sala_obj, funcion, indice_funcion, self.main_objeto)
        self.central_widget.setCurrentWidget(self.vista_asientos)
    
    def mostrar_resumen(self, venta, sala):
        self.vista_resumen.mostrar_resumen(venta, sala)
        self.central_widget.setCurrentWidget(self.vista_resumen)

    def mostrar_menu_admin(self):
        self.central_widget.setCurrentWidget(self.vista_menu_admin)
        
    def mostrar_reportes(self, tipo_reporte):
        self.vista_reportes.generar_reporte(tipo_reporte)
        self.central_widget.setCurrentWidget(self.vista_reportes)
    