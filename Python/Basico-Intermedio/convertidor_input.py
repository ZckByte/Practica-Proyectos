import requests
import Funciones as f
url = 'https://api.frankfurter.dev/v1/latest?base=USD'
req = requests.get(url)
data = req.json()
divisas = list(data["rates"])
# base = data["base"][""]
print("....Convetir Divisas....")
for i, key in enumerate(data["rates"]):
    print(f"{i}.",  key, end= " ")
print()
print("........................")
while True:
    try: 
        num = int(input("Convertir (ingrese el numero): "))
        primer_divisa = divisas[num]
        print("........................")
        num2 = int(input(f"Desea convertir {primer_divisa} a(ingrese el numero): "))
        segunda_divisa = divisas[num2]
        f.clear()
        print(f"....{primer_divisa} a {segunda_divisa}....")
    except:
        print("Numero invalido")
        f.delay(1.3)
        f.clear()
        continue;
    cantidad = int(input(f"Ingrese la cantidad de {primer_divisa} a convertir en {segunda_divisa}: "))
    primer_usd_tasa = data["rates"][f"{primer_divisa}"]
    segunda_usd_tasa = data["rates"][f"{segunda_divisa}"]
    monto_en_usd = cantidad / primer_usd_tasa
    conversion_de_usd = monto_en_usd * segunda_usd_tasa
    conversion_de_usd = round(conversion_de_usd)
    print(f"{cantidad}{primer_divisa} en {segunda_divisa} es: {conversion_de_usd}{segunda_divisa}")
    break;

