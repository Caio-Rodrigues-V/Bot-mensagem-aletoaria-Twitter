# Selenium Twitter Bot

Este é um bot desenvolvido com Selenium para gerar mensagens aleatórias no Twitter.

## Utilização

Antes de começar a utilizar o bot, certifique-se de configurar corretamente o arquivo `dados.py`. Nele, insira suas credenciais de login, usuário e senha do Twitter.

### Configuração

1. Abra o arquivo `dados.py`.
2. Insira suas credenciais:
    ```python
    LOGIN = 'seu_login'
    USUARIO = 'seu_usuario'
    SENHA = 'sua_senha'
    ```
3. Salve as alterações.

### Execução

Para executar o bot, basta rodar o script principal. Caso deseje ajustar a quantidade de mensagens a serem enviadas, altere o valor no loop. Você pode fazer isso ajustando o contador no script.

```python
# Exemplo: Alterando para mais de 50 mensagens
for i in range(100):  # Altere o valor para o número desejado
    gerar_mensagem()
    time.sleep(1)  # Adicione um intervalo entre as mensagens, se necessário
