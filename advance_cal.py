variable_1 =int(input("Primer Valor "))
variable_2 = int(input("Segundo Valor "))
operaciones = {"suma": variable_1 + variable_2, "resta": variable_1 -variable_2, "multiplicacion": variable_1 * variable_2, "division":variable_1/variable_2,
"division_exacta": variable_1 // variable_2, "elevar_al_cuadrado_1": variable_1 ** 2, "elevar_al_cuadrado_2": variable_2 ** 2, "elevar_al_cubo_1": variable_1 ** 3, 
"elevar_al_cubo_2": variable_2 ** 3,"modulo": variable_1 % variable_2}
for operacion in operaciones:
    print("El resultado de la operacion {0} es {1}".format(operacion.replace("_"," "),operaciones[operacion]))