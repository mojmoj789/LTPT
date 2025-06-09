import socket

def xu_ly_mang(mang):
    try:
        return str(sum(int(x) for x in mang))
    except ValueError:
        return "Dữ liệu không hợp lệ."

HOST = '0.0.0.0'
PORT = 23456

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

while True:
    conn, addr = server_socket.accept()
    data = conn.recv(10240).decode('utf-8')
    mang = data.strip().split()
    ket_qua = xu_ly_mang(mang)
    conn.sendall(ket_qua.encode('utf-8'))
    conn.close()