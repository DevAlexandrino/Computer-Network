from socket import *

# --- Configurações do Cliente ---
meuHost = '127.0.0.1'
minhaPorta = 5001

# Cria o objeto socket do cliente
sockobj = socket(AF_INET, SOCK_STREAM)
dest = (meuHost, minhaPorta)

try:
    sockobj.connect(dest)
    print('Conectado ao servidor de eco. Para sair, use CTRL+X\n')
    
    msg = ''
    while msg != '\x18':
        msg = input()
        
        # Envia a mensagem para o servidor
        sockobj.send(msg.encode())
        
        # Recebe a resposta (eco) do servidor
        recvMsg = sockobj.recv(1024)
        
        # Imprime a mensagem recebida de volta
        print(f"Eco do Servidor: {recvMsg.decode()}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    sockobj.close()