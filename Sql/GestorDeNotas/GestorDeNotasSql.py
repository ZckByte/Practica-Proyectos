#Gestor de notas con sqlite 
def tiempo(cantidad):
    time.sleep(cantidad)
def clear():
    os.system('cls')
import os
import sqlite3
import time
clear()
conex = sqlite3.connect('notas.db')
cs = conex.cursor()
contenido = "";
resu = cs.fetchall()
titulo = "";
input_eleccion_int = 0;
id_nota = None;
cs.execute(''' 
    CREATE TABLE IF NOT EXISTS notas(
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    contenido TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

print("....Gestor De Notas Con SQL....")
print("1. Crear Notas\n2. Modificar Notas\n3. Eliminar\n4. Consultar Notas")
while True:
    input_eleccion_int = int(input("\nIngrese que desea realizar: "))
    os.system('cls')
    if input_eleccion_int == 1:
        print("....Crear Notas....")
        titulo = str(input("Ingrese un titulo para la nota: "))   
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
        cs.execute("SELECT * FROM notas WHERE titulo = ?", (titulo,))
    elif input_eleccion_int == 2:
        print("....Modificación....")
        titulo = str(input("Ingrese el titulo de la nota: "))
        while True:
            cs.execute("SELECT userID FROM notas WHERE titulo = ?",(titulo,))
            id_nota = cs.fetchone()
            if id_nota:
                iduser = id_nota[0]
                print("Nota encontrada..")
                time.sleep(2)
                os.system('cls')
                break;
            else:
                os.system('cls')
                print("No se encontro la nota, Ingresa un titulo valido")
                os.system('cls')
                tiempo(2)
                continue;
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
    else:
        print("Ingrese una opción valido")
        continue
    break
conex.commit()
resu = cs.fetchall()
for fila in resu:
    print(fila)
conex.close()

