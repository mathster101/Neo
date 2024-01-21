import Neo
import multiprocessing as mp
import numpy as np
import time 
import sys

def server_proc():
    comm = Neo.Neo()
    comm.start_server()
    comm.get_new_conn()
    start = time.time()
    data = comm.receive_data()
    end = time.time()
    print(data[0])
    size = sys.getsizeof(data)
    print(size / (end - start))
    comm.send_data("hello from the server!!")
    comm.close_conn()
    

if __name__ == '__main__':
    server = mp.Process(target=server_proc, args=())
    server.start()
    print("server online")