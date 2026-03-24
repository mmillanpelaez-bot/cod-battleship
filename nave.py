class Nave:
    TOCADO = 1
    HUNDIDO = 2

    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.hundido = False

    def recibir_disparo(self):
        if self.hundido:
            return self.HUNDIDO

        self.vida -= 1

        if self.vida <= 0:
            self.vida = 0
            self.hundido = True
            print(f"{self.nombre} hundido")
            return self.HUNDIDO
        else:
            print(f"{self.nombre} tocado. Vida restante: {self.vida}")
            return self.TOCADO