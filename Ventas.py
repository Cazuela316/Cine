class Venta:
    def __init__(self, Total: int, Funcion):
        self.Total = 0
        self.Funcion = Funcion

    def Vender(self, ListaAsientos, Funcion, Main):
        AsientosVendidos = []
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
        return AsientosVendidos

#    def GenerarResumen(self):
#        return str