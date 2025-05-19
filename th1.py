import threading
import random
import time

N = 10000
array = [random.randint(1, 1000) for _ in range(N)]
k = 10

max_values = [None] * k
lock = threading.Lock()

def find_max(start, end, thread_id):
    local_max = max(array[start:end])
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    with lock:
        max_values[thread_id] = local_max
        print(f"T({thread_id + 1}) : {local_max} : {timestamp}")
    
threads = []
chunk_size = N // k

for i in range(k):
    start = i * chunk_size
    end = N if i == k - 1 else (i + 1) * chunk_size
    t = threading.Thread(target=find_max, args=(start, end, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

final_max = max(max_values)
print(f"so lon nhat trong mang la: {final_max}")
