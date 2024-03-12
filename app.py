from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dados import *
import random
import string
def iniciar_driver():
    # Cria uma instância de ChromeOptions para configurar várias opções do navegador Chrome
    chrome_options = Options()

    # Define uma lista de argumentos de linha de comando a serem passados para o navegador Chrome
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--incognito']

    # Adiciona cada argumento ao ChromeOptions
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Adiciona opções experimentais ao ChromeOptions usando o dicionário 'prefs'
    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_values.automatic_downloads': 1,
    })

    # Usa o ChromeDriverManager para baixar e instalar automaticamente o ChromeDriver apropriado
    # Cria uma instância do webdriver Chrome com o serviço e as opções configuradas
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Retorna a instância do driver para que possa ser usada no restante do código
    return driver

driver = iniciar_driver()

driver.get('https://twitter.com/')
def logar(passw,email,user):
    #essa função pega seu login, senha e usuario e insere nos campos fornecidso.
    try:
        signin = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Entrar']")))
        signin.click()

        email_campo = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.NAME,'text')))
        email_campo.send_keys(emaill)
    
        next_button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Avançar']")))
        next_button.click()
        
        user_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME,"text")))
        user_field.send_keys(usuario)
        
        print("Tempo limite excedido ao aguardar por um elemento.")
        next = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Avançar']")))
        next.click()

        password_campo = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,"password")))
        password_campo.send_keys(pw)
    
        #Clicando pra logar na conta.
        Login_button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Entrar']")))
        Login_button.click()

    except TimeoutException:
        print("Tempo limite excedido ao aguardar por um elemento.")



def gerar_mensagem_aleatoria(tamanho=50):
    sujeitos = [
        "Eu", "Você", "Ele", "Ela", "Nós", "Vocês", "Eles",
        "Os cientistas", "A equipe", "Minha família", "Os estudantes",
        "A sociedade", "Os músicos", "Os artistas", "As crianças"
    ]

    verbos = [
        "amo", "gosto de", "odeio", "pratico", "aprendo", "exploro", 
        "compreendo", "descubro", "desenvolvo", "ensino", "inspiro",
        "observo", "compartilho", "crio", "desfruto", "ajudo"
    ]

    objetos = [
        "programação", "música", "esportes", "cozinhar", "ler", 
        "tecnologia", "viagens", "filmes", "matemática", "ciência",
        "história", "arte", "natureza", "amigos", "família", "fotografia"
    ]

    frase_aleatoria = f"{random.choice(sujeitos)} {random.choice(verbos)} {random.choice(objetos)}.\nMensagem gerada por um bot em teste"
    return frase_aleatoria
    


#Chama a função pra logar com senha, usuario etc
logar(email=emaill,passw=pw,user=usuario)

sleep(12)

contador = 0
while contador < 50:
    frase_aleatoria = gerar_mensagem_aleatoria()
    

    driver.get('https://twitter.com/')


    #faz a postagem
    postagem = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")))
    postagem.send_keys(frase_aleatoria)

    botao_postagem = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19u6a5r r-2yi16 r-1qi8awa r-ymttw5 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")))   
    botao_postagem.click()
    sleep(30)
    contador +=1
print(f"Total de mensagem postas é {contador}")
driver.close()
