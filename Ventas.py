class Venta:
    cantidad_boletos = 2
    def __init__(self, Total: int, Funcion):
        self.Total = 0
        self.Funcion = Funcion

    def Vender(self, ListaAsientos, Funcion, Main):
        self.Total = 0
        self.Funcion = None
        AsientosVendidos = []
        AsientosVendidos2 = []
        for j in range(len(ListaAsientos)):
            AsientosVendidos2.append(ListaAsientos)
        for i in range (self.cantidad_boletos):
            for asiento in ListaAsientos:
                if asiento.Disponible == 1:
                    print("Asiento ya ocupado")
                else:
                    asiento.Disponible = 1
                    self.Total = self.Total + 3000
                    new_Venta = Venta(self.Total, self.Funcion)
                    AsientosVendidos.append(new_Venta)
                    print(f"Venta: {new_Venta.Total}, {new_Venta.Funcion}")

        self.Funcion = Funcion.Pelicula
        
        return AsientosVendidos, AsientosVendidos2
    def __str__(self):
        return f"Venta: {self.Funcion} y {self.Total}"
#    def GenerarResumen(self):
#        return str