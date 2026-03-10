class Nave:
    def __init__(self, nombre, tamanho):
        self.nombre = nombre
        self.vida = tamanho
        self.hundido = False

        self.TOCADO = 1
        self.HUNDIDO = 2

    def recibir_disparo(self):
        self.vida -= 1

        if self.vida <= 0:
            self.hundido = True
            return self.HUNDIDO
        else:
            return self.TOCADO