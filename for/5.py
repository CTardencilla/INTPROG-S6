def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 13):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


num = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)
