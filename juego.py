from tablero import Tablero
class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.lanzar_ataque(3,2)

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        print(f"Ataque a {x},{y}")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

if __name__ == "__main__":
    Juego()