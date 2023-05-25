#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

num = int(input("Ingrese la altua del triangulo:"))
for x in range(num):
    for j in range(x + 1):  
        print("x", end = "")
    print("") 
        