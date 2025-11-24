import Funcion
class Sala:
    def __init__(self,Numero:int, Funciones:Funcion):
        self.Numero = Numero
        self.Funciones = [None] * 3

    def resumen_sala(self, lista_ventas):
        total = 0 
        for venta in lista_ventas:
            if venta is not None:
                total += venta.Total 
        return total

    #def resumen_sala(self,ListaDeVentas,Total_sala=0):
    #    if Sala == Main.S1:
    #        for i in range (74):
    #            ListaDeVentas[i]
    #            Total_sala=ListaDeVentas[i]+Total_sala
    #    return Total_sala
#   def Sala(self):
#       Muestra las tres funciones de una sala (?)

#   def GetFuncion(self):
#       return Funcion