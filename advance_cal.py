variable_1 =int(input("Primer Valor "))
variable_2 = int(input("Segundo Valor "))
operaciones = ["suma","resta","multiplicacion","division","division exacta","Elevar al cuadrado","Elevar al cubo","Modulo"]

def ejecucion_operacion(var1,var2,operacion):
    
    #if operacion == "suma": result = var1 + var2
    #if operacion == "resta": result = var1 - var2
    #if operacion == "multiplicacion": result = var1 * var2
    #if operacion == "division": result = var1 / var2
    if operacion == "division exacta": result = var1 // var2
    if operacion == "Elevar al cuadrado": result = var1 ** 2
    if operacion == "Elevar al cubo": result = var1 ** 3
    if operacion == "Modulo": result = var1 % var2
    else: result = 0
    return result



for operacion in operaciones:
    resultado = ejecucion_operacion(variable_1,variable_2,operacion)
    print("El resultado de la operacion {0} es {1}".format(operacion,resultado))