class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")
#creamos la instancia de cubo_rojo
print(cubo_rojo.caras)#imprime 6
print(cubo_rojo.color)#imprime rojo
