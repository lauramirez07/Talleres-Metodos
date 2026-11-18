import math

# 1. Definimos la funcion f(x) = (tan(x))^ln(x) + x^4
def f(x):
    return (math.tan(x) ** math.log(x)) + (x ** 4)

# 2. Datos del problema
xi = 1
h = 0.1
valor = 15       
valor_real = 4.443023      # Derivada analitica real en xi = 1
error_max = 0.7

# 3. Calculo de las derivadas
adelante_1 = (f(xi + h) - f(xi)) / h
adelante_2 = (-f(xi + 2*h) + 4*f(xi + h) - 3*f(xi)) / (2*h)

atras_1 = (f(xi) - f(xi - h)) / h
atras_2 = (3*f(xi) - 4*f(xi - h) + f(xi - 2*h)) / (2*h)

centrada_1 = (f(xi + h) - f(xi - h)) / (2*h)
centrada_2 = (-f(xi + 2*h) + 8*f(xi + h) - 8*f(xi - h) + f(xi - 2*h)) / (12*h)

# 4. Calculo de los 3 errores para cada metodo
# Error 1: Absoluto 
e15_ad1 = abs(valor - adelante_1)
e15_ad2 = abs(valor - adelante_2)
e15_at1 = abs(valor - atras_1)
e15_at2 = abs(valor - atras_2)
e15_ce1 = abs(valor - centrada_1)
e15_ce2 = abs(valor - centrada_2)

# Error 2: Absoluto 
ereal_ad1 = abs(valor_real - adelante_1)
ereal_ad2 = abs(valor_real - adelante_2)
ereal_at1 = abs(valor_real - atras_1)
ereal_at2 = abs(valor_real - atras_2)
ereal_ce1 = abs(valor_real - centrada_1)
ereal_ce2 = abs(valor_real - centrada_2)

# Error 3: Relativo porcentual 
erel_ad1 = (ereal_ad1 / valor_real) * 100
erel_ad2 = (ereal_ad2 / valor_real) * 100
erel_at1 = (ereal_at1 / valor_real) * 100
erel_at2 = (ereal_at2 / valor_real) * 100
erel_ce1 = (ereal_ce1 / valor_real) * 100
erel_ce2 = (ereal_ce2 / valor_real) * 100

# 5. Mostrar resultados con los 3 errores
print("Adelante 1:", round(adelante_1, 4), "| Err vs 15:", round(e15_ad1, 4), "| Err Abs Real:", round(ereal_ad1, 4), "| Err Rel %:", round(erel_ad1, 4))
print("Adelante 2:", round(adelante_2, 4), "| Err vs 15:", round(e15_ad2, 4), "| Err Abs Real:", round(ereal_ad2, 4), "| Err Rel %:", round(erel_ad2, 4))
print("Atras 1:   ", round(atras_1, 4),    "| Err vs 15:", round(e15_at1, 4), "| Err Abs Real:", round(ereal_at1, 4), "| Err Rel %:", round(erel_at1, 4))
print("Atras 2:   ", round(atras_2, 4),    "| Err vs 15:", round(e15_at2, 4), "| Err Abs Real:", round(ereal_at2, 4), "| Err Rel %:", round(erel_at2, 4))
print("Centrada 1:", round(centrada_1, 4), "| Err vs 15:", round(e15_ce1, 4), "| Err Abs Real:", round(ereal_ce1, 4), "| Err Rel %:", round(erel_ce1, 4))
print("Centrada 2:", round(centrada_2, 4), "| Err vs 15:", round(e15_ce2, 4), "| Err Abs Real:", round(ereal_ce2, 4), "| Err Rel %:", round(erel_ce2, 4))


if erel_ad1 < error_max:
    print("- Adelante, metodo 1")
if erel_ad2 < error_max:
    print("- Adelante, metodo 2")
if erel_at1 < error_max:
    print("- Atras, metodo 1")
if erel_at2 < error_max:
    print("- Atras, metodo 2")
if erel_ce1 < error_max:
    print("- Centrada, metodo 1")
if erel_ce2 < error_max:
    print("- Centrada, metodo 2")