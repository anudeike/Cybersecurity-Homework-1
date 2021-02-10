"""
**PART 1**

Person 1: Bob
Person 2: Alice
Person 3: Eve

1. Bob and Alice decide on a prime modulus and a generator (publicly)

g = 3
p_m = 17

2. ALice selects a private random number (n = 15) and calculates 3 ** 15 mod 17 = 6

Alice sends 6 publicly to Bob

2. Bob selects a private random number (n = 13) and calculates 3 ** 13 mod 17 = 6

Bob sends 12 publicly to Alice

3. ALice takes the public result and raises and does the following:

(12 is Bob's result)

12 ** 15 mod 17 = 10

4. Bob takes Alice's public result and raises it and does the following:

(6 ** 13) mod 17 = 10 (should get the same result)

they can now use 10 and a key to encrypt and decrypt messages.
"""
import numpy as np 

#np.random.seed(0)

prime_modulus = 17
generator = 3

# 44
alice_random = np.random.randint(100)

# 15
bob_random = np.random.randint(100)

# to send to Bob
alice_public_result = (generator ** alice_random) % prime_modulus
print(f'Alice Public Result: {alice_public_result}')

# to send to Alice
bob_public_result = (generator ** bob_random) % prime_modulus

print(f'Bob Public Result: {alice_public_result}')

# alice using the generator from bob
shared_key_alice = (bob_public_result ** alice_random) % prime_modulus

shared_key_bob = (alice_public_result ** bob_random) % prime_modulus

# works!
print(f'Shared Key From Alice: {shared_key_alice}')

print(f'Shared Key From Bob: {shared_key_bob}')