# Comunicacao_Client-Server_em_Python
## Tecnologias

- Socket
    
    Socket é um módulo, ou biblioteca em python, utilizada para criar servidores e clientes que podem comunicar-se entre si. Socket (ou, em português, soquete) é um procedimento em redes de computadores que estabelece conexão entre dois dispositivos ou mais. É um canal de comunicação entre computadores. Ele funciona a partir da aplicação de protocolos de comunicação de rede, que é o TCP (mais seguro) ou UDP (mais rápido).
    

## Programação

```python
import socket

host = '127.0.0.1' # Esse endereço IP é do localhost. Ou seja, estou estabelecendo uma rede local ou intranet
porta = 8800 # Essa é a porta de acesso que o cliente terá para comunicar-se com meu servidor
```

Tanto o servidor quanto o cliente precisam ter o mesmo valor de HOST e PORTA para que haja conexão.

Dando continuidade ao código…

```python
""" Na linha abaixo, o comando AF_INET está criando uma conexão entre
endereços IP, determinando a porta de acesso que será usada.
O comando SOCK_STREAM está definindo que a comunicação será baseada no
protocolo TCP. Ou seja, será uma comunicação mais pesada, porém com maior
segurança e controle de erros. """
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" Nas duas linhas consecutivas, estou atribuindo a uma variável uma tupla
com o host e a porta definidas anteriormente (127.0.0.1, 8800). Depois,
estou associando o socket ao host e á porta, para que quando qualquer
dispositivo estiver procurando esse endereço, "chamando" o endereço do
servidor para uma conexão, o servidor "ouça" ou identifique o "chamado"
e estabelça a conexão clietne-servidor. """
recebe = (host, porta)
soquete.bind(recebe)
soquete.listen(2) # O socket aceita duas conexões simultâneas, mas é possível aumentar.

print('\nSERVIDOR INICIADO...IP:', host, 'PORTA:', porta)

"""O loop abaixo rodará infinitamente, mantendo a conexão com o cliente,
até que algum fator interrompa essa conexão (termine comunicação, faça o
loop parara de rodar)."""
while True:
    conexao, enderecoIP = soquete.accept() # Criando duas variáveis que vai receber e aceitar a conexão do cliente. Uma delas conterá o IP do cliente.
    print('\nSERVIDOR ACESSADO PELO CLIENTE:', enderecoIP)

    # Criamos um loop que rodará eternamente, responsável por receber as mensagens do cliente
    while True:
        """A variável mensagem receberá, como o próprio nome diz, a mesagem
        enviada pelo cliente. A variável conexao, graças ao valor que recebeu
        no momento em que a conexão foi criada, possui um método que irá
        receber mensagens de até 2kb, conforme passado como argumento entre
        os parênteses [.recv(2048)]."""
        mensagem = conexao.recv(2048)

        if not mensagem: # Caso não recebe nenhuma mensagem, o loop será interrompido, parando a conexão
            break
        print('\nIP CLIENTE:', enderecoIP)
        print('MENSAGEM RECEBIDA:', mensagem.decode())

    print('CONEXÃO FINALIZADA...', enderecoIP)
    conexao.close()
```

Essa é a conclusão do código do servidor.

O código do cliente é o seguinte:

```python
import socket

host = '127.0.0.1'
porta = 8800

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
envio = (host, porta)
soquete.connect(envio)

print('Digite S e pressione ENTER caso queira encerrar')
print('Digite a mensagem:')
mensagem = input()

# Enquanto o valor de mensagem for diferente da letra S (seja maiúscula ou minúscula), a conexão permanecerá (através do loop)
while mensagem not in ('s', 'S'):
    soquete.send(str(mensagem).encode()) # Encriptando a mensagem e enviando-a pela rede, garantindo que esteja no formato string
    mensagem = input() # Abre um input novamente para recebimento da mensagem

soquete.close()
```

Ambos os códigos são escritos em arquivos diferentes. O primeiro a ser executado é o do servidor, até porque sem ele, o cliente não tem como enviar mensagem. Após o servidor ser executado e posteriormente, o cliente também, será possível enviar mensagens pelo cliente e visualizá-las pelo servidor. Claro que, por se tratar do localhost, as únicas mensagens recebidas serão vindas do próprio computador.
