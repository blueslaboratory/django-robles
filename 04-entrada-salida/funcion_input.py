# 19/02/2024


print("\n*** Entrada y salida ***")


# Es necesario importar las depencendias necesarias
from datetime import datetime


# Entrada
# INPUT siempre recoge un STRING
nombre = input("Nombre: ")
edad = input("Edad: ")
year = format(datetime.now().year)


# Salida
print(f"Year actual: {year} --> {type(year)}")
print(f"Bienvenido {nombre}, naciste el year: {int(year) - int(edad)}")