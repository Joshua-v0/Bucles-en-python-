#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = int(input("Ingrese un numero entero positivo: "))
for x in range(0, num+1,):
    print(x, end = ",") 
    