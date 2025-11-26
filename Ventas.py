class Venta:
    import Asientos
    cantidad_boletos = 2
    def __init__(self, Total: int, Funcion,asientos:Asientos):
        self.asientos = []
        self.Total = 0
        self.Funcion = Funcion

    def Vender(self, ListaAsientos, Funcion, Main):
        self.Total = 0
        self.Funcion = None
        AsientosVendidos = []
        for i in range (self.cantidad_boletos):
            for asiento in ListaAsientos:
                if asiento.Disponible == 1:
                    print("Asiento ya ocupado")
                else:
                    self.asientos.append(ListaAsientos)
                    asiento.Disponible = 1
                    self.Total = self.Total + 3000
                    new_Venta = Venta(self.Total, self.Funcion, None)
                    AsientosVendidos.append(new_Venta)
                    print(f"Venta: {new_Venta.Total}, {new_Venta.Funcion}")

        self.Funcion = Funcion.Pelicula
        
        return AsientosVendidos, self.asientos
    def __str__(self):
        return f"Venta: {self.Funcion} - ${self.Total} - {len(self.asientos)} asientos"
#    def GenerarResumen(self):
#        return str