# 19/02/2024


print("\n*** Bucle while ***")


# Es necesario importar las depencendias necesarias
from datetime import datetime
import time
import os


# Año, Mes, Dia, Hora, Minutos, Segundos, Milisegundos:
warning_date = datetime(2027, 6, 21, 00, 00, 00, 00000)
end_date = datetime(2030, 6, 21, 00, 00, 00, 00000)

current_date = datetime.now()

diff_date1_days = (warning_date - current_date).days
diff_date2_days = (end_date - current_date).days

remaining_weeks1 = diff_date1_days//7
remaining_weeks2 = diff_date2_days//7


print(f"\nWarning Date Countdown (days): {diff_date1_days}")
print(f"Warning Date Countdown (weeks): {remaining_weeks1}")

print(f"\nEnd Date Countdown (days): {diff_date2_days}")
print(f"End Date Countdown (weeks): {remaining_weeks2}")

time.sleep(5)
os.system("cls")


while (diff_date1_days) > 0:
    
    for i in range(1, 8):
        diff_date1_days -= 1
        print(f"Remaining days until warning: {diff_date1_days}")
        
        time.sleep(1)
        os.system("cls")
    
    
    remaining_weeks1 -= 1
    print("Uuups, a week has gone by")
    print(f"Remaining weeks until warning: {remaining_weeks1}")
    
    time.sleep(3)
    os.system("cls")