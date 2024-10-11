from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

urls = [
    "https://web.whatsapp.com/",
    "https://discord.com/login",
    "https://www.gmail.com",
    "https://trello.com/login",
    "https://huggingface.co/chat/",
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

# Encerrando o programa, mas mantendo as abas abertas
os._exit(0)