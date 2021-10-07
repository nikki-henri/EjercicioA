'''
Inicializador, Bebidas
'''

class Bebida:
    líquido = "True"
    gas = "a"
    sabor = "b"
    tamaño = "c"
    temperatura = "d"
    

    def __init__(self,g,s,a,b):
        self.gas = g
        self.sabor = s
        self.tamaño = a
        self.temperatura = b

refresco = Bebida ("Con gas,","sabor Sprite.","Grande,","frío")
té = Bebida ("Sin gas,","sabor Durazno.","Chico,","caliente")
café = Bebida ("Sin gas,","sabor Mocha.","Mediano,","frío")

print(refresco.gas, refresco.sabor, refresco.tamaño, refresco.temperatura)
print(té.gas, té.sabor, té.tamaño, té.temperatura)
print(café.gas, café.sabor, café.tamaño, café.temperatura)
