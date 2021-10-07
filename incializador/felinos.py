'''
Inicializador, Felinos
'''

class Felino:
    Especie = "a"
    Color = "b"
    Reino = "Animalia"
    Filo = "Chordata"
    Clase = "Mammalia"
    Familia = "Felidae"
    patas = 4

    def __init__(self,e,c):
        self.especie = e
        self.color = c

felino1 = Felino ("Pantera,","negro")
felino2 = Felino ("León,","marron-naranja")
felino3 = Felino ("Lince boreal,","marrón rojizo")

print(felino1.especie, felino1.color)
print(felino2.especie, felino2.color)
print(felino3.especie, felino3.color)
