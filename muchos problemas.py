print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
print("~  Tienda la esquina  ~")
print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

print()

nombres = []

clientes = int(input("cuantos clientes son? "))

for i in range(clientes):

    artinom = str(input("\nnombre del articulo: "))
    nombres.append(artinom)
    precio = int(input("cual es el precio del articulo: "))
    artis = int(input("cuantos articulos son? "))
    costo = precio * artis
    costo2 = costo * 0.15
    iva = costo2 + costo
    print(f"tu importe es de ${iva}\n")

    tarje = str(input("deseas pagar con tarjeta o efectivo? ")).upper()

    if tarje == "TARJETA":
        tarjee = iva * 0.03
        tarje2 = tarjee + iva
        print(f"tu factura es de {tarje2:.2f}\n")

    elif tarje == "EFECTIVO":
        tarje2 = iva + 0
        print(f"tu total es {tarje2}\n")

    else:
        while tarje != "TARJETA" or tarje != "EFECTIVO":
            print("digito mal su metodo de pago\nvuevalo a digitarlo")
            tarje = str(input("deseas pagar con tarjeta o efectivo? ")).upper()

    xd = str(input("deseas donar a la calidad (si/no)? ")).upper()
    if xd == "SI":
        hola2 = int(input("cuanto deseas donar a la calidad: "))
        tarje2 += hola2
        print(f"tu total ahora es de ${tarje2:.2f}")
        print("gracias por tu donacion\n")


    hola = str(input(f"articulo que tienes son {nombres}\ndeseas devolver algun articulo (si/no)? ")).upper()
    if hola == "SI":

        devolver = str(input("que articulos deseas devolver: "))

        while devolver != artinom:
            print("el articulo que digito no se encuentra en la compra")
            devolver = str(input("que articulos deseas devolver: "))

        product = int(input("cuantos articulos deseas devolver: "))

        while artis < product or product == 0:
            if artis < product:
                print("la cantidad de articulos es mayor de las que tienes\n vuelva a digitarlo")
                product = int(input("cuantos articulos deseas devolver: "))

            elif product == 0:
                print("el digito debe ser mayor a 1")
                product = int(input("cuantos articulos deseas devolver: "))
        if product == artis:
            if product > 2 and artis > 2:
                print(f"los articulos {artinom} fueron devueltos por el monto de ${tarje2}")
            elif product < 1 and artis < 1:
                print(f"el articulo {artinom} fue devuelto por el monto de ${tarje2}")
        elif product != artis:
            if tarje == "TARJETA":
                pan = product - artis
                con = product * precio
                leche = con * 0.15
                iva2 = con + leche
                iva3 = iva2 * 0.03
                iva4 = iva3 + iva2
                print(f"los articulos {artinom} fueron devueltos por el monto de ${iva4}")
                print(f"tus articulos restantes son {artinom} y piezas {pan}")
                print(f"tu total a pagar {iva4 - tarje2:.2f}")
            elif tarje == "EFECTIVO":
                pan = product - artis
                con = product * precio
                leche = con * 0.15
                iva2 = con + leche
                print(f"los articulos {artinom} fueron devueltos por el monto de ${iva2}")
                print(f"tus articulos restantes son {artinom} y piezas {pan}")
                print(f"tu total a pagar {iva2 - tarje2:.2f}")
print("Gracias por tu compra\n")
