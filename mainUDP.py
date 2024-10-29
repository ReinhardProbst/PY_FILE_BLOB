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

import udp_receiver
import file_blob


if __name__ == '__main__':
    from optparse import OptionParser

    op = OptionParser(version = '%prog   ' + _ABOUT)

    op.add_option("-a", "--ipaddr",  dest="ipaddr", type="string", help="IP address", default="0.0.0.0")
    op.add_option("-p", "--port",  dest="port", type="int", help="Port", default=12000)
    op.add_option("-c", "--cs",  dest="chunk_size", type="int", help="Chunk size", default=8)
    op.add_option("-n", "--cn",  dest="chunk_numbers", type="int", help="Chunk numbers", default=2)
    op.add_option("-f", "--fbn",  dest="file_base_name", type="string", help="File base name", default="packet_")
    op.add_option("-i", "--fmi",  dest="file_numbers", type="int", help="Max file numbers", default=3)

    (options, args) = op.parse_args()

    # Invalid arguments are given
    if len(args) > 0:
        print(_ABOUT)
        op.print_help()
        op.exit()

    print(f"Arguments: {options.ipaddr} / {options.port} / {options.chunk_size} / {options.chunk_numbers} / {options.file_base_name} / {options.file_numbers}\n")

    udp_recv = udp_receiver.UDPReceiver(options.ipaddr, options.port, options.chunk_size, True)

    fb = file_blob.FileBlob(options.chunk_numbers, options.file_numbers, udp_recv.receive)

    fb.collect()

# Test locally with "cat 8bytes.bin | nc -u -4 -w 1  0.0.0.0 12000"
