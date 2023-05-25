#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

n = int(input("Ingrese la altura del numero: "))
for x in range(1 , n+1, 2):
    for i in range(x, 0, -2):
        print(x, end = "")
    print("") 

    