def tiempo(cantidad):
    time.sleep(cantidad)
#Gestor de notas con sqlite 
import os
import sqlite3
import time
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
        while True:
            titulo = str(input("Ingrese el titulo de la nota: "))
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
    else:
        print("Ingrese una opción valido")
        continue
    break
conex.commit()
resu = cs.fetchall()
for fila in resu:
    print(fila)
conex.close()

