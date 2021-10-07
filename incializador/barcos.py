'''
Inicializador, Barcos
'''

class Barco:
    timón = "True"
    color = "a"
    capacidad = "b"
    motor= "c"
    transporte = "True"
    vía = "Agua"    

    def __init__(self,a,b,c):
        self.color = a
        self.capacidad = b
        self.motor = c

Bote = Barco ("Marron,","6,","Sin motor")
Pontón  = Barco ("Verde oscuro,","13,","Con motor")
Wakeboard = Barco ("Rojo,","10,","Con motor")

print(Bote.color, Bote.capacidad, Bote.motor)
print(Pontón.color, Pontón.capacidad, Pontón.motor)
print(Wakeboard.color, Wakeboard.capacidad, Wakeboard.motor)
