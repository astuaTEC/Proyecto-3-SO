from datetime import datetime
import psutil

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
ORANGE = '\033[33m'
RED = '\033[31m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
PINK = '\033[95m'


"""
Toma una función como argumento y devuelve una función 
wrapper que muestra el uso de la CPU de la función original.
"""
def cpuStats(func):

    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(RED + '*'*50 + ENDC)
        print(f'{WARNING}Tiempo transcurrido: {time_elapsed}')
        print(f'{OKBLUE}Porcentaje CPU: {psutil.cpu_percent()} %')
        print(f'{ORANGE}Estadísticas del CPU: {psutil.cpu_stats()}')
        print(f'{OKCYAN}Memoria RAM: {psutil.virtual_memory().percent} %{ENDC}')
        print(RED + '*'*50 + ENDC)
    return wrapper
