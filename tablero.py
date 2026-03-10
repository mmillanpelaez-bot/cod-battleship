from nave import Nave
class Tablero:
    def __init__(self):
        #self.casilla = casilla
        #self.tamanho = tamanho
        #self.max = max_barco
       #self.min = min_barco
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2
        # Creamos una nave de ejemplo
        self.nave = Nave("Destructor", 2)
        # Posición de la nave
        self.nave_x = 3
        self.nave_y = 2

    def comprobar_impacto(self, x, y):
        print("Estoy comprobando el impacto")

        if x == self.nave_x and y == self.nave_y:
            return self.nave.recibir_disparo()

        return self.AGUA