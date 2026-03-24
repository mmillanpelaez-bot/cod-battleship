class Casilla:
    def __init__(self):
        self.nave = None
        self.visitada = False

    def disparar(self):
        if self.visitada:
            print("Ya disparaste aquí")
            return None

        self.visitada = True

        if self.nave is None:
            print("Agua")
            return 0

        return self.nave.recibir_disparo()