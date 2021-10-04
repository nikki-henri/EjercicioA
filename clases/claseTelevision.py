'''
Clases, Televisión
'''

class Television:
    #propiedades
    control = 1
    cables = 5
    entradas = 4
    color: "Negro"

    #metodos
    def encender(self):
        print("encender")
    def apagar(self):
        print("apagar")
    def cambiar_canal(self):
        print("cambiar_canal")
    def subir_volumen(self):
        print("subir_volumen")
    def bajar_volumen(self):
        print("bajar_volumen")
    def mute(self):
        print("mute")

samsung = Television()
LG = Television()

LG.encender()
LG.subir_volumen()
LG.cambiar_canal()
LG.mute()
LG.apagar()
