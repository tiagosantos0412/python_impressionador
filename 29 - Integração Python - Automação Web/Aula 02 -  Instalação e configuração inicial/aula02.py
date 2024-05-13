"""_Observação_
Aqui vamos importar a função webdriver da biblioteca selenium
Em seguida vamos apontar onde o serviço do chrome driver está armazenado ou instalado.
Por último vamos verificar a versão do navegador Google Chrome e baixar a versão correspondente  do webdriver, que por sua vez irá baixar o arquivo, armazená-lo em cache e aprontar ao serviço o local do arquivo.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)