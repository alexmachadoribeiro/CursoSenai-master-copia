# A variável paginas é uma lista de strings que representam páginas de um livro.
# O primeiro caracter de cada string é o número da página.
# Percorra todas as páginas procurando pela palavra "aplicações" e informe o número da página correspondente
# Informe também a posição da palavra "aplicações" na página

# Depois de obtida a posição de "aplicações", saía do loop
# Acesse a página na qual foi encontrada a palavra (palavra[n])
# Descubra a posição inicial e final da palavra "aplicações" na página
# E utilizando a notação de substring imprima a palavra "aplicações"

# Dica: Use a posição e o tamanho de "aplicações"

paginas = [
    """1 Este é um texto sobre microserviços em python""",
    """2 Microserviços são uma abordagem de arquitetura de software que estrutura uma aplicação como uma coleção de 
    serviços""",
    """3 Cada serviço é construído em torno de uma capacidade de negócios, sendo um serviço autônomo""",
    """4 Eles podem ser implementados, escalados e gerenciados independentemente""",
    """5 Pode ser uma boa abordagem para aplicações empresariais""",
         ]

pagina_find = 0
posicao_find = 0
palavra = "aplicações"
for n in range(len(paginas)):
    if "aplicações" in paginas[n]:
        pagina_find = n
        posicao_find = paginas[n].find("aplicações")
        break

print(f"A palavra 'aplicações' foi encontrada na página {pagina_find + 1} na posição {posicao_find + 1}")

print(paginas[pagina_find][posicao_find:posicao_find + len(palavra)])