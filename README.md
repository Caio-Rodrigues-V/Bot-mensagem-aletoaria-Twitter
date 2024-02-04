#Twitter Bot com Selenium

Este é um bot desenvolvido com Selenium para gerar mensagens aleatórias no Twitter.

## Utilização

Antes de começar a utilizar o bot, certifique-se de configurar corretamente o arquivo `dados.py`. Nele, insira suas credenciais de login, usuário e senha do Twitter.

## Instalando o Selenium:

Você pode instalar o Selenium usando o pip, o gerenciador de pacotes do Python. Execute o seguinte comando no terminal ou prompt de comando:

```pip install selenium```

## Baixando o ChromeDriver:
```
O ChromeDriver é uma ferramenta que permite ao Selenium interagir com o navegador Chrome. Certifique-se de baixar a versão correspondente à versão do Chrome instalada em sua máquina.

Descubra a versão do Chrome:

Abra o Chrome.
No canto superior direito, clique nos três pontos verticais.
Vá para "Ajuda" -> "Sobre o Google Chrome".
Anote a versão do Chrome.
Baixe o ChromeDriver:

Acesse https://sites.google.com/chromium.org/driver/.
Encontre a versão do ChromeDriver correspondente à sua versão do Chrome.
Baixe o arquivo zip correspondente ao seu sistema operacional (por exemplo, chromedriver_win32.zip para Windows).
Extraia o arquivo zip em um local conhecido.
```






### Configuração

1. Abra o arquivo dados.py.
2. Insira suas credenciais:


```
LOGIN = 'seu_login'
USUARIO = 'seu_usuario'
SENHA = 'sua_senha'
```




### Como alterar o Looping

contador = 0
while contador < 50: # Aqui você coloca a quantidade de mensagens que você quer que o bot gere.
    frase_aleatoria = gerar_mensagem_aleatoria()
    #Resto do codigo...
