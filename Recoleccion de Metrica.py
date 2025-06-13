import psutil
import pandas as pd
import time

datos = []

print("Recolectando datos del uso del CPU...")

for i in range(60):  # 1 minuto de muestras, una cada segundo
    uso_cpu = psutil.cpu_percent(interval=1)
    tiempo_actual = time.strftime("%H:%M:%S")
    datos.append({"Tiempo": tiempo_actual, "Uso_CPU": uso_cpu})
    print(f"[{tiempo_actual}] Uso del CPU: {uso_cpu}%")

df = pd.DataFrame(datos)
df.to_csv("Metrica del Parcial.csv", index=False)
print("Datos guardados en 'Metrica del Parcial.csv'")
