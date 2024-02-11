import pandas as pd
import numpy as np

# Datos proporcionados
materiales = ["acrilico", "comprimido", "madera", "yeso", "vidrio"]
d1 = [9.4] * 5  # cm
d2 = {8.5: 8.3, 8.4: 8.4, 8.7: 8.4, 8: 8.3, 7.5: 7.5}  # cm
d2 = [abs(key + value) / 2 for key, value in d2.items()]  # cm
ta = [10 * 60] * 5  # mins to secs
m_tot = [206.8, 208.19, 210.14, 208.84, 216.82]  # g
t = [5, 5, 5, 5, 2]  # min
t = [value * 60 for value in t]  # mins to secs
m_wa = [15.43] * 5  # g, ambiental
m_vasito = [192.01] * 2 + [161.67] * 3

m_w = [m_tot[i] - m_vasito[i] for i in range(len(m_tot))]

# Crear DataFrame
df = pd.DataFrame({"d1": d1, "d2": d2, "ta": ta, "m_tot": m_tot, "t": t, "m_wa": m_wa,
                   "m_w": m_w, "m_vasito": m_vasito}, index=materiales)

# Cálculos adicionales
df["d_avg"] = [abs(d1[i] + d2[i]) / 2 for i in range(len(d1))]
df["A"] = [np.pi * (df["d_avg"][i] / 2) ** 2 for i in range(len(df))]
df["Ra"] = [df["m_wa"][i] / df["ta"][i] for i in range(len(df))]
df["R"] = [df["m_w"][i] / df["t"][i] for i in range(len(df))]
df["Ro"] = [df["R"][i] - df["Ra"][i] for i in range(len(df))]

# Cálculo de la conductividad térmica (k)
diferencial_temperatura = 100  # °C
df["k"] = (df["m_wa"] * 80 * df["d_avg"]) / (df["A"] * df["ta"] * diferencial_temperatura)

# Visualizar el DataFrame con los resultados
print(df[["d1", "d2", "d_avg", "A", "ta", "m_wa", "m_w", "Ra", "R", "Ro", "k"]])
