from nave import Nave
from casilla import Casilla


class Tablero:
    def __init__(self):
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        # ===== NAVES =====
        por1 = Nave("Enterprise", "portaaviones", 5)

        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        # ===== TABLERO: matriz 10x10 de objetos Casilla =====
        self.casillero = [[Casilla() for _ in range(10)] for _ in range(10)]

        # ===== COLOCAR NAVES: asignar nave al atributo .nave de cada Casilla =====

        # Portaaviones — fila 1, columnas 1-5
        self.casillero[1][1].nave = por1
        self.casillero[1][2].nave = por1
        self.casillero[1][3].nave = por1
        self.casillero[1][4].nave = por1
        self.casillero[1][5].nave = por1

        # Bismarck — columna 3, filas 3-5 (vertical)
        self.casillero[3][3].nave = fra1
        self.casillero[4][3].nave = fra1
        self.casillero[5][3].nave = fra1

        # Prince of Wales — fila 7, columnas 1-3
        self.casillero[7][1].nave = fra2
        self.casillero[7][2].nave = fra2
        self.casillero[7][3].nave = fra2

        # Graf Spee — fila 9, columnas 1-3
        self.casillero[9][1].nave = fra3
        self.casillero[9][2].nave = fra3
        self.casillero[9][3].nave = fra3

        # Submarinos
        self.casillero[4][6].nave = sub1
        self.casillero[9][9].nave = sub2
        self.casillero[7][6].nave = sub3
        self.casillero[9][5].nave = sub4

    # ===== DISPARO =====
    def comprobar_impacto(self, x, y):
        return self.casillero[x][y].disparar()