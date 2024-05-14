from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Na importação abaixo vamos setar como vamos selecionar este elemento
from selenium.webdriver.common.by import By 
import time  # Importa o módulo time

# Instala o ChromeDriver automaticamente
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.hashtagtreinamentos.com/todos-os-cursos')

# Localizando pelo XPATH
navegador.find_element(By.XPATH, '//*[@id="menu-item-30499"]/a').click()
time.sleep(5)
navegador.find_element(By.XPATH, '//*[@id="menu-item-30799"]/a').click()
time.sleep(5)
navegador.find_element(By.XPATH, '/html/body/header/a/img').click()

# Aguarda uma entrada do usuário antes de terminar
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador
navegador.quit()