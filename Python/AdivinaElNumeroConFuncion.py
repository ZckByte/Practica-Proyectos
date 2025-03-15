#Adivina el número, con función
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

def numAleatorio(inicio, final):
    seguir1 = True
    while seguir1:
        try:
            numero_random = None
            intentos = 0
            resultado = None
            numero_random = random.randrange(inicio, final)
            print("")
            print("...EL NUMERO RANDOM HA SIDO ESCOGIDO...")
            while True:
                print("")
                adivinado = int(input((f"Escoga un numero del {inicio}-{final-1}: ")))
                if adivinado > final or adivinado < 0:
                    print("")
                    print("🛑Escoga un numero dentro del limite, intentos -1🛑")
                    intentos = intentos - 1
                    if intentos < 0:
                        intentos = intentos + 1
                if adivinado == numero_random:
                    print("!!!!!!!!!!!")
                    resultado = print(f"!NUMERO CORRECTO!, Intentos: {intentos}")
                    seguir1 = False
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
    return resultado

while seguir:
    if limite == 1:
        numAleatorio(0,11)
    if limite == 2:
        numAleatorio(0,26)
    if limite == 3:
        numAleatorio(0,51)
    if limite == 4: 
        numAleatorio(0,101)
    seguir = False
