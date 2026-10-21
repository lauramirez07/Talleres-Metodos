import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x) - x**2 + 1


def biseccion(a, b, tolerancia=1e-12):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("El intervalo debe contener un cambio de signo.")

    while b - a > tolerancia:
        medio = (a + b) / 2
        fm = f(medio)

        if fa * fm <= 0:
            b = medio
            fb = fm
        else:
            a = medio
            fa = fm

    return (a + b) / 2


raiz1 = biseccion(-1, 0)
raiz2 = biseccion(1, 1.5)

print(f"Primera raíz: {raiz1:.4f}")
print(f"Segunda raíz: {raiz2:.4f}")


