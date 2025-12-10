import sys
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QStackedWidget, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


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
        volver_button.setFont(QFont('Tektur', 12))
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
        
        reporte_html = reporte.replace('▬', '<span style="color: #FF5722;">▬</span>')
        
        reporte_html = f'<pre style="font-family: Courier New; font-size: 11pt;">{reporte_html}</pre>'

        self.reporte_text.setHtml(reporte_html)

    def reporte_por_sala(self):

        reporte = "\n"
        reporte += f"{'▬'*150}\n"
        reporte += "                        _____                                           _____       _       \n"
        reporte += "                       |  __ \                                     _   / ____|     | |      \n"
        reporte += "                       | |__) |___  ___ _   _ _ __ ___   ___ _ __ (_) | (___   __ _| | __ _ \n"
        reporte += "                       |  _  // _ \/ __| | | | '_ ` _ \ / _ \ '_ \     \___ \ / _` | |/ _` |\n"
        reporte += "                       | | \ \  __/\__ \ |_| | | | | | |  __/ | | |_   ____) | (_| | | (_| |\n"
        reporte += "                       |_|  \_\___||___/\__,_|_| |_| |_|\___|_| |_(_) |_____/ \__,_|_|\__,_|\n"
    #    reporte = "—"*150+"\n"
    #    reporte += "    ╱ Resumen de venta por sala ╱\n"
    #    reporte += "—"*150+"\n\n"
        
        for sala in self.salas:
            reporte += f"{'▬'*150}\n\n"
            reporte += f"  Sala {sala.Numero}\n"
            
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
            reporte += f"{'▬'*150}\n\n"
            reporte += f"Total sala {sala.Numero}:\n"
            reporte += f"Entradas vendidas: {entradas_sala}\n"
            reporte += f"Total: ${total_sala:,}\n\n"
            reporte += f"{'▬' *150}\n\n"
        return reporte

    def reporte_por_funcion(self):
        reporte = "\n"
        reporte += f"{'▬'*150}\n"
        reporte += "               _____                                          ______                _   __        \n"
        reporte += "              |  __ \                                     _  |  ____|              (_) /_/        \n"
        reporte += "              | |__) |___  ___ _   _ _ __ ___   ___ _ __ (_) | |__ _   _ _ __   ___ _  ___  _ __  \n"
        reporte += "              |  _  // _ \/ __| | | | '_ ` _ \ / _ \ '_ \    |  __| | | | '_ \ / __| |/ _ \| '_ \ \n"
        reporte += "              | | \ \  __/\__ \ |_| | | | | | |  __/ | | |_  | |  | |_| | | | | (__| | (_) | | | |\n"
        reporte += "              |_|  \_\___||___/\__,_|_| |_| |_|\___|_| |_(_) |_|   \__,_|_| |_|\___|_|\___/|_| |_|\n"
    #    reporte = "="*150+"\n"
    #    reporte += "  Resumen de venta por funcion\n"
    #    reporte += "="*150+"\n\n"
        total_general = 0
        
        for sala in self.salas:
            for funcion in sala.Funciones:
                if funcion:
                    entradas_vendidas = funcion.EntradasVendidas
                    total_funcion = entradas_vendidas * 3000
                    total_general += total_funcion
                    reporte += f"{'▬'*150}\n\n"
                    reporte += f" {funcion.Pelicula}\n"
                    reporte += f"   Sala: {sala.Numero}\n"
                    reporte += f"   Horario: {funcion.Horario}\n"
                    reporte += f"   Entradas vendidas: {entradas_vendidas}\n"
                    reporte += f"   Total: ${total_funcion:,}\n\n"
        reporte += f"{'▬'*150}\n\n"
        reporte += f"Total general: ${total_general:,}\n\n"
        reporte += f"{'▬'*150}\n"
        return reporte

    def reporte_por_horario(self):
    
        reporte = "\n"
        reporte += f"{'▬'*150}\n"
        reporte += "                _____                                          _    _                      _       \n"
        reporte += "               |  __ \                                     _  | |  | |                    (_)      \n"
        reporte += "               | |__) |___  ___ _   _ _ __ ___   ___ _ __ (_) | |__| | ___  _ __ __ _ _ __ _  ___  \n"
        reporte += "               |  _  // _ \/ __| | | | '_ ` _ \ / _ \ '_ \    |  __  |/ _ \| '__/ _` | '__| |/ _ \ \n"
        reporte += "               | | \ \  __/\__ \ |_| | | | | | |  __/ | | |_  | |  | | (_) | | | (_| | |  | | (_) |\n"
        reporte += "               |_|  \_\___||___/\__,_|_| |_| |_|\___|_| |_(_) |_|  |_|\___/|_|  \__,_|_|  |_|\___/ \n"
    
    #    reporte = "="*150+"\n"
    #    reporte += "  Resumen de venta por horario\n"
    #    reporte += "="*150+"\n\n"
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
            reporte += f"{'▬' * 150}\n\n"
            reporte += f" {horario.upper()}\n"
            
            for func in datos['funciones']:
                reporte += f"   Sala {func['sala']} - {func['pelicula']}\n"
                reporte += f"       Entradas: {func['entradas']} | Total: ${func['total']:,}\n\n"
            reporte += f"Total {horario}:\n"
            reporte += f"   Entradas vendidas: {datos['entradas']}\n"
            reporte += f"   Total: ${datos['total']:,}\n\n"
            total_general += datos['total']
        reporte += f"{'▬'*150}\n\n"
        reporte += f"Total general: ${total_general:,}\n\n"
        reporte += f"{'▬'*150}\n"
        return reporte

    def reporte_general(self):
    
        reporte = "\n"
        reporte += f"{'▬'*150}\n"
        reporte += "                     _____                                          _____  __      \n"
        reporte += "                    |  __ \                                     _  |  __ \/_/      \n"
        reporte += "                    | |__) |___  ___ _   _ _ __ ___   ___ _ __ (_) | |  | |_  __ _ \n"
        reporte += "                    |  _  // _ \/ __| | | | '_ ` _ \ / _ \ '_ \    | |  | | |/ _` |\n"
        reporte += "                    | | \ \  __/\__ \ |_| | | | | | |  __/ | | |_  | |__| | | (_| |\n"
        reporte += "                    |_|  \_\___||___/\__,_|_| |_| |_|\___|_| |_(_) |_____/|_|\__,_|\n"
    
    #    reporte = "="*150+"\n"
    #    reporte += "  Resumen general del dia\n"
    #    reporte += "="*150+"\n\n"


        total_entradas = 0
        total_recaudacion = 0
    #    reporte += "  Detalle por sala:\n"
        reporte += f"{'▬' * 150}\n\n"
        
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
        reporte += f"{'▬'*150}\n\n"
        reporte += "Estadisticas generales:\n"
        reporte += f"   Total de entradas vendidas: {total_entradas}\n"
        reporte += f"   Precio por entrada: $3,000\n"
        reporte += f"   Capacidad total del cine: 75 asientos (3 salas)\n\n"
        reporte += f"  {'▬'*150}\n\n"

        if total_entradas > 0:
            ocupacion = (total_entradas / 75) * 100
            reporte += f"Ocupación del día: {ocupacion:.1f}%\n"
        reporte += f"Total del dia: ${total_recaudacion:,}\n\n"
        reporte += f"  {'▬'*150}\n"
        return reporte

    def volver_menu_admin(self):
        ventana_principal = self.window()
        if hasattr(ventana_principal, 'mostrar_menu_admin'):
            ventana_principal.mostrar_menu_admin()