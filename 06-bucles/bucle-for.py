# 19/02/2024


print("\n*** Bucle for ***")


import time

counter = 0

# [0, 3]
for counter in range(0, 4):
    time.sleep(0.5)
    print(f"Counter: {counter}")
    


print("\nTabla de multiplicar")
n_user = int(input("Numero de la tabla: "))

if n_user < 1:
    n_user = 1
else:
    # [1, 10]
    for i in range(1, 11):
        
        if n_user == 69:
            print("break --> sexy time")
            break
        
        print(f"{n_user} x {i} = {n_user*i}")