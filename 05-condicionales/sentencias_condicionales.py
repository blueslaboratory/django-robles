# 19/02/2024

print("\n*** Sentencias condicionales ***")



print("\n############ EJEMPLO 7 ############")

pais = "FRANCIA".lower()
continente = "europa"

if pais == "mexico" or pais == "españa" or pais == "colombia":
    print(f"{pais} es un pais de habla hispana!!")
elif pais == "":
    print(f"Eres apatrida")
elif not pais != "francia":
    print(f"Liberte, egalite, fraternite")
    print(f"Vive la {pais}")
else:
    print(f"{pais} no es un pais de habla hispana :(")
    
    if continente == "europa":
        print(f"Al menos estas en {continente}, podria ser peor")
