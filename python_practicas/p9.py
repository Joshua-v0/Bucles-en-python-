#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

key = "password"
password = ""

while password != key:
    pas = input("Ingrese su contraseña: ")
    print("contraseña correcta")
    break
else:
    print("contraseña incorrecta") 
