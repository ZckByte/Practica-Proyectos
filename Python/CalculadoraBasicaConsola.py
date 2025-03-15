#Calculadora BASICA Desde Consola, sin excepciones, ni bucles

#Inputs de usuario

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#Operacion 

operation = input("\n1. Suma\n2. Multiplicación \n3. Resta\n4. Division \nQue desea realizar?: " )

#Resultado con condicional

if operation == "1":
    print(f"La suma de {num1} y {num2} es: {num1+num2}")
elif operation == "2":
    print(f"La multiplicacion de {num1} y {num2} es: {num1*num2}")
elif operation == "3":
    print(f"La resta de {num1} y {num2} es: {num1-num2}")
elif operation == "4":
    print(f"La división de {num1} entre {num2} es: {num1/num2}")