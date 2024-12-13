class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass
#definimos un objeto instancia de clase hija ornitorrinco (hereda las caracteristicas de Vertebrado)
ornitorrinco = Ornitorrinco()

ornitorrinco.poner_huevos()
print(ornitorrinco.tiene_pico)
print(ornitorrinco.vertebrado)
print(ornitorrinco.venenoso)
ornitorrinco.nadar()
ornitorrinco.caminar()
ornitorrinco.amamantar()
#atributos del ornitorrinco (perry)
