import psutil
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def barra_progreso(porcentaje, longitud=30):
    bloques = int(porcentaje / 100 * longitud)
    barra = '█' * bloques + '-' * (longitud - bloques)
    return f"[{barra}] {porcentaje:.1f}%"

def obtener_top_procesos(metric="cpu", top_n=5):
    procesos = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            procesos.append(p.info)
        except psutil.NoSuchProcess:
            continue
    key = 'cpu_percent' if metric == "cpu" else 'memory_percent'
    procesos.sort(key=lambda p: p[key], reverse=True)
    return procesos[:top_n]

def mostrar_recursos():
    try: 
        while True:
            clear_console()
            print("=== MONITOR DE RECURSOS DEL SISTEMA ===\n")

            # Uso de CPU
            cpu = psutil.cpu_percent(interval=1)
            print(f"Uso de CPU:")
            print(barra_progreso(cpu))

            # Memoria RAM
            memoria = psutil.virtual_memory()
            porcentaje_ram = memoria.percent
            print("\nUso de Memoria RAM:")
            print(barra_progreso(porcentaje_ram))
            total_mem = memoria.total / (1024 ** 3)
            usada_mem = memoria.used / (1024 ** 3)
            libre_mem = memoria.available / (1024 ** 3)
            print(f"\nTotal: {total_mem:.2f} GB | Usada: {usada_mem:.2f} GB | Libre: {libre_mem:.2f} GB")

            # Disco
            disco = psutil.disk_usage('/')
            porcentaje_disco = disco.percent
            print("\nUso de Disco:")
            print(barra_progreso(porcentaje_disco))
            print(f"Total: {disco.total / (1024**3):.2f} GB | Usado: {disco.used / (1024**3):.2f} GB | Libre: {disco.free / (1024**3):.2f} GB")

            # Procesos
            print("\nTop 5 procesos por uso de CPU:")
            for p in obtener_top_procesos("cpu"):
                print(f"{p['name']} (PID {p['pid']}) - CPU: {p['cpu_percent']}%")

            print("\nTop 5 procesos por uso de RAM:")
            for p in obtener_top_procesos("mem"):
                print(f"{p['name']} (PID {p['pid']}) - RAM: {p['memory_percent']:.2f}%")

            time.sleep(20) # Esperar 20 segundos antes de actualizar
    except KeyboardInterrupt:
        print("\nMonitor detenido por el usuario.")

if __name__ == "__main__":
    mostrar_recursos()