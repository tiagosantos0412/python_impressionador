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

# selecionando o elemento por uma tag
# vamos capturar o texto dentro do elemento h2
titulo = navegador.find_element(By.TAG_NAME, 'h2').text
print(titulo)

# desta vez vamos selecionar um elemento de acordo com o seu conteúdo do texto de um link, neste caso se o 
# selenium encontrar a palvra WhatsApp, ele irá salvar o número em uam variável
numero_whatsapp = navegador.find_element(By.PARTIAL_LINK_TEXT, 'WhatsApp').text
print(numero_whatsapp)

# Por último vamos selecionar o elemento do formulário com o atributo name
navegador.find_element(By.NAME, 'email').send_keys('tiagosantos@gmail.com')

# Aguarda uma entrada do usuário antes de terminar
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador
navegador.quit()
