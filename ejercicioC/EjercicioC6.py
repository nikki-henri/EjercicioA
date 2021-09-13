'''
funcion 6
'''

oración = input ("Escribe para contar las vocales")
string = oración.lower ()
print (string)
count = 0
vocales = ["a","e","i","o","u"]
for char in string:
    if char in vocales:
        count = count+1

print ("Numero total de vocales:", count)
