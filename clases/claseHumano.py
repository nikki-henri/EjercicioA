'''
Clases, Humano
'''

class Humano:
    #propiedades
    cabeza = 1
    ojos= 2
    nariz = 1
    boca = 1
    orejas = 2
    brazos = 2
    piernas = 2
    cuerpo = "tez clara"

    #metodos
    def respirar(self):
        print("respirar")
    def caminar(self):
        print("caminar")
    def correr(self):
        print("correr")
    def agacharse(self):
        print("agacharse")
    def brincar(self):
        print("brincar")
    def dormir(self):
        print("dormir")
    def comer(self):
        print("comer")

hombre = Humano()
mujer = Humano()

mujer.respirar()
mujer.caminar()
mujer.agacharse()
mujer.brincar()
mujer.correr()
