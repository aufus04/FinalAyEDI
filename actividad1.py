''''
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
(es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
Si la suma es menor o igual a 6:
    "La suma de tus dados es {suma_dados}. Lamentable"
Si la suma es mayor a 6 y menor a 10:
    "La suma de tus dados es {suma_dados}. Tienes buenas chances"
Si la suma es mayor o igual a 10:
    "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6
'''

import random

#función de tirar dados
def lanzar_dados():
    dado1 = random.randint(1, 6)  
    dado2 = random.randint(1, 6)  
    return dado1, dado2  #devuelve dados

#evaluamos la jugada
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2  #suma total de puntos
    #ya de ahí, se deriva, retornando las 3 alternativas posibles
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 7 <= suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

#tests de funciones

#tiro los dados
dado1, dado2 = lanzar_dados()  

#ver puntuacion 
resultado = evaluar_jugada(dado1, dado2)  

#imprimo el resultado
print(resultado)  