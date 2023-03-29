import Neo
import multiprocessing as mp
import numpy as np

def server_proc():
    comm = Neo.Neo()
    comm.start_server()
    comm.get_new_conn()
    print(comm.receive_data())
    comm.send_data("hi")
    

def client_proc():
    comm = Neo.Neo()
    comm.connect_client()
    comm.send_data([1,2,"Hey!",np.zeros((2,2))])
    print(comm.receive_data()) 

if __name__ == '__main__':
    server = mp.Process(target=server_proc, args=())
    client = mp.Process(target=client_proc, args=())
    server.start()
    client.start()
    server.join()
    client.join()