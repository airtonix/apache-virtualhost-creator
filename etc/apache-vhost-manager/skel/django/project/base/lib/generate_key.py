from hashlib import md5, sha1
from base64 import urlsafe_b64encode as b64encode

import random
random.seed()


def random_string():
    """
    Generate a random string (currently a random number as a string)
    """
    return str(random.randint(0,100000))

def generate_key(max_length, data, encoder=b64encode, digester=md5):
    """
    Generate a Base64-encoded 'random' key by hashing the data.
    data is a tuple of seeding values. Pass arbitrary encoder and
    digester for specific hashing and formatting of keys
    """
    base = ''
    for arg in data:
        base += str(arg)
    key = encoder(digester(base).digest())
    return key[:max_length]

