import random

#"tirar" la moneda (nos tira un vlor lógico, que es cara o cruz)
def lanzar_moneda():
    return random.choice(["Cara", "Cruz"]) 

#función para probar suerte
def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("la lista se autodestruirá")
        return []  
        #devuelve una lista vacía
    else:
        print("la lista fue salvada")
        return lista_numeros  
        #devuelve la lista intacta

#lista de números
lista_numeros = [27, 5, 2004]

#ejecutar las funciones
resultado = lanzar_moneda()  

print(f"resultado de la moneda: {resultado}")  
#mostrar el resultado de la moneda

#creamos una lista "nueva", tomando los datos de la lista de números, en caso de que la moneda de cruz, si da cara, solo se borra la lista
lista_nueva = probar_suerte(resultado, lista_numeros)

print(f"estado de la lista: {lista_nueva}")

