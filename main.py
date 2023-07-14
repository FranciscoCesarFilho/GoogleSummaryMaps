# GoogleSummaryMaps - Projeto para o Youtube
from selenium import webdriver # importando webdriver
from selenium.webdriver.common.by import By # importando a classe dos elementos da pagina
import drivers # importando os drivers
import time # importando s biblioteca para o Time
import SkillSpeak_TTS


def result_speak(text):
    engine = SkillSpeak_TTS.init() # criando o objeto engine
    voices = engine.getProperty('voices')       # pegando uma lista de vozes
    engine.setProperty('voice', voices[0].id)  # definindo a voz padrão do sistema operacional
    rate = engine.getProperty('rate')   # pegando a velocidae da voz            
    engine.setProperty('rate', rate-50) # definindo a velocidade da voz
    print(f"Result: {text}") # mostrando o resultado
    engine.speak(text) # falando o resultado
    engine.start() # iniciando a voz


def main():
    # definindo uma entrada
    query = input("Digite o nome da cidade ou país: ")

    # instalando o chromedriver se não existir
    drivers.install()

    # Inicializar o navegador
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/maps/search/{query}")

    # Aguardar o resultado ser carregado
    driver.implicitly_wait(5)

    # acessando o resultado completo
    driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div/span/button').click()
    time.sleep(3)

    # extraindo o resultado acessado
    resumo = driver.find_element(By.CLASS_NAME, "wEvh0b").text
    resumo = resumo.replace(". ", ", ")

    print(resumo) # exibindo o resultado

    # encerrando a pesquisa
    driver.quit()

# inicia a função principal do programa
if __name__ == "__main__":
    main()