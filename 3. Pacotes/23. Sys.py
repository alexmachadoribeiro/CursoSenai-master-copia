# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Módulo sys em Python

Este arquivo demonstra o uso do módulo sys em Python.

1. Obtendo Informações do Interpretador Python
2. Manipulando Caminhos do Sistema
3. Ajustando o Caminho de Busca de Módulos
4. Saindo do Programa
"""

import sys

print("1. Obtendo Informações do Interpretador Python:")
# Obtendo a versão do Python
versao_python = sys.version
print(f"Versão do Python: {versao_python}")

# Obtendo a versão detalhada do Python
versao_detalhada = sys.version_info
print(f"Versão Detalhada: {versao_detalhada}")

# Obtendo o caminho para o interpretador Python
caminho_interpretador = sys.executable
print(f"Caminho do Interpretador Python: {caminho_interpretador}")

print("\n2. Manipulando Caminhos do Sistema:")
# Obtendo o caminho do diretório atual
diretorio_atual = sys.path[0]
print(f"Diretório Atual: {diretorio_atual}")

print("\n3. Saindo do Programa:")
# Saindo do programa com código de saída 0 (sem erros)
sys.exit(0)
