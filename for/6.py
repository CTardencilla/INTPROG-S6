suma = 0
contador = 0

while True:
    calificacion = float(input("Ingresa una calificación (o -1 para terminar): "))
    
    if calificacion == -1:
        break
    
    suma += calificacion
    contador += 1

if contador > 0:
    promedio = suma / contador
    print("El promedio de las calificaciones es:", promedio)
else:
    print("No se ingresaron calificaciones válidas.")
