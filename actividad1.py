#importamos la biblioteca random
import random

def lanzar_dados():
    #"tiramos" dados (simbólicamente)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2 #retornar los dados (lo que retorna se usa en evaluar_jugada)

def evaluar_jugada(dado1, dado2):
    #dependiendo de suma_dados, hay 3 posibles respuestas
    suma_dados = dado1 + dado2
    if suma_dados >= 2 and suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados <= 9:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

menu = "------------------CASINO DE AUGUSTO------------------"
print(menu)
#test de funciones
dado1, dado2 = lanzar_dados()
print(f"tiraste los dados: {dado1} y {dado2}") #nos dice que dados "tiré"
resultado = evaluar_jugada(dado1, dado2)
print(resultado)
