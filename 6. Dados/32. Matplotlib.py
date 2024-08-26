# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Matplotlib em Python

Este arquivo apresenta diversos exemplos do uso da biblioteca Matplotlib em Python para criação de gráficos.

Certifique-se de ter o Matplotlib instalado usando o seguinte comando:
pip install matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

# Exemplo 1: Gráfico de Linha Simples
def exemplo_grafico_linha_simples():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='sen(x)')
    plt.title('Gráfico de Linha Simples')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo 2: Gráfico de Dispersão
def exemplo_grafico_dispersao():
    np.random.seed(42)
    x = np.random.rand(50)
    y = np.random.rand(50)

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='blue', label='Pontos Aleatórios')
    plt.title('Gráfico de Dispersão')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo 3: Gráfico de Barras
def exemplo_grafico_barras():
    categorias = ['A', 'B', 'C', 'D', 'E']
    valores = [20, 35, 30, 25, 40]

    plt.figure(figsize=(8, 5))
    plt.bar(categorias, valores, color='green', alpha=0.7)
    plt.title('Gráfico de Barras')
    plt.xlabel('Categorias')
    plt.ylabel('Valores')
    plt.grid(axis='y')
    plt.show()

# Exemplo 4: Gráfico de Pizza
def exemplo_grafico_pizza():
    categorias = ['A', 'B', 'C', 'D', 'E']
    valores = [20, 35, 30, 25, 40]

    plt.figure(figsize=(8, 5))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink'])
    plt.title('Gráfico de Pizza')
    plt.show()

# Exemplo 5: Gráficos Múltiplos
def exemplo_graficos_multiplos():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(x, y1, label='sen(x)', color='blue')
    plt.title('Gráficos Múltiplos')
    plt.ylabel('sen(x)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(x, y2, label='cos(x)', color='red')
    plt.xlabel('Eixo X')
    plt.ylabel('cos(x)')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Exemplo 6: Gráfico de Linhas com Marcadores
def exemplo_grafico_linhas_marcadores():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='sen(x)', marker='o', linestyle='--', color='purple')
    plt.title('Gráfico de Linhas com Marcadores')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Executar os Exemplos
if __name__ == "__main__":
    exemplo_grafico_linha_simples()
    exemplo_grafico_dispersao()
    exemplo_grafico_barras()
    exemplo_grafico_pizza()
    exemplo_graficos_multiplos()
    exemplo_grafico_linhas_marcadores()
