variable_1 =int(input("Primer Valor"))
variable_2 = int(input("Segundo Valor"))
operaciones = ["suma","resta","multiplicacion","division"]

def ejecucion_opercion(var1,var2,operacion):
    if operacion == "suma": result = var1 + var2
    if operacion == "resta": result = var1 - var2
    if operacion == "multiplicacion": result = var1 * var2
    if operacion == "division": result = var1 / var2
    return result

#mensaje = "El resultado de la operacion "
#print()


for operacion in operaciones:
    resultado = ejecucion_opercion(variable_1,variable_2,operacion)
    print("El resultado de la operacion {0} es {1}".format(operacion,resultado))