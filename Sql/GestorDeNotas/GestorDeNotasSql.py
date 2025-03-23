import os
import sqlite3
import time
#Gestor de notas con sqlite 
def tiempo(cantidad):
    time.sleep(cantidad)
def clear():
    os.system('cls')
clear()

conex = sqlite3.connect('notas.db')
cs = conex.cursor()
def mostrar():
    cs.execute("SELECT * FROM notas")
    conex.commit()
    resu = cs.fetchall()
    for fila in resu:
        print(fila)
def mostra_titulo(mostrar_titulo):
    cs.execute("SELECT * FROM notas WHERE titulo = ?",(mostrar_titulo,))
    conex.commit()
    resu = cs.fetchall()
    for fila in resu:
        print(fila)
contenido = "";
titulo = "";
input_eleccion_int = 0;
seguir = False;
id_nota = None;
cs.execute(''' 
    CREATE TABLE IF NOT EXISTS notas(
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    contenido TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
while not seguir:
    print("....Gestor De Notas Con SQL....")
    print("1. Crear Notas\n2. Modificar Notas\n3. Eliminar\n4. Consultar Notas\n5. Salir")
    while True:
        input_eleccion_int = int(input("\nIngrese que desea realizar: "))
        os.system('cls')
        if input_eleccion_int == 1:
            titulo = str(input("Ingrese un titulo para la nota: "))   
            print("....Crear Notas....")
            cs.execute("INSERT INTO notas (titulo) VALUES (?)", (titulo,))
            os.system('cls')
            print("....Contenido....")
            contenido = str(input("Contenido: "))
            cs.execute("UPDATE notas SET contenido = ? WHERE titulo = ?", (contenido,titulo))
            print("Agregado Exitosamente.")
            conex.commit()
            time.sleep(3)
            os.system('cls')
            print("....Visualización....")
            mostra_titulo(titulo)
            tiempo(3)
            clear()
        elif input_eleccion_int == 2:
            print("....Modificación....")
            while True:
                titulo = str(input("Ingrese el titulo de la nota: "))
                cs.execute("SELECT userID FROM notas WHERE titulo = ?",(titulo,))
                id_nota = cs.fetchone()
                if id_nota:
                    iduser = id_nota[0]
                    print("Nota encontrada..")
                    tiempo(1.5)
                    clear()
                    break;
                else:
                    print("Titulo Invalido");
                    time.sleep(1.5)
                    os.system('cls')
                    continue
            print("....Modificación....")
            modificacion_eleccion = int(input("1. Titulo\n2. Contenido\nQue desea modificar: "))
            if modificacion_eleccion == 1:
                os.system('cls')
                print("....Modificación De Titulo....")
                titulo_nuevo = str(input("Modificación de titulo: "))
                cs.execute('UPDATE notas SET titulo = ? WHERE userID = ?',(titulo_nuevo,iduser))
                print("Modificado Exitosamente.")
                tiempo(2)
                os.system('cls')
            if modificacion_eleccion == 2:
                clear()
                print("....Modificación De Contenido....")
                contenido_eleccion = int(input("1. Cambiar Contenido\n2. Agregar contenido\nQue desea realizar: "))
                if contenido_eleccion == 1:
                    clear()
                    print("....Cambiar Contenido....")
                    nuevo_contenido = str(input("Nuevo Contenido: "))
                    cs.execute('UPDATE notas SET contenido = ? WHERE userID = ?',(nuevo_contenido,iduser,))
                    print("Modificado Exitosamente.")
                    tiempo(2)
                    clear()
                elif contenido_eleccion == 2:
                    clear()
                    print("....Agregando Contenido....")
                    agregar_contenido = str(input("Contenido Agregado: "))
                    cs.execute('SELECT contenido FROM notas WHERE titulo = ?', (titulo,))
                    contenido_antiguo = cs.fetchone()
                    contenido_antiguo = contenido_antiguo[0]
                    contenido_nuevo = f"{contenido_antiguo } {agregar_contenido}"
                    cs.execute('UPDATE notas SET contenido = ? WHERE userID = ?',(contenido_nuevo,iduser))
                    print("Agregado Correctamente.")
                    tiempo(1.5)
                    clear()
        elif input_eleccion_int == 3:
            clear()
            print("....Eliminacion....")
            titulo = str(input("Ingrese el titulo de la nota: "))
            while True:
                cs.execute("SELECT userID FROM notas WHERE titulo = ?", (titulo,))
                id_nota = cs.fetchone();
                if id_nota:
                    iduser = id_nota[0]
                    print("Nota Encontrada..")
                    tiempo(1.5)
                    clear()
                    break;
                else:
                    print("Nombre Invalido")
                    tiempo(1.5)
                    clear()
                    continue;
            confirmacion = str(input("Confirma la eliminación, S/N: ")).lower()
            if confirmacion != "n":
                cs.execute("DELETE FROM notas WHERE titulo = ?", (titulo,))
                print("Notas Eliminada...")
                tiempo(1.5)
                clear()
        elif input_eleccion_int == 4:
            print("....Visualizacion Notas....")
            mostrar()
            input("Presione una tecla para continuar")
            clear()
            break
        elif input_eleccion_int == 5:
            print("!Gracias por utilizar!")
            tiempo(1.5)
            seguir = True
            clear()
            break
        else:
            print("Ingrese una opción valido")
            continue
        break
    if seguir:
        break;
    clear()
    seguir2 = str(input("Desea realizar otra acción?, S/N: ")).lower()
    if seguir2 != "n":
        clear()
        continue
    else:
        clear()
        break;
conex.commit()
conex.close()

