from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
import config


def iniciar_driver():
    chrome_oprions = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_oprions.add_argument(argument)

    # Uso de configurações experimentais
    chrome_oprions.add_experimental_option('prefs', {
        # Desabilitar a configuração de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_oprions)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )
    return driver, wait


driver, wait = iniciar_driver()

while True:
    # ENTRAR NO INSTAGRAM
    driver.get('https://www.instagram.com/')
    sleep(3)
    # CLICAR E DIGITAR O USUARIO
    campo_usuario = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
    campo_usuario.send_keys(config.usuario)
    sleep(3)
    # CLICAR E DIGITAR A SENHA
    campo_senha = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
    campo_senha.send_keys(config.senha)
    sleep(3)
    # CLICAR NO CAMPO ENTRAR
    botao_entrar = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='_acan _acap _acas "
                                                               "_aj1-']")))
    botao_entrar.click()
    sleep(10)
    # NAVEGAR NA URL DA PAGINA DESEJADA
    driver.get('https://instagram.com/devaprender')
    sleep(3)
    # CLICAR NA ULTIMA POSTAGEM
    postagens = wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, "//div[@class='_aagu']")))
    sleep(5)
    postagens[0].click()
    sleep(5)
    # VERIFICAR SE A POSTAGEM FOI CURTIDA, CASO NÃO TENHA SIDO, CLICAR EM CURTIR
    elementos_postagem = wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, "//div[@class='_abm0 _abl_']")))
    if len(elementos_postagem) == 7:
        elementos_postagem[1].click()
        sleep(86400)
    # CASO JA TENHA SIDO, AGUARDAR 24 HORAS
    else:
        print('postagem ja curtida!')
        sleep(86400)

