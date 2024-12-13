class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")
#de antemano, tenemos el cómo se va a defender cada uno

#creamos una función de defenderse
def personaje_defender(personaje):
    personaje.defender()
    #llamamos a la función de defender, dependiendo del personaje, nos va a imprimir el cómo va a defenderse

#creamos objetos de las clases Mago, Arquero y Samurai
mago = Mago()
arquero = Arquero()
samurai = Samurai()

#invocamos las funciones englobando a cada clase
#los personajes tienen una acción en comun: defenderse (Todos para uno y uno para todos), pero el cómo, varía según la clase
personaje_defender(mago)
personaje_defender(arquero)
personaje_defender(samurai)

