import numpy as np

#FUNCION ES:  8 * np.sin(x) * np.exp(-x) - 1

# 3 cifras significativas => tol = 0.05%  (criterio: 0.5 * 10^(2-n) con n=3)

def punto_fijo(x0, g, tol=0.05, max_iter=100):
    print("\n" + "-" * 50)
    print("MÉTODO DE PUNTO FIJO")
    print(f"Iter   | Xi         | g(Xi)      | ea (%)")
    print("-" * 50)

    xi = x0
    for i in range(1, max_iter + 1):
        gi = g(xi)
        ea = abs((gi - xi) / gi) * 100

        print(f"{i:<5} | {xi:<10.6f} | {gi:<10.6f} | {ea:<10.4f}")

        if ea < tol:
            break
        xi = gi
    return gi


# --- Raíz 1 ≈ 0.14501 ---
# Despeje: 8·sin(x)·e^(-x) = 1 => sin(x) = e^x/8 => x = arcsin(e^x/8)
def g1(x):
    return np.arcsin(np.exp(x) / 8)

print("\n" + "=" * 50)
print("RAÍZ 1  |  g(x) = arcsin(e^x / 8)  |  x0 = 0.5")
print("=" * 50)
raiz1 = punto_fijo(x0=0.5, g=g1)

print("\n" + "=" * 50)
print(f"Punto Fijo Raíz 1: {raiz1:.6f}")


# --- Raíz 2 ≈ 1.98903 ---
# Despeje: 8·sin(x)·e^(-x) = 1 => e^x = 8·sin(x) => x = ln(8·sin(x))
def g2(x):
    return np.log(8 * np.sin(x))

print("\n" + "=" * 50)
print("RAÍZ 2  |  g(x) = ln(8·sin(x))     |  x0 = 1.0")
print("=" * 50)
raiz2 = punto_fijo(x0=1.0, g=g2)

print("\n" + "=" * 50)
print(f"Punto Fijo Raíz 2: {raiz2:.6f}")
