from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Na importação abaixo vamos setar como vamos selecionar este elemento
from selenium.webdriver.common.by import By 

# Instala o ChromeDriver automaticamente
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.hashtagtreinamentos.com/todos-os-cursos')

#Para selecionar um elemento dentro de uma página html por exemplo, temos duas opções:
#navegador.find_element ou (retorna um único item)
#navegador.find_elements (retorna uma lista de itens)

# Localizei um elemento com o id firstname e salvei em uma variável
campo_nome = navegador.find_element(By.ID, 'firstname')
# Acessei a variável e setei o nome, de acordo a instrução do formulário 
campo_nome.send_keys('Tiago') 

# Localizei um elemento com o id firstname e desta vez não salvei em uma variável,
# mas sim setei o email no momento em que o elemento foi localizado
navegador.find_element(By.ID, 'email').send_keys('tiagosantos@gmail.com')

# Para o botão podemos selecionar através do nome da classe e solicitar o click após a localização
navegador.find_element(By.CLASS_NAME, 'botao-formulario-newsletter').click()

# Aguarda uma entrada do usuário antes de terminar
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador
navegador.quit()
