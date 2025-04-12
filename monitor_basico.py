import psutil
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_recursos():
    try: 
        while True:
            clear_console()
            print("=== MONITOR DE RECURSOS DEL SISTEMA ===\n")

            # Uso de CPU
            cpu = psutil.cpu_percent(interval=1)
            print(f"Uso de CPU: {cpu}%")

            # Memoria RAM
            memoria = psutil.virtual_memory()
            total_mem = memoria.total / (1024 ** 3)
            usada_mem = memoria.used / (1024 ** 3)
            libre_mem = memoria.available / (1024 ** 3)

            print(f"Memoria RAM Total: {total_mem:.2f} GB")
            print(f"Memoria RAM Usada: {usada_mem:.2f} GB")
            print(f"Memoria RAM Libre: {libre_mem:.2f} GB")

            time.sleep(1) # Esperar 1 segundo antes de actualizar
    except KeyboardInterrupt:
        print("\nMonitor detenido por el usuario.")

if __name__ == "__main__":
    mostrar_recursos()