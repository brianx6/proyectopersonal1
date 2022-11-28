saldo = 1000

print("\t.:menu:.")
print("1. ingresar dinero en la cuenta")
print("2. retirar dinero de la cuenta")
print("3. mostrar dinero disponible")
print("4. salir")
opcion = int(input("digite una opcion de menu: "))

print()

if opcion==1:
    add=float(input("cuanto dinero deseas ingresar: "))
    saldo=add+saldo
    print(f"dinero en la cuenta: {saldo}")
elif opcion==2:
    retirar=float(input("cuanto dinero deseas retirar: "))
    if retirar>saldo:
        print(f"no tienes esa cantidad de dinero")
    else:
        saldo=saldo-retirar
        print(f"dinero en la cuenta: {saldo}")
elif opcion==3:
    print(f"dinero en la cuenta: {saldo}")
elif opcion==4:
    print("gracias. que tengas un buen dia")
else:
    print("opcion erronea, vuelva a iniciar")