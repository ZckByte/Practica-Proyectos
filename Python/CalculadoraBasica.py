#Calculadora Basica 2/13/25
seguir = True 
while seguir:
    calc = input("Desea calcular? S o N: ")
    calc = calc.lower()
    operaciones = ["+", "-", "*", "/"]
    if calc == "s":
        seguir = False
        operacion = str(input(f"Ingrese la operacion {operaciones}: "))
        if operacion == "+" or operacion == "-" or operacion == "*":
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
        elif operacion == "-":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
        if operacion == "+":
            resultado = num1 + num2 
            print(f"La suma de {num1} y {num2} es: {resultado}")
        elif operacion == "-":
            resultado = num1 - num2 
            print(f"La resta de {num1} y {num2} es: {resultado}")
        elif operacion == "*":
            resultado = num1 + num2 
            print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    else:
        seguir = False
