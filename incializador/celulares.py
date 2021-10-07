'''
Inicializador, Celulares
'''

class Celular:
    calculadora = "True"
    cámara = "a"
    cargador = "True"
    color = "b"
    compañía = "c"
    marca = "d"
    pantalla = 1
    reloj = "True"

    def __init__(self,a,b,c,m):
        self.cámara = a
        self.color = b
        self.compañía = c
        self.marca = m

Celular1 = Celular ("3,","Morado,","Apple,","iPhone 12")
Celular2 = Celular ("6,","Platino,","Huawei,","Mate 40 Pro")
Celular3 = Celular ("4,","Verde,","Samsung,","Galaxy Note20")

print(Celular1.cámara, Celular1.color, Celular1.compañía, Celular1.marca)
print(Celular2.cámara, Celular2.color, Celular2.compañía, Celular2.marca)
print(Celular3.cámara, Celular3.color, Celular3.compañía, Celular3.marca)
