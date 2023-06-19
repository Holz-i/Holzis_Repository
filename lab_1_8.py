import numpy as np
import matplotlib.pyplot as plt

# Erzeugung der Winkelwerte von 0 bis 360 Grad
angles = np.arange(0, 361)

# Berechnung der Genauigkeit als Cosinus des Winkels (angepasstes Beispiel)
accuracy = np.cos(np.deg2rad(angles))

# Plot erstellen
plt.plot(angles, accuracy)
plt.title("Genauigkeit in Winkelgraden")
plt.xlabel("Winkel in Grad")
plt.ylabel("Genauigkeit")
plt.grid(True)
plt.show()