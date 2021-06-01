import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 10000))
sock.listen(1)
connections = []


def mfcc_predict(num_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
    return


def handler(c, a):
    global connections
    while True:
        data = c.recv(1024)
        print(data)
        # do smth with model
        c.send("hello this is the server".encode('utf-8'))
        if not data:
            connections.remove(c)
            c.close()
            break


while True:
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)
