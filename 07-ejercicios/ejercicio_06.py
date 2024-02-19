# 19/02/2024

"""
Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones.
"""

print("\n*** Ejercicio 6 ***")

for m in range(1, 11):
    print(f"\n*** Tabla del {m} ***")
    
    for n in range(1, 11):
        print(f"{m} x {n} = {m*n}")