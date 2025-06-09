from xmlrpc.server import SimpleXMLRPCServer

def X(mang):
    try:
        print(mang)
        numbers = [int(x) for x in mang]

        if not numbers:
            return "Mảng rỗng."

        avg = sum(numbers) / len(numbers)
        print("avg=",avg)
        return f"{avg:.2f}"
    except ValueError:
        return "Dữ liệu không hợp lệ."

server = SimpleXMLRPCServer(("0.0.0.0", 9999), allow_none=True)
server.register_function(X, "X")

print("RPC Server đang chạy trên cổng 9999...")
server.serve_forever()