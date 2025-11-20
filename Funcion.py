class Funcion:
    def __init__(self, Horario:str, Pelicula:str, EntradasVendidas:int):
        self.Horario = Horario
        self.Pelicula = Pelicula
        self.EntradasVendidas = EntradasVendidas
        self.Asientos = [[0 for j in range(5)] for i in range(5)]
    
    filas = 5
    columnas = 5



#    def VerificarDisponible(self):
#        return bool
   
#    def ReservarAsiento(self):    
#        return bool
    
#    def VisualizarAsientos(self):
#        Muestra los asientos

#    def GetTotalRecaudado(self):
#        Return int


    #for i in range(columnas):
    #    for j in range(filas):
    #        Asientos[i][j]= i+j
    #for i in range(columnas):
    #    print("\n")
    #    for j in range(filas):
    #        print(Asientos[i][j], end=' ')

    
