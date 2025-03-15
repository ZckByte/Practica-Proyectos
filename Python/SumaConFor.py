print("....Suma con for....")
cantidad = int(input("Ingrese la cantidad: "))
resultado = 0;
for i in range(1,cantidad+1):
    numero = int(input(f"Numero {i}: "))
    resultado += numero
print(resultado)

#Con while

resultado2 = 0;
print("....Suma con While....")
cantidad2 = int(input("Ingrese la cantidad: "))
cantidad21 = 0
while True:
    if cantidad21 == cantidad2:
        break
    numero2 = int(input(f"Numero {cantidad21+1}: "))
    resultado2 += numero2
    cantidad21 = cantidad21 + 1
    
print(resultado2)