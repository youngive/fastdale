def bytes_stream(key):
    stream = bytearray(range(256))
    i = j = 0
    key = [ord(char) for char in key]
    for j in range(256):
        i = (i + stream[j] + key[j % len(key)]) % 256
        stream[j], stream[i] = stream[i], stream[j]

    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (stream[i] + j) % 256
        stream[i], stream[j] = stream[j], stream[i]
        yield stream[(stream[i] + stream[j]) % 256]


def encrypt(text, key):
    text = [ord(char) for char in text]
    bytes_gen = bytes_stream(key)
    return ''.join([f'{char ^ next(bytes_gen):02x}' for char in text])


def decrypt(bytes, key):
    cipher = [char for char in bytes if char != ' ']
    cipher = map(lambda _: int(f"0x{''.join(_)}", 0), zip(*[iter(cipher)] * 2))
    bytes = bytes_stream(key)
    return "".join([chr(char ^ next(bytes)) for char in cipher])