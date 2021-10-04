'''
Clases, Animal
'''

class Animal:
    #propiedades
    cabeza = 1
    ojos= 2
    patas = 4
    rapido = "True"
    color: "Naranja"

    #metodos
    def caminar(self):
        print("caminar")
    def correr(self):
        print("correr")
    def cazar(self):
        print("cazar")
    def brincar(self):
        print("brincar")
    def dormir(self):
        print("dormir")
    def comer(self):
        print("comer")

jaguar = Animal()
oso_perezoso = Animal()

jaguar.comer()
jaguar.cazar()
jaguar.brincar()
jaguar.correr()
