import Funcion as F
import Asientos as A
import Sala as S
import Ventas as V

class Main:
    def __init__(self, Nombre:str, TotalVentasDia:int, ListaDeVentas:V, Salas:S,Cont:int):
        self.Nombre = Nombre
        self.Salas = [3]
        self.TotalVentasDia = TotalVentasDia
        self.ListaDeVentas = [None] * 75
        self.Cont = 0

    def Holi (self, Venta:V.Venta):
        self.ListaDeVentas[self.Cont]=V2
        self.Cont=self.Cont+1

def main():
    app = QApplication(sys.argv)
    ventana = VentanaP()
    ventana.show()
    sys.exit(app.exec())

if __name__=="__main__":
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

    A1=A.Asientos(2,0,0, S1) #Inicializa un asiento libre en la posicion del arreglo [0][2], que esta libre y pertenece a la sala 1
    #Aunque estos asientos se generan solo cuando uno se vende

    V2=V.Venta(None,None)

    Cine=Main("Cine-1",100000, None, None, 0)

    print(V2.Total) 
    
    V2.Vender([A1], F1, Cine)

    for j in range(75):
        print(Cine.ListaDeVentas[j], end=' ')

    Cine.Holi(V2)

    print("\n\n\n")

    for j in range(75):
        print(Cine.ListaDeVentas[j], end=' ')

    print(A1.Disponible, "   ", V2.Total)
