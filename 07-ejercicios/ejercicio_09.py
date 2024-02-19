# 19/02/2024

"""
Ejercicio 9. Estas en un escape room hasta que introduces la password.
"""

print("\n*** Ejercicio 9 ***")

import time
import threading


def countdown_timer():
    global countdown
    countdown = 3
    while countdown > 0:
        time.sleep(1)
        countdown -= 1


user_pw = ""
system_pw = "sacatan sacatun tan tan tan que summun pen que tum pan que tepetepe tan tu que tun pan to que tun"
countdown = 0

thread = threading.Thread(target=countdown_timer)
thread.start()


print(f"Tienes {countdown} segundos para escapar de la simulacion")
print("¿Cuál es la password?")


while user_pw != system_pw and countdown > 0:
    user_pw = input("> ")

    if user_pw == system_pw:
        print("¡Lo lograste! ¡Libertad!")
        break
    else:
        print(f"Quedan {countdown} segundos. TIC TAC.")

if user_pw != system_pw and countdown <= 0:
    print("¡Se acabó el tiempo! ¡Te atraparon!")