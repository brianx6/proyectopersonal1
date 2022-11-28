print()

nombres = {}
valor = []
cantidad = []
total = []

clientes = int(input("cuantos clientes son? "))

for i in range(clientes):

       while True:
        artinom = str(input("\nnombre del articulo: ")).lower()
        precio = int(input("cual es el precio del articulo: "))
        cantidad.append(precio)
        artis = int(input(" cuantos articulos son? "))
        nombres[artinom] = artis
        aa = str(input("deseas otro producto si/no? ")).upper()
        costo = precio * artis
        costo2 = costo * 0.15
        iva = costo2 + costo
        total.append(iva)
        if aa == "SI":
            break

        ss = sum(total) + 0
        print(f"tu total es de {ss:.2f}\n")

        tarje = str(input("deseas pagar con tarjeta o efectivo? ")).upper()

        if tarje == "TARJETA":
            tarjee = ss * 0.03
            tarje2 = tarjee + ss
            print(f"tu factura es de {tarje2:.2f}\n")

        elif tarje == "EFECTIVO":
            tarje2 = ss+0
            print(f"tu total es {tarje2}\n")

        elif tarje != "TARJETA" or tarje != "EFECTIVO":
            print("digito mal su metodo de pago\nvuevalo a digitarlo")
            tarje = str(input("deseas pagar con tarjeta o efectivo? ")).upper()

        dn = str(input("deseas donar a la calidad si/no? ")).upper()
        if dn == "SI":
            hola2 = int(input("cuanto deseas donar a la calidad: "))
            tarje2 += hola2
            print(f"tu total ahora es de {tarje2:.2f}")
            print("gracias por tu donacion\n")

        hola = str(input(f"tus articulos de compras son "
                         f"{nombres.keys()}\ndeseas devolver algun producto si/no? ")).upper()
        if hola == "SI":
            nombres = str(input("que articulos deseas devolver: ")).lower()

            if nombres != artinom:

             while nombres != artinom:
                print("el articulo que digito no se encuentra")
                nombres = str(input("que articulos deseas devolver: ")).lower()

                product = int(input("cuantos articulos deseas devolver: "))

            if nombres < product or product == 0:
                while artis < product:
                    print("la cantidad de articulos es mayor de las que tienes\n vuelva a digitarlo")
                    product = int(input("cuantos articulos deseas devolver: "))
                while product == 0:
                    print("el digito debe ser mayor a 1")
                    product = int(input("cuantos articulos deseas devolver: "))
            if product == nombres:
                if product > 2 and nombres > 2:
                    print(f"los articulos {nombres} fueron devueltos por el monto de {tarje2}")
                elif product < 1 and nombres < 1:
                    print(f"el articulo {nombres} fue devueltoo por el monto de {tarje2}")
            elif product != artis:
                if tarje == "TARJETA":
                    pan = product - sum(cantidad)
                    con = product * precio
                    leche = con * 0.15
                    iva2 = con + leche
                    iva3 = iva2 * 0.03
                    iva4 = iva3 + iva2
                    print(f"los articulos {nombres} fueron devueltos por el monto de ${iva4}")
                    print(f"tus articulos restantes son {artinom}, {pan}")
                elif tarje == "EFECTIVO":
                    pan = product - artis
                    con = product * precio
                    leche = con * 0.15
                    iva2 = con + leche
                    print(f"los articulos {nombres} fueron devueltos por el monto de ${iva2}")
                    print(f"tus articulos restantes son {artinom}, {pan}")

print("Gracias por tu compra\n")
