import math

radio = float(input("radio:"))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"el area es: {area:.2f}")
print(f"la longitud de la circuferencia es: {longitud:.2f}")
# :.5f para reducir la cantidad de numeros que se generan