"""
UDP Receiver

UDP Receiver
"""


##------------------------------------------------------------
_AUTHOR    = 'RP'
_VERSION   = '0.5.0'
_COPYRIGHT = '(c) 2024'

_ABOUT = _AUTHOR + '  v' + _VERSION + '   ' + _COPYRIGHT
##------------------------------------------------------------


import socket
import ipaddress
import struct


class UDPReceiver:
    def __init__(self, ip_addr, port, bufsize, diag = False):
        self.bufsize = bufsize

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((ip_addr, port))

        if ipaddress.IPv4Address(ip_addr).is_multicast:
            mreq = struct.pack("4sl", socket.inet_aton(ip_addr), socket.INADDR_ANY)
            self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
            print("Multicast address detected %sn" % (ip_addr))

        if diag:
            print("Receiving on %s:%d\n" % (ip_addr, port))

    def __del__(self):
        self.sock.close()

    def receive(self):
        return self.sock.recvfrom(self.bufsize)

