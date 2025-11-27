import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QStackedWidget, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import Asientos as A

class InicioVista(QWidget):
    def __init__(self, salas, parent = None):
        super().__init__(parent)
        self.salas = salas
        self.inicializar()

    def inicializar(self):
        Hola_label = QLabel (self)
        Hola_label.setText("Bienvenido a Cinema")
        Hola_label.setFont(QFont('Cinzel', 30))
        Hola_label.adjustSize()
        Hola_label.move(520, 15)
        
        Admin_button = QPushButton(self)
        Admin_button.setText('Administrador')
        Admin_button.setFont(QFont('Times New Roman', 10))
        Admin_button.setGeometry(1330, 10, 100, 35)
        Admin_button.clicked.connect(self.entrar_admin)

        sala1_label = QLabel(self)
        sala1_label.setText("Sala 1")
        sala1_label.setFont(QFont('Times New Roman', 18))
        sala1_label.setGeometry(100, 150, 150, 40)

        for i, funcion in enumerate(self.salas[0].Funciones): 
            if funcion:
                seleccion_button = QPushButton(self)
                seleccion_button.setText(f"{funcion.Pelicula}\n({funcion.Horario})")
                seleccion_button.setFont(QFont('Times New Roman', 12))
                seleccion_button.setGeometry(280 + i*350, 150, 320, 50)
                seleccion_button.clicked.connect(lambda checked, s=self.salas[0], iax=i: self.seleccionar_funcion(s,iax)) 

        sala2_label = QLabel(self)
        sala2_label.setText("Sala 2")
        sala2_label.setFont(QFont('Times New Roman', 18))
        sala2_label.setGeometry(100, 265, 150, 40)

        for i, funcion in enumerate(self.salas[1].Funciones):
            if funcion:
                seleccion2_button = QPushButton(self)
                seleccion2_button.setText(f"{funcion.Pelicula}\n({funcion.Horario})")
                seleccion2_button.setFont(QFont('Times New Roman', 12))
                seleccion2_button.setGeometry(280 + i*350, 265, 320, 50)
                seleccion2_button.clicked.connect(lambda checked, s=self.salas[1], iax=i: self.seleccionar_funcion(s,iax))

        sala3_label = QLabel(self)
        sala3_label.setText("Sala 3")
        sala3_label.setFont(QFont('Times New Roman', 18))
        sala3_label.setGeometry(100, 380, 150, 40)

        for i, funcion in enumerate(self.salas[2].Funciones):
            if funcion:
                seleccion2_button = QPushButton(self)
                seleccion2_button.setText(f"{funcion.Pelicula}\n({funcion.Horario})")
                seleccion2_button.setFont(QFont('Times New Roman', 12))
                seleccion2_button.setGeometry(280 + i*350, 350, 320, 50)
                seleccion2_button.clicked.connect(lambda checked, s=self.salas[2], iax=i: self.seleccionar_funcion(s,iax))

    def seleccionar_funcion(self, sala, indice):
        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):   
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
        self.titulo_label.setFont(QFont('Times New Roman', 30))
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_label.setGeometry(450, 50, 570, 50)

        usuario_label = QLabel(self)
        usuario_label.setText("Usuario:")
        usuario_label.setFont(QFont('Times New Roman', 15))
        usuario_label.setGeometry(500, 200, 100, 30)

        self.usuario_input = QLineEdit(self)
        self.usuario_input.setFont(QFont('Times New Roman', 12))
        self.usuario_input.setGeometry(600, 195, 300, 40)

        contra_label = QLabel(self)
        contra_label.setText("Contraseña:")
        contra_label.setFont(QFont('Times New Roman', 15))
        contra_label.setGeometry(500, 270, 120, 30)

        self.contra_input = QLineEdit(self)
        self.contra_input.setEchoMode(QLineEdit.EchoMode.Password)   
        self.contra_input.setFont(QFont('Times New Roman', 12))
        self.contra_input.setGeometry(620, 265, 280, 40)

        ingresar_button = QPushButton(self)
        ingresar_button.setText('Ingresar')
        ingresar_button.setFont(QFont('Times New Roman', 12))
        ingresar_button.setGeometry(600, 340, 200, 50)
        ingresar_button.clicked.connect(self.validar_inicio)

        volver_button = QPushButton(self)
        volver_button.setText('Volver al inicio')
        volver_button.setFont(QFont('Times New Roman', 12))
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
            QMessageBox.warning(self, "Error", "Faltan datos")
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def volver_inicio(self):
        self.usuario_input.clear()
        self.contra_input.clear()

        ventana_principal = self.window()
        if isinstance(ventana_principal, VentanaP):
            ventana_principal.mostrar_inicio()
        
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
        self.titulo_label.setText("Eliga sus asientos")
        self.titulo_label.setFont(QFont('Times New Roman', 30))
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titulo_label.setGeometry(400, 20, 650, 50)

        self.info_label = QLabel(self)
        self.info_label.setText("")
        self.info_label.setFont(QFont('Times New Roman', 22))
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setGeometry(400, 80, 650, 30)

        disponible_label = QLabel(self)
        disponible_label.setText(" _ = Disponible")
        disponible_label.setFont(QFont('Courier New', 14))
        disponible_label.setGeometry(1050, 280, 200, 30)

        ocupado_label = QLabel(self)
        ocupado_label.setText(" x = Ocupado")
        ocupado_label.setFont(QFont('Courier New', 14))
        ocupado_label.setGeometry(1050, 360, 200, 30)

        seleccionado_label = QLabel(self)
        seleccionado_label.setText(" o = Seleccionado")
        seleccionado_label.setFont(QFont('Courier New', 14))
        seleccionado_label.setGeometry(1050, 320, 200, 30)

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
        self.total_label.setFont(QFont('Times New Roman', 18))
        self.total_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.total_label.setGeometry(550, 610, 350, 40)

        volver_button = QPushButton(self)
        volver_button.setText("Volver a las funciones")
        volver_button.setFont(QFont('Times New Roman', 12))
        volver_button.setGeometry(20, 20, 200, 50)
        volver_button.clicked.connect(self.volver_funciones)
        
        confirmar_button = QPushButton(self)
        confirmar_button.setText("Confirmar Compra")
        confirmar_button.setFont(QFont('Times New Roman', 12))
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
            QMessageBox.warning(self, "Asiento Ocupado", "Este asiento esta ocupado. Porfavor eliga otro")
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

