"""
Create file blobs from a receiver function

Create file blobs from a receiver function
"""


##------------------------------------------------------------
_AUTHOR    = 'RP'
_VERSION   = '0.5.0'
_COPYRIGHT = '(c) 2024'

_ABOUT = _AUTHOR + '  v' + _VERSION + '   ' + _COPYRIGHT
##------------------------------------------------------------


class FileBlob:
    def __init__(self, chunk_numbers = 100, file_numbers = 10, recv = None, base_name = "packet"):
        self.base_name = base_name
        self.chunk_numbers = chunk_numbers
        self.file_numbers = file_numbers
        self.recv = recv

    def collect(self):
        idx = 0

        while idx < self.file_numbers:
            data = []
            chunk_act = 0

            while chunk_act < self.chunk_numbers:
                chunk_data = self.recv()
                data.append(chunk_data)
                chunk_act += 1

            fno = "{:04}".format(idx)
            with open(self.base_name + fno + ".bin", 'wb') as f:
                f.write(b''.join(data))
                print(f"Created: {self.base_name}{fno}.bin\n")

            idx += 1
