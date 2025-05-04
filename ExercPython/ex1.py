"""
- Aluno: Pedro Henrique de Sousa Prestes
- N°USP: 15507819
- 19/11/2024
- Atividade 1: Documentação da Função linear_function
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definir a função linear para o fitting
def linear_function(x, a, b):
    """
    Calcula uma função afim.

    Parâmetros:
        x: Variável da função.
        a: Coeficiente angular.
        b: Coeficiente linear.

    Retorno:
        Retorna o valor da função.
    """
    return a * x + b

# Gerar dados
np.random.seed(0)  # Para reprodutibilidade
x = np.linspace(0, 10, 100)  # 100 valores de x entre 0 e 10
#f(x) = a*x + b
y = 2.5 * x + 1.5 + np.random.normal(0, 1, x.size)  # Dados com ruído 

# Fazer o ajuste (fitting) usando SciPy
params, covariance = curve_fit(linear_function, x, y)
a, b = params  # Parâmetros ajustados (coeficientes da reta)

# Função ajustada
y_fit = linear_function(x, a, b)

# Plotar os dados e o ajuste
plt.figure(figsize=(8, 4))
plt.scatter(x, y, label='Dados com ruído', color='blue')
plt.plot(x, y_fit, label= f'Ajuste Linear: y = {a:.2f}x + {b:.2f}', color='red')
plt.title('Ajuste de Curva Linear com SciPy')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()