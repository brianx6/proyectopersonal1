num1 = float(input("digite el numero 1:"))
num2 = float(input("digite el numero 2:"))

operacion = input("digite la operacion:").upper()

if operacion=="SUMA":
    sum=num1+num2
    print(f"\nla suma es: {sum}")
elif operacion=="RESTA":
    rest=num1-num2
    print(f"\nla resta es: {rest}")
elif operacion=="MULTIPLICACION":
    multi=num1*num2
    print(f"\nla multiplicacion es: {multi}")
elif operacion=="DIVISION":
    div=num1/num2
    print(f"\nla division es: {div:.2f}")
else:
    print("\se equivoco de operacion")
