"""
- Aluno: Pedro Henrique de Sousa Prestes
- N°USP: 15507819
- 19/11/2024
- Atividade 2: Simulação com Animação do Sistema Massa-Mola
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema_massa_mola(amplitude, fase_inicial, constante_mola, massa, pontos):
    """
    Gera a posição da massa no sistema massa-mola ao longo do tempo.

    Parâmetros:
      amplitude : Deslocamento máximo (em metros).
      fase_inicial : Fase inicial (em radianos).
      constante_mola : Constante da mola (N/m).
      massa : Massa do corpo (kg).
      pontos : Número de amostras para o vetor de tempo.

    Retorna:
      tempos : Array com os instantes de tempo.
      posicoes : Array com as posições correspondentes no movimento.
    """
    # Frequência angular
    omega = np.sqrt(constante_mola / massa)

    # Tempo total para completar um ciclo 
    periodo = (2 * np.pi / omega)
    tempos = np.linspace(0, periodo * 2, pontos)

    # Posições ao longo do tempo
    posicoes = amplitude * np.cos(fase_inicial + omega * tempos)

    return tempos, posicoes

# Parâmetros do sistema
amplitude = 3  # metros
fase_inicial = 0  # radianos
constante_mola = 10  # N/m
massa = 5  # kg
pontos = 100

# Calculando a trajetória
tempos, posicoes = sistema_massa_mola(amplitude, fase_inicial, constante_mola, massa, pontos)

# Configuração da figura
figura, eixo = plt.subplots()
linha, = eixo.plot([], [], color='blue', linewidth=2)

eixo.set_xlim(0, tempos[-1])
eixo.set_ylim(posicoes.min() * 2, posicoes.max() * 2)
eixo.set_xlabel('Tempo (s)')
eixo.set_ylabel('Posição (m)')
eixo.set_title('Movimento Harmônico de um Sistema Massa-Mola')
eixo.grid(True)

def atualizar_animacao(quadro):
    linha.set_data(tempos[:quadro], posicoes[:quadro])
    return linha,

animacao = FuncAnimation(figura, atualizar_animacao, frames=len(tempos), interval=20)
plt.show()
