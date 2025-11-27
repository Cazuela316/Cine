import sys
import Funcion,Ventas,Sala,Asientos
from PyQt6.QtWidgets import QApplication
import Funcion as F
import Asientos as A
import Sala as S
import Ventas as V
from Ventana import VentanaP

class Main:
    def __init__(self, Nombre:str, TotalVentasDia:int, ListaDeVentas:V, Salas:S,Cont:int, AsientosVendidos22, Connt:int):
        self.Nombre = Nombre
        self.Salas = [3]
        self.TotalVentasDia = TotalVentasDia
        self.ListaDeVentas = [None] * 75
        self.Cont = 0
        self.AsientosVendidos22 = [None] * 75
        self.Connt = 0

    def Holi (self, Venta: V.Venta):
        self.ListaDeVentas[self.Cont]=Venta
        self.Cont=self.Cont+1

    def Hole (self, AsientosVendidos22: V.Venta):
        self.AsientosVendidos22[self.Connt]=AsientosVendidos22
        self.Connt=self.Connt+1


def main():
    F1=F.Funcion("Matiné", "Peli1", 0)
    F2=F.Funcion("Vermut", "Peli2", 0)
    F3=F.Funcion("Vespertina", "Peli3", 0)

    F4=F.Funcion("Matiné", "Peli4", 0)
    F5=F.Funcion("Vermut", "Peli5", 0)
    F6=F.Funcion("Vespertina", "Peli6", 0)

    F7=F.Funcion("Matiné", "Peli7", 0)
    F8=F.Funcion("Vermut", "Peli8", 0)
    F9=F.Funcion("Vespertina", "Peli9", 0)

    S1=S.Sala(1, None)
    S1.Funciones[0]=F1
    S1.Funciones[1]=F2
    S1.Funciones[2]=F3
    S2=S.Sala(2, None)
    S2.Funciones[0]=F4
    S2.Funciones[1]=F5
    S2.Funciones[2]=F6
    S3=S.Sala(3, None)
    S3.Funciones[0]=F7
    S3.Funciones[1]=F8
    S3.Funciones[2]=F9

    Cine=Main("Cine-1",100000, None, None, 0, None, 0)
    Cine.Salas = [S1, S2, S3]
    
    app = QApplication(sys.argv)
    ventana = VentanaP(Cine, [S1, S2, S3])
    ventana.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()

    #A1=A.Asientos(2,0,0, S1) #Inicializa un asiento libre en la posicion del arreglo [0][2], que esta libre y pertenece a la sala 1
    #Aunque estos asientos se generan solo cuando uno se vende

    #A2=A.Asientos(3,0,0, S1)
    #A3=A.Asientos(4,0,0, S1)
    #A4=A.Asientos(5,0,0, S1)
    #V2=V.Venta(None,None,None)

    #Cine=Main("Cine-1",100000, None, None, 0, None, 0)

    #print(V2.Total) 
    
    #V2.Vender([A1,A2], F1, Cine)
    #Cine.Holi(V2)
    #V2.Vender([A3,A4], F1, Cine)
    #Cine.Holi(V2)
    #Total_sala=S1.resumen_sala(Cine.ListaDeVentas)
    #print(Total_sala)

    #for j in range(75):
    #    print(Cine.ListaDeVentas[j], end=' ')


    #print("\n\n\n")

    #for j in range(75):
    #    print(Cine.ListaDeVentas[j], end=' ')

    #print(A1.Disponible, "   ", V2.Total)
