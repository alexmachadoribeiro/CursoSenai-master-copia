from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime as dt

import pandas as pd
pd.options.display.width = 0


class MegaLeiloes:
    def __init__(self, limite_pg=0):
        self.dados = []
        self.limite_pg = limite_pg

    def captura(self):
        print("<<< Automação da Mega Leilões >>>")
        # FIXME: O parâmetro tipo%5B0%5D=1&tipo%5B1%5D=2 designa que somente serão buscados imóveis do tipo judicial
        url = "https://www.megaleiloes.com.br/imoveis/?tov=igbr&tipo%5B0%5D=1&pagina="

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Sem abertura do navegador
        options.add_argument("start-maximized")  # Início maximizado
        options.add_argument("--no-sandbox")  # Tratativa do erro DevToolsActivePort file doesn't exist
        options.add_argument("--disable-dev-shm-usage")  # Tratativa do erro DevToolsActivePort file doesn't exist
        # options.add_argument("--disable-blink-features=AutomationControlled") # Previne detecção do Selenium

        # Inicialização
        driver = webdriver.Chrome(options=options)
        driver.get(url + "1")

        # Identifica a quantidade de páginas
        qtd_pg = None

        try:
            qtd_pg = driver.find_element(By.XPATH,
                                         "/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/div/b[4]").text
            print("Quantidade de páginas: ", qtd_pg)
            existem_elementos = 1

        except:
            existem_elementos = 0

        if not existem_elementos:
            print("Não existem elementos para serem capturados.")

        elif existem_elementos:
            for i in range(1, int(qtd_pg) + 1):
                print(f"<<< Acessando página {i}")

                # Verificando limite
                if i > self.limite_pg:
                    break

                print(url + str(i))
                driver.get(url + str(i))

                # Acesse o data-key de cada card e com base nele busque os dados
                cards = driver.find_elements(By.XPATH, '//*[@class="col-sm-6 col-md-4 col-lg-3"]')
                for i, card in enumerate(cards):
                    data_key = card.get_attribute('data-key')
                    try:
                        titulo = driver.find_element(By.XPATH,
                                                     f'//*[@data-key="{data_key}"]//a[@class="card-title"]').text
                        print("Título: ", titulo)
                    except:
                        titulo = ""

                    try:
                        status = driver.find_element(By.XPATH,
                                                     f'//*[@data-key="{data_key}"]//div[@class="card-status"]').text
                    except:
                        status = ""

                    # Traz o valor ativo: quando a 1ª praça expira, retorna o valor da 2ª
                    try:
                        valor = driver.find_element(By.XPATH,
                                                    f'//*[@data-key="{data_key}"]//div[@class="card-price"]').text
                    except:
                        valor = "0"

                    try:
                        dados2 = driver.find_element(By.XPATH,
                                                     f'//*[@data-key="{data_key}"]//div[@class="instance active"]').text
                        dados2 = dados2.replace("\n", " ")
                    except:
                        dados2 = ""

                    try:
                        localidade = driver.find_element(By.XPATH,
                                                         f'//*[@data-key="{data_key}"]//a[@class="card-locality"]').text
                    except:
                        localidade = ""

                    try:
                        tipo = driver.find_element(By.XPATH,
                                                   f'//*[@data-key="{data_key}"]//div[@class="card-instance-title"]').text
                        tipo = tipo.split()[0]
                    except:
                        tipo = ""

                    try:
                        href = driver.find_element(By.XPATH,
                                                   f'//*[@data-key="{data_key}"]//div[@class="card open"]//div[@class="card-content"]//div[@class="wrap"]//a[@class="card-title"]')
                        link = href.get_attribute('href')

                    except:
                        try:
                            href = driver.find_element(By.XPATH,
                                                       f'//*[@data-key="{data_key}"]//div[@class="card waiting"]//div[@class="card-content"]//div[@class="wrap"]//a[@class="card-title"]')
                            link = href.get_attribute('href')
                        except:
                            link = ""

                    # Só é definido se a 1ª praça já tiver expirado (-----------)
                    try:
                        _1instancia_expirada = driver.find_element(By.XPATH,
                                                                   f'//*[@data-key="{data_key}"]//div[@class="instance first passed"]//span[@class="card-instance-value"]').text
                    except:
                        _1instancia_expirada = ""

                    try:
                        valor2 = driver.find_element(By.XPATH,
                                                     f'//*[@data-key="{data_key}"]//div[@class="instance active"]//span[@class="card-instance-value"]').text
                    except:
                        valor2 = ""

                    try:
                        dados1_expirada = driver.find_element(By.XPATH,
                                                              f'//*[@data-key="{data_key}"]//div[@class="instance first passed"]//span[@class="card-first-instance-date"]').text
                    except:
                        dados1_expirada = ""

                    try:
                        dados1_ativa = driver.find_element(By.XPATH,
                                                           f'//*[@data-key="{data_key}"]//div[@class="instance first active"]//span[@class="card-first-instance-date"]').text
                    except:
                        dados1_ativa = ""

                    # Imprimir todos os dados capturados para cada card
                    print(f"""\nCARD {i} - título: {titulo}, status: {status}, valor: {valor}, dados2: {dados2},
                     localidade: {localidade}, tipo: {tipo}, link: {link}, 1ª instância expirada: {_1instancia_expirada}
                     , valor 2ª instância: {valor2}, dados 1ª instância expirada: {dados1_expirada},
                      dados 1ª instância ativa: {dados1_ativa}""")

                    # Construir lista com os dados capturados
                    self.dados.append([titulo, status, valor, dados2, localidade, tipo, link, _1instancia_expirada, valor2, dados1_expirada, dados1_ativa])

            driver.close()
            print()

    def salvar(self):
        print("<<< Salvando os dados capturados >>>")
        # Salvar os dados capturados em um arquivo CSV
        df = pd.DataFrame(self.dados, columns=["Título", "Status", "Valor", "Dados 2", "Localidade", "Tipo", "Link", "1ª Instância Expirada", "Valor 2ª Instância", "Dados 1ª Instância Expirada", "Dados 1ª Instância Ativa"])
        df.to_excel("dados_megaleiloes.xlsx", index=False)
        print("Dados salvos com sucesso!")


if __name__ == "__main__":
    ml = MegaLeiloes(limite_pg=1)
    ml.captura()
    ml.salvar()