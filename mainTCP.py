#!/usr/bin/env python3

"""
MAIN

Create file blobs from UDP packets
"""

##------------------------------------------------------------
_AUTHOR    = 'RP'
_VERSION   = '0.5.0'
_COPYRIGHT = '(c) 2024'

_ABOUT = _AUTHOR + '  v' + _VERSION + '   ' + _COPYRIGHT
##------------------------------------------------------------

import tcp_client
import file_blob


if __name__ == '__main__':
    from optparse import OptionParser

    op = OptionParser(version = '%prog   ' + _ABOUT)

    op.add_option("-a", "--ipaddr",  dest="ipaddr", type="string", help="IP address", default="0.0.0.0")
    op.add_option("-p", "--port",  dest="port", type="int", help="Port", default=12000)
    op.add_option("-c", "--cs",  dest="chunk_size", type="int", help="Chunk size", default=8)
    op.add_option("-n", "--cn",  dest="chunk_numbers", type="int", help="Chunk numbers", default=2)
    op.add_option("-f", "--fbn",  dest="file_base_name", type="string", help="File base name", default="packet_")
    op.add_option("-m", "--mfn",  dest="max_file_numbers", type="int", help="Max file numbers", default=3)
    op.add_option("-i", "--ini",  dest="init_str", type="string", help="Init string send", default=b"Try to connect\n")

    (options, args) = op.parse_args()

    # Invalid arguments are given
    if len(args) > 0:
        print(_ABOUT)
        op.print_help()
        op.exit()

    print(f"Arguments: {options.ipaddr} / {options.port} / {options.chunk_size} / {options.chunk_numbers} / {options.file_base_name} / {options.max_file_numbers} / {options.init_str}\n")

    tcp_cl = tcp_client.TCPClient(options.ipaddr, options.port, options.chunk_size, True)

    fb = file_blob.FileBlob(options.chunk_numbers, options.max_file_numbers, tcp_cl.receive)

    tcp_cl.connect(str.encode(options.init_str))
    fb.collect()

# Test locally with "nc -l 12000 < 48bytes.bin"
