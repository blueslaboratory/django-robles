# 19/02/2024

"""
Ejercicio 5. Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario
"""

print("\n*** Ejercicio 5 ***")

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

if n1 > n2:
    n1, n2 = n2, n1

numeros = ""

for i in range(n1, n2+1):
    if(i != n2):
        numeros += f"{i}, "
    else:
        numeros += f"{i}"
        
print(f"Numeros: {numeros}")