'''
función 5, números pares
'''

def funcion_numeros():
    lista_numeros = [21, 7, 26, 16, 100, 54, 1, 43]
    x = [y for y in lista_numeros if y % 2 == 0]
    print("Estos son los números pares que se encontraron: ", x)

funcion_numeros()
