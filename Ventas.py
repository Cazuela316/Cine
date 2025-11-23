import Asientos
class Venta:
    def __init__(self, Total:int, Funcion):
        self.Total = 0
        self.Funcion = Funcion

    def Vender(self, Asientos, Funcion,Main):
        
        AsientosVendidos = []

        if (Asientos.Disponible==1):
            print("NOOOOOOOO")
        else:
            Asientos.Disponible=1
            self.Total=self.Total+3000
            self.Funcion=Funcion.Pelicula

        for Funcion, Total in Asientos,Funcion:
            new_Venta=Venta(self.Total, self.Funcion)
            AsientosVendidos.append(new_Venta)
            print(f"Holiiiiii: {new_Venta.Total}, {new_Venta.Funcion}")
        
        return AsientosVendidos

#    def GenerarResumen(self):
#        return str