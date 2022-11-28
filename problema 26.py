lista1 = [1,4,3,6,4,3,6,2,5]
lista2 = [6,4,3,7,2,4,6,3,5]

a = set(lista1)
b = set(lista2)

union = (a | b)

soloa = list(a - b)
solob = list(b - a)
interseccion = list(a & b)

print(f"numeros que aparecen en las dos listas {union}")
print(f"numeros que solo aparecen en a {soloa}")
print(f"numeros que solo aparecen en b {solob}")