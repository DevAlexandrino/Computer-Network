from socket import *

# --- Configurações do Servidor ---
meuHost = ''
minhaPorta = 5001

# Cria o objeto socket do servidor
sockobj = socket(AF_INET, SOCK_STREAM)
orig = (meuHost, minhaPorta)

try:
    sockobj.bind(orig)
    sockobj.listen(1)

    print('Servidor de Eco pronto e esperando por conexões...')

    while True:
        conn, cliente = sockobj.accept()
        print('Conectado por:', cliente)

        while True:
            # Recebe a mensagem do cliente
            recvMsg = conn.recv(1024)
            # Se a mensagem for 'Ctrl+X' (b'\x18') ou a conexão for fechada
            if recvMsg == b'\x18' or not recvMsg:
                print('Finalizando conexão do cliente', cliente)
                break
            
            # Mostra a mensagem recebida (opcional, mas bom para depuração)
            print(f"Recebido de {cliente}: {recvMsg.decode()}")
            
            # Envia a mesma mensagem de volta para o cliente
            conn.send(recvMsg)
            
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    conn.close()
    sockobj.close()