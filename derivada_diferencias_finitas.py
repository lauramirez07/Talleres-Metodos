"""Diferencias finitas para f(x) = (tan(x))**ln(x) + x**4.

Metodos 1 y 2 de las formulas de clase para la primera derivada.
Se trabaja en radianes y la funcion real requiere x > 0 y tan(x) > 0.
"""

from math import cos, log, sin, tan


def f(x: float) -> float:
    tangente = tan(x)
    if x <= 0 or tangente <= 0:
        raise ValueError("Se requiere x > 0 y tan(x) > 0 para valores reales.")
    return tangente ** log(x) + x**4


def derivada_analitica(x: float) -> float:
    tangente = tan(x)
    if x <= 0 or tangente <= 0:
        raise ValueError("Se requiere x > 0 y tan(x) > 0 para valores reales.")
    potencia = tangente ** log(x)
    return potencia * (log(tangente) / x + log(x) / (sin(x) * cos(x))) + 4 * x**3


def adelante_metodo_1(x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h


def adelante_metodo_2(x: float, h: float) -> float:
    return (-f(x + 2 * h) + 4 * f(x + h) - 3 * f(x)) / (2 * h)


def atras_metodo_1(x: float, h: float) -> float:
    return (f(x) - f(x - h)) / h


def atras_metodo_2(x: float, h: float) -> float:
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)


def centrada_metodo_1(x: float, h: float) -> float:
    return (f(x + h) - f(x - h)) / (2 * h)


def centrada_metodo_2(x: float, h: float) -> float:
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def main() -> None:
    xi = 1.0
    h = 0.1
    valor_verdadero = 15.0
    error_maximo = 0.7

    metodos = {
        "Adelante, metodo 1": adelante_metodo_1,
        "Adelante, metodo 2": adelante_metodo_2,
        "Atras, metodo 1": atras_metodo_1,
        "Atras, metodo 2": atras_metodo_2,
        "Centrada, metodo 1": centrada_metodo_1,
        "Centrada, metodo 2": centrada_metodo_2,
    }

    print("f(x) = (tan(x))**ln(x) + x**4")
    print(f"xi = {xi}, h = {h}, valor verdadero indicado = {valor_verdadero}")
    print(f"Derivada analitica en xi: {derivada_analitica(xi):.6f}")
    print(f"Error maximo permitido: {error_maximo}\n")

    for nombre, metodo in metodos.items():
        aproximacion = metodo(xi, h)
        error = abs(valor_verdadero - aproximacion)
        cumple = "Si" if error < error_maximo else "No"
        print(f"{nombre:21s}: {aproximacion:.6f} | error vs. 15 = {error:.6f} | cumple: {cumple}")


if __name__ == "__main__":
    main()
