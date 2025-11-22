import Funcion,Venta,Sala,Asientos

class Main:
    def __init__(self, Nombre:str, TotalVentasDia:int, ListaDeVentas:Venta):
        self.Nombre = Nombre
        self.Salas[3]
        self.TotalVentasDia = TotalVentasDia
        self.ListaDeVentas[None] * 75


if __name__=="__main__":
    F1=Funcion.Funcion("Matiné", "Peli1", 0)
    F2=Funcion.Funcion("Vermut", "Peli2", 0)
    F3=Funcion.Funcion("Vespertina", "Peli3", 0)

    F4=Funcion.Funcion("Matiné", "Peli4", 0)
    F5=Funcion.Funcion("Vermut", "Peli5", 0)
    F6=Funcion.Funcion("Vespertina", "Peli6", 0)

    F7=Funcion.Funcion("Matiné", "Peli7", 0)
    F8=Funcion.Funcion("Vermut", "Peli8", 0)
    F9=Funcion.Funcion("Vespertina", "Peli9", 0)

    S1=Sala.Sala(1)
    S1.Funciones[0]=F1
    S1.Funciones[1]=F2
    S1.Funciones[2]=F3
    S2=Sala.Sala(2)
    S2.Funciones[0]=F4
    S2.Funciones[1]=F5
    S2.Funciones[2]=F6
    S3=Sala.Sala(3)
    S3.Funciones[0]=F7
    S3.Funciones[1]=F8
    S3.Funciones[2]=F9

    A1=Asientos(2,"A",0, S1) #Inicializa un asiento libre en la posicion del arreglo [0][2], que esta libre y pertenece a la sala 1
    #Aunque estos asientos se generan solo cuando uno se vende

    V1=Venta(9000, F4)
    V1.AsientosVendidos[1]=A1 #Y asi para A2 y A3 pues fueron vendidos 3 asientos

    Cine=Main("Cine-1",100000)