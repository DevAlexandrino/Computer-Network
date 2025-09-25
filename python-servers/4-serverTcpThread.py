import threading
from socket import *

# --- Configurações do Servidor ---
meuHost = '' # aceita conexões de qualquer endereço de ip
minhaPorta = 5001 # porta nao reservada

# Cria o objeto socket para o servidor
sockobj = socket(AF_INET, SOCK_STREAM) #cria o objeto socket
orig = (meuHost, minhaPorta) #cria uma tupla com o host e a porta

# --- Função para tratar a conexão do cliente ---
# Esta função será executada em uma thread separada para cada cliente
def handle_cliente(conn, cliente): # recebe o socket do cliente e o endereço de ip
    print(f'Conectado por: {cliente}')
    try:
        while True:
            recvMsg = conn.recv(1024) # tamanho do buffer
            # Interrompe quando receber ctrl-X (b'\x18') ou a conexão for fechada
            if recvMsg == b'\x18' or not recvMsg:
                print(f'Finalizando conexão do cliente: {cliente}')
                break
            print(f'[{cliente[0]}:{cliente[1]}] {recvMsg.decode()}') # imprime a mensagem recebida
    finally:
        # Garante que o socket do cliente será fechado, mesmo em caso de erro
        conn.close()

# --- Loop principal do Servidor ---
def servidor_main():
    try:
        sockobj.bind(orig) # associa o socket ao host e porta
        sockobj.listen(5)  # Aumenta o número de conexões na fila para 5

        print('Servidor pronto para aceitar conexões...')

        while True:
            # Aceita uma nova conexão
            conn, cliente = sockobj.accept()
            # Cria e inicia uma nova thread para lidar com o cliente
            cliente_thread = threading.Thread(target=handle_cliente, args=(conn, cliente,))
            cliente_thread.daemon = True  # Permite que a thread seja encerrada junto com o programa principal
            cliente_thread.start()

    except Exception as e:
        print(f"Ocorreu um erro no servidor: {e}")
    finally:
        # Garante que o socket do servidor será fechado quando o programa principal terminar
        sockobj.close()

# --- Inicia o Servidor ---
if __name__ == "__main__":
    servidor_main()