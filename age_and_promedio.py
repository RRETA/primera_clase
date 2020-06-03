edad = int(input("Escribe tu edad: "))
promedio = float(input("Escribe tu promedio: "))
if edad > 0:
    if edad <6:   print("Kinder, sigue disfutando")
    elif edad >= 6 and edad < 12:    
        if promedio >= 9.5:    print("Primaria, promedio aceptable")
        else:    print("Primaria, promedio inaceptable")
    elif edad >= 12 and edad < 15:
        if promedio >= 9:    print("Secundaria, promedio aceptable")
        else:    print("Secundaria, promedio inaceptable")  
        print("Secundaria")
    elif edad >=15 and edad < 18:    
        if promedio >= 8.5:    print("Bachillerato, promedio aceptable")
        else:    print("Bachillerato, promedio inaceptable")
    elif edad >=18 and edad <23:    
        if promedio >= 9:    print("Universida, promedio aceptable")
        else:    print("Universidad, promedio inaceptable")
    elif edad >=23 :    print("Tu ya no estudias")