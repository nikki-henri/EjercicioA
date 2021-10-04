'''
Clases, Auto
'''

class Auto:
    #propiedades
    volante = 1
    puertas= 5
    llantas = 4
    rapido = "True"
    color: "Blanco"
    año: 2020

    #metodos
    def encender(self):
        print("encender")
    def apagar(self):
        print("apagar")
    def acelerar(self):
        print("acelerar")
    def estacionarse(self):
        print("estacionarse")
    def frenar(self):
        print("frenar")
    def reversa(self):
        print("reversa")

toyota = Auto()
audi = Auto()

toyota.encender()
toyota.acelerar()
toyota.frenar()
toyota.estacionarse()
toyota.apagar()
