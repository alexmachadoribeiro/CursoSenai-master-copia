# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Selenium em Python

Este arquivo apresenta vários exemplos do uso do Selenium em Python para automação de interações com páginas web.

Certifique-se de ter o Selenium instalado usando o seguinte comando:
pip install selenium
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Exemplo 1: Abrindo um Navegador e Acessando uma Página
def exemplo_abrir_navegador():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    print("Página aberta com sucesso!")
    driver.quit()


# Exemplo 2: Preenchendo um Formulário
def exemplo_preencher_formulario():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com/form")

    input_nome = driver.find_element(By.NAME, "nome")
    input_nome.send_keys("John Doe")

    input_email = driver.find_element(By.NAME, "email")
    input_email.send_keys("john.doe@example.com")

    btn_enviar = driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_enviar.click()

    print("Formulário preenchido e enviado com sucesso!")
    driver.quit()


# Exemplo 3: Interagindo com Elementos Dinâmicos
def exemplo_interacao_elementos_dinamicos():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com/dynamic_elements")

    try:
        elemento_dinamico = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "elemento-dinamico"))
        )
        print("Elemento dinâmico encontrado:", elemento_dinamico.text)
    finally:
        driver.quit()


# Exemplo 4: Trabalhando com Frames
def exemplo_trabalhar_com_frames():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com/frames")

    # Mudar para um frame usando o índice (0 ou 1)
    driver.switch_to.frame(0)

    # Realizar ações dentro do frame
    input_no_frame = driver.find_element(By.ID, "input-no-frame")
    input_no_frame.send_keys("Texto no frame!")

    # Voltar para o contexto padrão
    driver.switch_to.default_content()

    # Mudar para outro frame usando o nome
    driver.switch_to.frame("nome-do-frame")

    print("Texto no segundo frame:", driver.find_element(By.ID, "texto-no-frame").text)

    driver.quit()


# Exemplo 5: Executando JavaScript
def exemplo_executar_javascript():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

    # Executar JavaScript para rolar a página até o final
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.quit()


# Exemplo 6: Capturando Screenshots
def exemplo_capturar_screenshot():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    driver.save_screenshot("screenshot.png")
    print("Screenshot salvo com sucesso!")
    driver.quit()


# Exemplo 7: Trabalhando com Cookies
def exemplo_trabalhar_com_cookies():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

    # Adicionar um cookie
    novo_cookie = {"name": "exemplo_cookie", "value": "123"}
    driver.add_cookie(novo_cookie)

    # Imprimir todos os cookies
    cookies = driver.get_cookies()
    print("Cookies:", cookies)

    driver.quit()


# Exemplo 8: Realizando uma Busca no Google
def exemplo_realizar_busca_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    # Encontrar o campo de pesquisa e enviar uma consulta
    campo_pesquisa = driver.find_element(By.NAME, "q")
    campo_pesquisa.send_keys("Python Selenium example")
    campo_pesquisa.send_keys(Keys.RETURN)

    print("Resultados da busca exibidos!")
    driver.quit()


# Executar os Exemplos
if __name__ == "__main__":
    exemplo_abrir_navegador()
    exemplo_preencher_formulario()
    exemplo_interacao_elementos_dinamicos()
    exemplo_trabalhar_com_frames()
    exemplo_executar_javascript()
    exemplo_capturar_screenshot()
    exemplo_trabalhar_com_cookies()
    exemplo_realizar_busca_google()
