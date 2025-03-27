productos = {
    "Manzana": 1500,
    "Banano": 1200,
    "Pera": 1800,
    "Uvas": 3500
}


for i, fruta in enumerate(productos):
    print(i, fruta)
cantidad = int(input("Ingrese la cantidad que quiere ver: "))
claves = list(productos.keys())
frutas = claves[cantidad]
print(f"escogiste {frutas} en el indice {claves.index(frutas)} vale {productos[frutas]}")