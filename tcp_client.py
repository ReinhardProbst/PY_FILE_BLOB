"""
TCP Client

TCP Client
"""


##------------------------------------------------------------
_AUTHOR    = 'RP'
_VERSION   = '0.5.0'
_COPYRIGHT = '(c) 2024'

_ABOUT = _AUTHOR + '  v' + _VERSION + '   ' + _COPYRIGHT
##------------------------------------------------------------


import socket


class TCPClient:
    def __init__(self, ip_addr, port, bufsize, diag = False):
        self.ip_addr = ip_addr
        self.port    = port
        self.bufsize = bufsize
        self.diag    = diag

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        if self.diag:
            print("Create tcp socket\n")

    def __del__(self):
        self.sock.close()

    def connect(self, init = b""):
        self.sock.connect((self.ip_addr, self.port))
        if self.diag:
            print(f"Connected to server {self.ip_addr}/{self.port}\n")
        if len(init) > 0:
            self.sock.send(init)

    def receive(self):
        return self.sock.recv(self.bufsize)

    def close(self):
        self.sock.close()

