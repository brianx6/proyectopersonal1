def puntuacion(clase):
    return sum(clase) / len(clase)

clase = [8, 6, 9]
media = puntuacion(clase)
print(f"la puntuacion de esta clase es: {media}")

clase = [8, 6, 7]
media = puntuacion(clase)
print(f"la puntuacion de esta clase es: {media}")