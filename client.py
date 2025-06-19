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
