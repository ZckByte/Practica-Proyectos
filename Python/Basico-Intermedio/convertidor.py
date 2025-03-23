import requests #Request se utiliza para hacer peticiones a paginas y traer datos

url = 'https://api.frankfurter.dev/v1/latest?base=USD' #De donde se sacaran los datos, es mejor buscar en apis
req = requests.get(url) #aca manda la petición a la url para sacar los datos

data = req.json() #una vez se tenga los datos se guarda en un json (diccionario)

#Para sacar datos espeficicos de un diccionario primero
#Se coloca el diccionario["La llave"]["dato a sacar"]

usd_to_mxn = data["rates"]["MXN"] #De usd a mx
usd_to_euro = data["rates"]["EUR"] #de usd a euro tasa
cantidad_mxn = 1000

monto_de_mx_en_usd = cantidad_mxn / usd_to_mxn
monto_de_mxusd_a_euro = monto_de_mx_en_usd * usd_to_euro

 

print(f"{cantidad_mxn} de pesos mexicanos a euro, con dolar de intermediario es: {monto_de_mxusd_a_euro}")
# print(f"Porque la conversión de dolar a peso mexicano es {usd_to_mxn}")
# print(f"Y la conversion de dolar a euro es: {usd_to_euro}")
print(f"""Primero se saca la tasa de cambio de usd a mxn {usd_to_mxn}, luego de usd a euro {usd_to_euro}
    se define una cantidad a convertir de pesos mexicanos a euro, {cantidad_mxn}
    se hace la conversion de la cantidad de pesos mexicanos en la tasa de cambio de usd a mxn {monto_de_mx_en_usd}
    es decir {cantidad_mxn} / {usd_to_mxn} se divide porque se pasa de mx a usd
    se multiplica la cantidad de pesos mexicanos convertidos en usd por la tasa de cambio de el dolar a euro
    y da como resultado {monto_de_mxusd_a_euro}
    """)
    #Aunque es mas facil sin intermediarios, pero asi se hace con intermediarios
# print(json.dumps(req.json(), indent=4))

#El codigo de la linea 32 es para que se imprima de una manera mas legible el diccionario