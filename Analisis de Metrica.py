import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Metrica del Parcial.csv")

print("Resumen estadístico:")
print(df.describe())

sns.set(style="darkgrid")
plt.figure(figsize=(10, 5))
sns.lineplot(x="Tiempo", y="Uso_CPU", data=df, marker='o')
plt.title("Uso del CPU a lo largo del tiempo")
plt.ylabel("Uso del CPU (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
