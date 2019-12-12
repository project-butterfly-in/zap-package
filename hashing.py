import hashlib
from sys import argv, platform

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def md5sum(file_address):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    md5 = hashlib.md5()

    with open(file_address, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def sha1sum(file_address):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    sha1 = hashlib.sha1()
    with open(file_address, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

if __name__ == "__main__":
    sumtype = argv[1].lower()
    file_address = argv[2]
    if sumtype == "sha1sum":
        result = sha1sum(file_address)
    elif sumtype == "md5sum":
        result = md5sum(file_address)
    elif sumtype == "sha256sum":
        result = sha256sum(file_address)
    else:
        print("Incorrect arguments!")
        print("Available options:\n\t1.{}\n\t2.{}\n\t3.{}".format("sha1sum","md5sum","sha256sum"))
        exit()
    print("{1}: {0}".format(result, sumtype.upper()))

