from secrets import token_bytes
from typing import Tuple

# generate a random key for use as dummy data
def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert the bytes to bit_string (int) and return it
    return int.from_bytes(tb, 'big') 

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    # print(dummy)
    original_key: int = int.from_bytes(original_bytes, "big")
    # print(original_key)
    encrypted: int = original_key ^ dummy # XOR ops on both dummy and original key
    # print(encrypted)
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("One time Pad!")
    result: str = decrypt(key1, key2)
    print(result)