class ResumenVista(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.inicializar()

    def inicializar(self):
        titulo_label = QLabel(self)
        titulo_label.setText("Boletos comprados")
        titulo_label.setFont(QFont('Times New Roman', 35))
        titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_label.setGeometry(400, 30, 650, 60)

        self.resumen_text = QTextEdit(self) 
        self.resumen_text.setReadOnly(True)
        self.resumen_text.setFont(QFont('Times New Roman', 14))
        self.resumen_text.setGeometry(300, 120, 850, 450)

        volver_button = QPushButton(self)
        volver_button.setText("Volver al inicio")
        volver_button.setFont(QFont('Times New Roman', 12))
        volver_button.setGeometry(750, 600, 300, 50)
        volver_button.clicked.connect(self.volver_inicio)
    
    def mostrar_resumen(self, venta, sala):
        filas = ['A', 'B', 'C', 'D', 'E']
        resumen = "ღ"*124+"\n\n"
        resumen+= "Resumen\n"
        resumen+= f"    Sala: {sala.Numero}\n"
        resumen+= f"    Pelicula: {venta.Funcion.Pelicula}\n"
        resumen+= f"    Horario: {venta.Funcion.Horario}\n"
        resumen+= f"    Cantidad de entradas: {len(venta.asientos)}\n"
        resumen+= f"    Precio por entrada: $3000\n"
        resumen+= f"    Asientos comprados: "
        for asiento in venta.asientos:
            resumen += f" {filas[asiento.Fila]}{asiento.Columna+1}\n\n"
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
        titulo_label.setFont(QFont('Times New Roman', 35))
        titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_label.setGeometry(400, 50, 650, 60)

        subtitulo_label = QLabel(self)
        subtitulo_label.setText("Eliga el resumen que quiera ver: ")
        subtitulo_label.setFont(QFont('Times New Roman', 16))
        subtitulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitulo_label.setGeometry(400, 130, 650, 40)

        sala_button = QPushButton(self)
        sala_button.setText("Resumen de Ventas por Sala")
        sala_button.setFont(QFont('Times New Roman', 14))
        sala_button.setGeometry(525, 210, 400, 60)
        sala_button.clicked.connect(lambda: self.ver_reporte('sala'))

        funcion_button = QPushButton(self)
        funcion_button.setText("Resumen de Ventas por Función")
        funcion_button.setFont(QFont('Times New Roman', 14))
        funcion_button.setGeometry(525, 210 + 80, 400, 60)
        funcion_button.clicked.connect(lambda: self.ver_reporte('funcion'))

        horario_button = QPushButton(self)
        horario_button.setText("Resumen de Ventas por Horario")
        horario_button.setFont(QFont('Times New Roman', 14))
        horario_button.setGeometry(525, 210 + 80*2, 400, 60)
        horario_button.clicked.connect(lambda: self.ver_reporte('horario'))

        general_button = QPushButton(self)
        general_button.setText("Resumen General del Dia")
        general_button.setFont(QFont('Times New Roman', 14))
        general_button.setGeometry(525, 210 + 80*3, 400, 60)
        general_button.clicked.connect(lambda: self.ver_reporte('general'))

        cerrar_button = QPushButton(self)
        cerrar_button.setText("Cerrar Sesion")
        cerrar_button.setFont(QFont('Times New Roman', 12))
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

class ReporteVista(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.main_objeto = None
        self.salas = None
        self.inicializar()

    def inicializar(self):
        self.titulo_label = QLabel(self)
        self.titulo_label.setText("Resumenes de Ventas")
        self.titulo_label.setFont(QFont('Times New Roman', 30))
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_label.setGeometry(400, 30, 650, 60)

        self.reporte_text = QTextEdit(self)
        self.reporte_text.setReadOnly(True)
        self.reporte_text.setFont(QFont('Courier New', 11))
        self.reporte_text.setGeometry(200, 110, 1050, 530)

        volver_button = QPushButton(self)
        volver_button.setText("Volver al Menú de Administración")
        volver_button.setFont(QFont('Times New Roman', 12))
        volver_button.setGeometry(20, 20, 300, 50)
        volver_button.clicked.connect(self.volver_menu_admin)

    def set_datos(self, main_objeto, salas):
        self.main_objeto = main_objeto
        self.salas = salas

    def generar_reporte(self, tipo_reporte):
        if tipo_reporte == 'sala':
            self.titulo_label.setText("Resumen de Ventas por Sala")
            reporte = self.reporte_por_sala()
        elif tipo_reporte == 'funcion':
            self.titulo_label.setText("Resumen de Ventas por Función")
            reporte = self.reporte_por_funcion()
        elif tipo_reporte == 'horario':
            self.titulo_label.setText("Resumen de Ventas por Horario")
            reporte = self.reporte_por_horario()
        else:  
            self.titulo_label.setText("Resumen General del Día")
            reporte = self.reporte_general()
        
        self.reporte_text.setPlainText(reporte)

    def reporte_por_sala(self):
        reporte = "="*80+"\n"
        reporte += "     Resumen de venta por sala\n"
        reporte += "="*80+"\n\n"
        
        for sala in self.salas:
            reporte += f"{'ღ'*80}\n\n"
            reporte += f"  Sala {sala.Numero}\n"
            #reporte += f"{'─' * 80}\n"
            
            total_sala = 0
            entradas_sala = 0
            
            for funcion in sala.Funciones:
                if funcion:
                    entradas_vendidas = funcion.EntradasVendidas
                    total_funcion = entradas_vendidas * 3000
                    total_sala += total_funcion
                    entradas_sala += entradas_vendidas
                    reporte += f"       {funcion.Pelicula} ({funcion.Horario})\n"
                    reporte += f"           Entradas vendidas: {entradas_vendidas}\n"
                    reporte += f"           Total: ${total_funcion:,}\n\n"
            reporte += f"{'ღ'*80}\n\n"
            reporte += f"Total sala {sala.Numero}:\n"
            reporte += f"Entradas vendidas: {entradas_sala}\n"
            reporte += f"Total: ${total_sala:,}\n\n"
            reporte += f"{'ღ' * 76}\n\n"
        return reporte

    def reporte_por_funcion(self):
        reporte = "="*80+"\n"
        reporte += "  Resumen de venta por funcion\n"
        reporte += "="*80+"\n\n"
        total_general = 0
        
        for sala in self.salas:
            for funcion in sala.Funciones:
                if funcion:
                    entradas_vendidas = funcion.EntradasVendidas
                    total_funcion = entradas_vendidas * 3000
                    total_general += total_funcion
                    reporte += f"{'ღ'*80}\n\n"
                    reporte += f" {funcion.Pelicula}\n"
                    #reporte += f"{'ღ'*80}\n"
                    reporte += f"   Sala: {sala.Numero}\n"
                    reporte += f"   Horario: {funcion.Horario}\n"
                    reporte += f"   Entradas vendidas: {entradas_vendidas}\n"
                    reporte += f"   Total: ${total_funcion:,}\n\n"
        reporte += f"{'ღ'*80}\n\n"
        reporte += f"Total general: ${total_general:,}\n\n"
        reporte += f"{'ღ'*80}\n"
        return reporte

    def reporte_por_horario(self):
        reporte = "="*80+"\n"
        reporte += "  Resumen de venta por horario\n"
        reporte += "="*80+"\n\n"
        horarios = {}
        
        for sala in self.salas:
            for funcion in sala.Funciones:
                if funcion:
                    horario = funcion.Horario
                    if horario not in horarios:
                        horarios[horario] = {'entradas': 0, 'total': 0, 'funciones': []}
                    entradas_vendidas = funcion.EntradasVendidas
                    total_funcion = entradas_vendidas * 3000
                    horarios[horario]['entradas'] += entradas_vendidas
                    horarios[horario]['total'] += total_funcion
                    horarios[horario]['funciones'].append({
                        'sala': sala.Numero,
                        'pelicula': funcion.Pelicula,
                        'entradas': entradas_vendidas,
                        'total': total_funcion
                    })
        total_general = 0
        
        for horario, datos in horarios.items():
            reporte += f"{'ღ' * 80}\n\n"
            reporte += f" {horario.upper()}\n"
            #reporte += f"{'ღ' * 80}\n"
            
            for func in datos['funciones']:
                reporte += f"   Sala {func['sala']} - {func['pelicula']}\n"
                reporte += f"       Entradas: {func['entradas']} | Total: ${func['total']:,}\n\n"
            reporte += f"Total {horario}:\n"
            reporte += f"   Entradas vendidas: {datos['entradas']}\n"
            reporte += f"   Total: ${datos['total']:,}\n\n"
            total_general += datos['total']
        reporte += f"{'ღ'*80}\n\n"
        reporte += f"Total general: ${total_general:,}\n\n"
        reporte += f"{'ღ'*80}\n"
        return reporte

    def reporte_general(self):
        reporte = "="*80+"\n"
        reporte += "  Resumen general del dia\n"
        reporte += "="*80+"\n\n"
        total_entradas = 0
        total_recaudacion = 0
        reporte += "  Detalle por sala:\n"
        reporte += f"{'ღ' * 80}\n\n"
        
        for sala in self.salas:
            total_sala = 0
            entradas_sala = 0
            
            for funcion in sala.Funciones:
                if funcion:
                    entradas_vendidas = funcion.EntradasVendidas
                    total_funcion = entradas_vendidas * 3000
                    total_sala += total_funcion
                    entradas_sala += entradas_vendidas
            total_entradas += entradas_sala
            total_recaudacion += total_sala
            reporte += f"Sala {sala.Numero}:\n"
            reporte += f"Entradas: {entradas_sala} | Total: ${total_sala:,}\n\n"
        reporte += f"{'ღ'*80}\n\n"
        reporte += "Estadisticas generales:\n"
        #reporte += f"{'ღ'*80}\n\n"
        reporte += f"   Total de entradas vendidas: {total_entradas}\n"
        reporte += f"   Precio por entrada: $3,000\n"
        reporte += f"   Capacidad total del cine: 75 asientos (3 salas)\n\n"
        reporte += f"  {'ღ'*80}\n\n"

        if total_entradas > 0:
            ocupacion = (total_entradas / 75) * 100
            reporte += f"Ocupación del día: {ocupacion:.1f}%\n"
        reporte += f"Total del dia: ${total_recaudacion:,}\n\n"
        reporte += f"  {'ღ'*80}\n"
        return reporte

    def volver_menu_admin(self):
        ventana_principal = self.window()
        if hasattr(ventana_principal, 'mostrar_menu_admin'):
            ventana_principal.mostrar_menu_admin()

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
    