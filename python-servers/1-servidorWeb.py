from socket import *

# --- Configurações do Servidor ---
meuHost = ''
minhaPorta = 8080

# Cria o objeto socket do servidor
sockobj = socket(AF_INET, SOCK_STREAM)
orig = (meuHost, minhaPorta)

try:
    sockobj.bind(orig)
    sockobj.listen(1)

    print(f'Servidor Web pronto na porta {minhaPorta}...')

    while True:
        conn, cliente = sockobj.accept()
        print('Conexão aceita de:', cliente)

        # Recebe a requisição HTTP (não a usamos, mas é necessário para o protocolo)
        request = conn.recv(1024)
        print('Requisição recebida:\n', request.decode())

        # --- Constrói a Resposta HTTP ---
        
        # 1. Linha de Status
        status_line = "HTTP/1.1 200 OK\r\n"
        
        # 2. Cabeçalhos
        header = "Content-Type: text/html\r\n\r\n"
        
        # 3. Corpo da Resposta: Lê o conteúdo do arquivo HTML
        try:
            with open('index.html', 'r', encoding='utf-8') as arquivo_html:
                html_content = arquivo_html.read()
        except FileNotFoundError:
            html_content = "<h1>Erro 404: Arquivo nao encontrado</h1>"
            print("Erro: O arquivo index.html nao foi encontrado.")
            
        # --- Envia a Resposta Completa ---
        response = (status_line + header + html_content).encode('utf-8')
        conn.send(response)
        
        # Fecha a conexão após enviar a resposta
        conn.close()
        print('Conexão com', cliente, 'finalizada.')

except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    sockobj.close()