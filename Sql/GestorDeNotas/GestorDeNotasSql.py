#Gestor de notas con sqlite 
import os
import sqlite3
conex = sqlite3.connect('notas.db')
cs = conex.cursor()

cs.execute(''' 
    CREATE TABLE IF NOT EXISTS notas(
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    contenido TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

print("....Gestor De Notas Con SQL....")
print("1. Crear Notas\n2. Modificar Notas\n3.Eliminar")
while True:
    eleccion = int(input("\nIngrese que desea realizar: "))
    if eleccion == 1:
        os.system('cls')
        print("....Crear Notas....")
        nombre = str(input("Ingrese un nombre para el archivo: "))
        print("")
    else:
        print("Ingrese una opción valido")
        continue
    break
print("Pal commit xD")


conex.commit()
resu = cs.fetchall()
for fila in resu:
    print(fila)
conex.close()
