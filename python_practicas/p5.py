#pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

inversion = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interes anual: "))
num = int(input("Ingrese la cantidad de de años. ")) 
for i in range(num):
    interes *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(interes, 2)))    




      