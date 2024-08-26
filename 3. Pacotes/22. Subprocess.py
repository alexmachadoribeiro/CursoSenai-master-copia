# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Módulo subprocess em Python para Windows

Este arquivo demonstra o uso do módulo subprocess em Python para execução de comandos no terminal do Windows.

1. Executando um Comando Simples
2. Capturando a Saída do Comando
3. Trabalhando com Entrada de Dados
"""

import subprocess

print("1. Executando um Comando Simples:")
# Executando o comando "dir" no Windows
subprocess.run(["dir"], shell=True)  # O parâmetro shell indica que o comando será executado no terminal do Windows
