#Twitter Bot com Selenium

Este é um bot desenvolvido com Selenium para gerar mensagens aleatórias no Twitter.

## Utilização

Antes de começar a utilizar o bot, certifique-se de configurar corretamente o arquivo `dados.py`. Nele, insira suas credenciais de login, usuário e senha do Twitter.

### Configuração

1. Abra o arquivo dados.py.
2. Insira suas credenciais:

´´´
LOGIN = 'seu_login'
USUARIO = 'seu_usuario'
SENHA = 'sua_senha'
´´´


### Como alterar o Looping

contador = 0
while contador < 50: # Aqui você coloca a quantidade de mensagens que você quer que o bot gere.
    frase_aleatoria = gerar_mensagem_aleatoria()
    #Resto do codigo...
