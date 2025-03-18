def pedir_input_string():
    texto = str(input("Ingrese: "))
    return texto;
#Gestor de notas con sqlite 
import os
import sqlite3
import time
conex = sqlite3.connect('notas.db')
cs = conex.cursor()
contenido = "";
titulo = "";

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
    eleccion = int(input("\nIngrese que desea realizar: "))
    input_eleccion = pedir_input_string()
    os.system('cls')
    if eleccion == 1:
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
    elif eleccion == 2:
        print("....Modificación....")
        titulo = str(input("Ingrese el titulo de la nota: "))
        modificacion_eleccion = int(input("1. Titulo\n2. Contenido\nQue desea modificar: "))
        if modificacion_eleccion == 1:
            input_eleccion()
            if input_eleccion == "1":
                print("Si")
    else:
        print("Ingrese una opción valido")
        continue
    break
conex.commit()
resu = cs.fetchall()
for fila in resu:
    print(fila)
conex.close()

