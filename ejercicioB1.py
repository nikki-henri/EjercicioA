'''
Ejercicio Calcular Masa Corporal
'''
peso = 61
altura = 1.65

def calcular_masacorporal():
    imc = peso /(altura**2)
    print (imc)

    if imc <= 18.5:
        print ("Peso Bajo")

    if imc >= 18.5 and imc <= 25.4:
        print ("Adecuado")
      
    if imc >= 25.5 and imc <= 29.9:
        print ("Sobrepeso")

    if imc >= 30:
        print ("Obesidad")

calcular_masacorporal()
