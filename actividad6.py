class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):#hijo hereda de padre
    def hobby(self):#cambiamos el metodo hobby()
        return "Juego videojuegos en mi tiempo libre"


#creamos una instancia de la clase Hijo
hijo = Hijo()

#llamar al metodo hobby
print(hijo.hobby())  
