# GoogleSummaryMaps - Projeto para o Youtube
from selenium import webdriver # importando webdriver
from selenium.webdriver.common.by import By # importando a classe dos elementos da pagina
import drivers # importando os drivers
import time # importando s biblioteca para o Time

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