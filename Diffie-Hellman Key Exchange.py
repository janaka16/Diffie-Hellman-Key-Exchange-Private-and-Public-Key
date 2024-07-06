import random
import hashlib

def generate_prime(low, high):
    prime = random.randint(low, high)
    while not is_prime(prime):
        prime += 1
    return prime

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primitive_root(prime):
    def find_primitive_root(prime, start=2):
        if pow(start, prime - 1, prime) == 1:
            return start
        else:
            return find_primitive_root(prime, start + 1)
    return find_primitive_root(prime)

def compute_shared_key(private_key, public_key, prime):
    return pow(public_key, private_key, prime)

def hash_key(key):
    return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % 10**6

def diffie_hellman_key_exchange():
    prime = generate_prime(100, 1000)
    primitive_root = primitive_root(prime)

    tim_private_key = random.randint(1, prime - 1)
    tim_public_key = pow(primitive_root, tim_private_key, prime)

    stephen_private_key = random.randint(1, prime - 1)
    stephen_public_key = pow(primitive_root, stephen_private_key, prime)

    tim_shared_key = compute_shared_key(tim_private_key, stephen_public_key, prime)
    stephen_shared_key = compute_shared_key(stephen_private_key, tim_public_key, prime)

    print("Tim's shared key (S):", hash_key(tim_shared_key))
    print("Stephen's shared key (S):", hash_key(stephen_shared_key))

    if hash_key(tim_shared_key) == hash_key(stephen_shared_key):
        print("Shared keys are equal! Secure communication established.")
    else:
        print("Shared keys are not equal! Failed to establish secure communication.")

diffie_hellman_key_exchange()
