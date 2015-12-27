import random
 
 
def generate_hash(bits=96):
    assert bits % 8 == 0
    required_length = bits / 8 * 2
    s = hex(random.getrandbits(bits)).lstrip('0x').rstrip('L')
    if len(s) < required_length:
        return my_hash(bits)
    else:
        return s


def client_access_token_valid():
    return True
 
 

 
