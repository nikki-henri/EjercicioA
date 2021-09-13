'''
función 2, lista números ordenados
'''
lista = []
for x in range (5):
    valor = int (input ("Escribe un número:"))
    lista.append (valor)
#ordenar de menor a mayor
for k in range(4):
    for x in range(4):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux

print ("Lista ordenada")
print (lista)
