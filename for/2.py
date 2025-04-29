#leer numero ngresado por el usuario
#mostar la letra a por cada numero del 1 al numero
#a
#aa
#aaa

def mostrarletra(numero):
    for i in range(1,numero+1):
        print(f'a'*i)

def main():
    num= int(input('Ingrese un numero: '))
    mostrarletra(num)

main()