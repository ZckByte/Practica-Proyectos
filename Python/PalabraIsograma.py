#Verificar si una palabra es isograma o no

palabra = str(input("Ingrese una palabra: "))
verificar = []
prueba = None

for i in palabra:
    verificar.append(i)
    cantidad = verificar.count(i)
    if cantidad == 2:
        prueba = 2
        break;
    if cantidad == 1:
        prueba = 1;
        continue
if prueba == 1:
    print("No es un isograma")
else:
    print("Es un isograma")