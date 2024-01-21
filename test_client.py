import Neo
import multiprocessing as mp
import numpy as np

def client_proc():
    comm = Neo.Neo()
    comm.connect_client(IP='127.0.0.0')
    comm.send_data(["Hey from the client!!",np.random.random((100,100))])
    print(comm.receive_data())
    comm.close_conn()

if __name__ == '__main__':
    client = mp.Process(target=client_proc, args=())
    client.start()