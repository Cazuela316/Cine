class Asientos:

    def __init__(self, Fila:int, Columna:int, Disponible:bool, Sala):
        self.Fila = Fila
        self.Columna = Columna
        self.Disponible = Disponible
        self.Sala = Sala
    
    def __str__(self):
        return f"{self.Columna} y {self.Fila}"

#   def Asientos(self):
#       Muestra todos los asientos

#   def MarcarOcupado(self):
#       return void