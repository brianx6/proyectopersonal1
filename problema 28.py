import math

numero = int(input("digite un numero: "))

while numero<0:
    print("error. deberia de ser un numero positivo")
    numero = int(input("digite un numero: "))

print(f"\nsu raiz cuadrada es: {(math.sqrt(numero)):.2f}")
