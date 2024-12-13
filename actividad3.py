lista_numeros = [11, 22, 33, 44, 55, 66, 77, 88, 99] #poseemos la lista con números

def suma_menores(lista_numeros):
    return sum(i for i in lista_numeros if 0 < i < 1000)#el for, va recorriendo cada índice y va sumando, algo asi como un "acumulador", mientras que la i (índice) es contador

print(suma_menores(lista_numeros))#Imprime la suma
