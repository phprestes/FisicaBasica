import math

# Constantes dadas no problema
r = 5.4e11  # distância em metros
M = 8.7e30  # massa da estrela em kg
G = 6.673e-11  # constante gravitacional em m^3 kg^-1 s^-2

# Cálculo do período de translação
T = 2 * math.pi * math.sqrt(r**3 / (G * M))
print(round(T / 1e7, 3))