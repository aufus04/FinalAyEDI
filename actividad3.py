lista_numeros = [11, 22, 33, 44, 55, 66, 77, 88, 99]

def suma_menores(lista_numeros):
    return sum(i for i in lista_numeros if 0 < i < 1000)

print(suma_menores(lista_numeros))
