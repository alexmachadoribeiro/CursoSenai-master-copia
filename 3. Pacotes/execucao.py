from pacote_shutil import VerificacaoArquivos
import shutil
import time
import os


nome_raiz = "Downloads"
verificacao = VerificacaoArquivos()

pastas_principal = verificacao.leitura_downloads(diretorio="Downloads")
# print(pastas_principal)

for subpasta in pastas_principal:
    sub_diretorio = f"{nome_raiz}/{subpasta}"
    itens_subpasta = verificacao.leitura_downloads(sub_diretorio)
    # print(itens_subpasta)

    for arquivo in itens_subpasta:
        item = f"{sub_diretorio}/{arquivo}"
        nome_arquivo = arquivo
        conteudo = verificacao.leitura_arquivo(item)

        infectado = verificacao.antivirus(conteudo)
        if infectado:
            print(f"Resultado da análise do antivírus no arquivo {item} foi {infectado}")
            shutil.move(item, f"Quarentena/{nome_arquivo}")
            print("Arquivo movido para Quarentena")

time.sleep(2)

try:
    shutil.rmtree("Quarentena")
    print("Arquivos infectados excluídos com sucesso")
except Exception as e:
    print(f"Houve um erro durante a exclusão: {e}")
else:
    print(f"Exclusão bem sucedida dos arquivos infectados")

time.sleep(2)
os.mkdir("Quarentena")
