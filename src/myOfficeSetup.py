from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

urls = [
    "https://web.whatsapp.com/",
    "https://discord.com/",
    "https://www.gmail.com",
    "https://trello.com/",
    "https://huggingface.co/",
]

navegador = webdriver.Chrome()

# Abrindo a primeira aba
navegador.get(urls[0])

# Abrindo as demais abas
for url in urls[1:]:
    # Criando uma nova aba
    navegador.execute_script("window.open('');")
    # Mudando para a nova aba
    navegador.switch_to.window(navegador.window_handles[-1])
    # Carregando o próximo URL
    navegador.get(url)
    time.sleep(1)  # pausa de 1 segundo entre as abas

# Mantendo o navegador aberto
while True:
    pass