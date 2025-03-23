#Gestor de notas con variables y bloc de notas
import os
seleccion = None
ruta = "C:/Users/Administrator/Desktop/Coding/Python/Notas"
print("....Gestor de Notas....\n1. Crear Notas\n2. Modificar Notas\n3. Eliminar Archivo")
while True: 
    try:
        seleccion = int(input("Que desea realizar: "))
        nombre = str(input("Nombra el archivo: "))       
        break
    except:
        print("!Ingrese un numero valido!")
        continue
if seleccion == 1: 
    open(f'{ruta}/{nombre}.txt', 'x').close()
    print("Creado exitosamente")
if seleccion == 2:
    print("")
    print("....Gestor de notas....\n1. Agregar Texto\n2. Eliminar Todo El Texto\n3. Leer Archivo")
    seleccion2 = int(input("Que desea realizar: "))
    if seleccion2 == 1:
        while True:    
            try:
                with open(f'{ruta}/{nombre}.txt','a', encoding="utf-8") as archivo:
                    escribir = str(input("Escriba: "))  
                    archivo.write(escribir + "\n")
                    print("Escrito correctamente.")
                break
            except:
                print("No se encontro el archivo.")
                continue   
    if seleccion2 == 2:
        open(f"{ruta}/{nombre}.txt", 'w').close()
        print("Notas Eliminadas.")
    if seleccion2 == 3:
        with open(f'{ruta}/{nombre}.txt', 'r') as leer:
            print("")
            print(leer.read())
            print("")
if seleccion == 3:
    print("----------------------")
    try:
        os.remove(f"C:/Users/Administrator/Desktop/Coding/Python/Notas/{nombre}.txt")
        print("Se elimino exitosamente.")
    except:
        print("El archivo no existe.")