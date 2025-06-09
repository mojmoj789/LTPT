import socket
import random

def sinh_mang_so_nguyen(n=2):
    return [str(random.randint(1, 100)) for _ in range(n)]

HOST = '192.168.70.157' 
PORT = 23456

mang = sinh_mang_so_nguyen()
print(mang)
chuoi_gui = ' '.join(mang) 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.sendall(chuoi_gui.encode('utf-8')) 
du_lieu = client_socket.recv(1024).decode('utf-8')  

print("Kết quả từ server:", du_lieu)

client_socket.close()