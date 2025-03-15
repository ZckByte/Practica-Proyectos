#Adivina el número, sin función
numero_random = None
intentos = 0
seguir = True
import random

print("...... Adivinanza ......")
print("\n1. 0-10\n2. 0-25\n3. 0-50\n4. 0-100\n")
while True:
    try: 
        limite = int(input("Escoga el limite de la adivinanza: "))
        break
    except:
        print("Escoga un numero del 1 al 4")
        limite = int(input("Escoga el limite de la adivinanza: "))

    

while seguir:

            try: 
                if limite == 1:
                    numero_random = random.randrange(11)
                    print("")
                    print("...EL NUMERO RANDOM HA SIDO ESCOGIDO...")
                    while True:
                        print("")
                        adivinado = int(input(("Escoga un numero del 0-10: ")))
                        if adivinado > 10 or adivinado < 0:
                            print("")
                            print("🛑Escoga un numero dentro del limite, intentos -1🛑")
                            intentos = intentos - 1
                            if intentos < 0:
                                intentos = intentos + 1
                        if adivinado == numero_random:
                            print("!!!!!!!!!!!")
                            print(f"!NUMERO CORRECTO!, Intentos: {intentos}")
                            seguir = False
                            break
                        else:
                            intentos += 1
                            print("")
                            print("!INCORRECTO!")
                            continue
                if limite == 2:
                    numero_random = random.randrange(26)
                    print("")
                    print("...EL NUMERO RANDOM HA SIDO ESCOGIDO...")
                    while True:
                        print("")
                        adivinado = int(input(("Escoga un numero del 0-26: ")))
                        if adivinado > 25 or adivinado < 0:
                            print("")
                            print("🛑Escoga un numero dentro del limite, intentos -1🛑")
                            intentos = intentos - 1
                            if intentos < 0:
                                intentos = intentos + 1
                        if adivinado == numero_random:
                            print("!!!!!!!!!!!")
                            print(f"!NUMERO CORRECTO!, Intentos: {intentos}")
                            seguir = False
                            break
                        else:
                            intentos += 1
                            print("")
                            print("!INCORRECTO!")
                            continue
                if limite == 3:
                    numero_random = random.randrange(51)
                    print("")
                    print("...EL NUMERO RANDOM HA SIDO ESCOGIDO...")
                    while True:
                        print("")
                        adivinado = int(input(("Escoga un numero del 0-50: ")))
                        if adivinado > 50 or adivinado < 0:
                            print("")
                            print("🛑Escoga un numero dentro del limite, intentos -1🛑")
                            intentos = intentos - 1
                            if intentos < 0:
                                intentos = intentos + 1
                        if adivinado == numero_random:
                            print("!!!!!!!!!!!")
                            print(f"!NUMERO CORRECTO!, Intentos: {intentos}")
                            seguir = False
                            break
                        else:
                            intentos += 1
                            print("")
                            print("!INCORRECTO!")
                            continue
                if limite == 4:
                    numero_random = random.randrange(101)
                    print("")
                    print("...EL NUMERO RANDOM HA SIDO ESCOGIDO...")
                    while True:
                        print("")
                        adivinado = int(input(("Escoga un numero del 0-100: ")))
                        if adivinado > 100 or adivinado < 0:
                            print("")
                            print("🛑Escoga un numero dentro del limite, intentos -1🛑")
                            intentos = intentos - 1
                            if intentos < 0:
                                intentos = intentos + 1
                        if adivinado == numero_random:
                            print("!!!!!!!!!!!")
                            print(f"!NUMERO CORRECTO!, Intentos: {intentos}")
                            seguir = False
                            break
                        else:
                            intentos += 1
                            print("")
                            print("!INCORRECTO!")
                            continue
            except:
                print("🛑Ingresa datos validos\nSe reiniciara tus intentos y el numero...🛑")
                intentos = 0
                continue