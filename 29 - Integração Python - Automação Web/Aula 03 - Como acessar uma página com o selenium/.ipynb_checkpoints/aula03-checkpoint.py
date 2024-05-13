from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instala o ChromeDriver automaticamente
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.hashtagtreinamentos.com/todos-os-cursos')

# Aguarda uma entrada do usuário antes de terminar
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador
navegador.quit()
