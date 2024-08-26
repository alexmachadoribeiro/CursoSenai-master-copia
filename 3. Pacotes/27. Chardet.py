import chardet

with open('Downloads/Documentos/anotacoes.txt', 'rb') as f:
    result = chardet.detect(f.read())

print(result['encoding'])