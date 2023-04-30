import Neo
import multiprocessing as mp
import numpy as np

def client_proc():
    comm = Neo.Neo()
    comm.connect_client(IP='192.168.0.4')
    comm.send_data(["Hey!",np.random.random((100,100))])
    print(comm.receive_data()) 

if __name__ == '__main__':
    client = mp.Process(target=client_proc, args=())
    client.start()