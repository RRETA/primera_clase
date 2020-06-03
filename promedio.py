numero_materias = 3
nombre=input("Nombre de Alumno:")
calificaciones = []
for i in range(1,numero_materias + 1):    calificaciones.append(int(input("Calificacion {0}: ".format(i))))
suma= 0
for calificacion in calificaciones:    suma = suma + calificacion 
promedio = suma / len(calificaciones)
if promedio >= 7:    print("Felicidades {0} pasaste de año con un promedio de: {1}".format(nombre,promedio))
else:    print("Reprobaste de año {0} con un promedio de: {1}".format(nombre,promedio))
