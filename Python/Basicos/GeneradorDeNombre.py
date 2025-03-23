#Generador de nombres con listas predefinidas
import random
#Cantidad de nombres

cantidad = int(input("Cantidad de nombres?: "))

#Listas predefinidas
List1 = ["Sofía","Mateo","Valentina","Lucas","Isabella"]
List2 = ["Gonzáles", "Rodríguez", "López", "Martínez", "García"]

#Generar nombres aleatorios

for i in range(cantidad): #El range funciona con un entero, se repite esa cantidad de veces

    #Indices
    indice1 = random.randrange(len(List1)) #el randrange, retorna un elemento random desde el 0 hasta el que se coloque menos uno
    indice2 = random.randrange(len(List2)) #y len se utiliza para sacar la cantidad de index que tenga una lista
    print(f"Nombre: {List1[indice1]} {List2[indice2]}" )
    