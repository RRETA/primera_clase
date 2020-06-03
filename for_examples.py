
#Reto 1
print("Reto 1")
for numeros in range(2,301,2): print(numeros)

#Reto 2
print("Reto 2")
tabla = 15
for numero in range(0,tabla + 1): print("1 X {0} = {1}".format(numero,numero * tabla))

#Reto 3
print("Reto 3")
resultado = 0
lista = []
for numero in range(51,101,2): 
    resultado = resultado + numero
    lista.append(resultado)
print(lista)
print("Suma = {0}".format(resultado))

#Reto 4
print("Reto 4")
suma = 0
lista = []
for numero in range(10,101,2):
    suma = suma + numero
    lista.append(suma)
print(lista)
print("Suma = {}".format(suma))
