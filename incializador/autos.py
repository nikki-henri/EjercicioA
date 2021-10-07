'''
Inicializador, Autos
'''

class Auto:
    volante = "True"
    asientos = 5
    puertas= 5
    llantas = 4
    nombre = "a"
    color: "b"
    bolsas_de_aire = "True"
    

    def __init__(self,n,c):
        self.nombre = n
        self.color = c
        

Audi = Auto ("A1","Blanco")
Jeep = Auto ("Wrangler","Azul")
Toyota = Auto ("Highlander","Gris")

print(Audi.nombre, Audi.color)
print(Jeep.nombre, Jeep.color)
print(Toyota.nombre, Toyota.color)
