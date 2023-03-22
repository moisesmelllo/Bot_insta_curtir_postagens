from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


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
    drivers = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_oprions)
    return drivers


driver = iniciar_driver()

driver.get('https://www.facebook.com/')
sleep(5)
email = driver.find_element(By.ID, 'email')
senha = driver.find_element(By.ID, 'pass')

sleep(5)
email.send_keys(Config.email)
sleep(5)
senha.send_keys(Config.password)
sleep(5)
senha.send_keys(Keys.ENTER)
sleep(5)
campo_status = driver.find_element(By.XPATH, "//div[@class='x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe xi81zsa']")
sleep(3)
campo_status.click()
sleep(5)
campo_publicacao = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
sleep(5)
campo_publicacao.click()
sleep(5)
campo_publicacao.send_keys('Testando automação!')
sleep(5)
botao_publicar = driver.find_element(By.XPATH, "//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 "
                                               "xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l "
                                               "x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
sleep(5)
botao_publicar.click()
input('')
driver.close()
