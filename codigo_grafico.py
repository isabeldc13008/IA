import numpy as np
import matplotlib.pyplot as plt

trayectos = [
    "Tricentenario-Caribe",
    "Caribe-Hospital",
    "Hospital-ParqueBerrío",
    "ParqueBerrío-SanAntonio",
    "Hospital-Bello",
    "Bello-Hospital",
    "Niquía-Tricentenario",
    "Niquía-Bello"
]

tiempos_aproximados = [10, 15, 20, 25, 35, 15, 5, 30]
velocidades_metro = [80, 80, 80, 80, 80, 80, 80, 80]

x = np.arange(len(trayectos))
width = 0.4

fig, ax1 = plt.subplots()

# Barras agrupadas para velocidades_metro
ax1.bar(x - width/2, velocidades_metro, width, color="g", label="Velocidades_metro (Km/h)")

# Establecer rangos y etiquetas del eje y
ax1.set_ylabel("Velocidades_metro (Km/h)")
ax1.set_ylim(0, max(velocidades_metro) + 20)

# Configurar el eje x
ax1.set_xlabel("Trayecto")
ax1.set_xticks(x)
ax1.set_xticklabels(trayectos, rotation=45, ha="right")

# Crear un segundo eje y para tiempos_aproximados
ax2 = ax1.twinx()
ax2.set_ylabel("Tiempos_aproximados (minutos)")

# Línea con puntos para la velocidad del metro
ax2.plot(x, tiempos_aproximados, linestyle="--", marker="o", color="b", label="Tiempos_aproximados (minutos)")
ax2.set_ylim(0, max(velocidades_metro) + 10)

# Añadir leyendas
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.92))
fig.tight_layout()

plt.show()