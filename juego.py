from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")
        elif resultado is None:
            print("Ya disparaste aquí")

    def lanzar_ataque(self, x, y):
        print(f"\nAtaque en ({x},{y})")

        resultado = self.tablero.comprobar_impacto(x, y)

        self.mostrar_resultado(resultado)

    def jugar_demo(self):
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(1, 4)
        self.lanzar_ataque(1, 5)


if __name__ == "__main__":
    juego = Juego()
    juego.jugar_demo()