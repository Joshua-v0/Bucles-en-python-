#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for x in range(1, 11):
    for j in range(1, 11):
        print(x * j, end = "\t")
    print("") 