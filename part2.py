"""
** PART 2 **

1. Pick 2 Prime Numbers
ie: p = 2, q = 7

2. Find the modulus number or Big N 
N = p * q = 2 * 7 = 14
N = 14

3. Find phi(N) = (p-1)(q-1)
This number gives the amount of numbers that are coprime to N 
phi(14) = 6

4. Find the encryption number e, given the following
- e must be greater than 1 and less that phi(N)
- e number be coprime with N an phi(N)
- e = 5 (in this case)

5. Find the decrpytion number
- choose d such that de(mod phi(N)) = 1
- ie 5 * d(mod 6) = 1
- we can choose d = 11


"""
import re
import numpy as np

# not purely my own code, was following a tutorial on stackoverflow
def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

# for getting a single number 
def get_prime_number(high, low):
  primes = [x for x in range(high, low) if isprime(x)]
  return primes[-1]

# for getting ranges
def get_prime_number_range(high, low):
  primes = [x for x in range(high, low) if isprime(x)]
  return primes

def phi(p, q):
  return (p - 1) * (q - 1)

def compute_encryption_number(phi_N, N):
  # 1 < e < phi_N
  # if it is prime then it must necessarily be prime with both numbers
  # (that is not necessarily true --> but it might work)
  valid_range = get_prime_number_range(1, phi_N)
  return valid_range[-1]

def compute_decryption_number(e, phi_N):
  # since e * n (mod phi_N) = 1
  # simply pick a random number = n, and multiply by e, then subtract 1

  # can be a random number
  n = np.random.randint(100)

  d = (phi_N * n) - 1


  # verify that it works
  one = (e * d) % phi_N

  # its can't work if it doesn't have the criteria
  if one != 1:
    raise ValueError("This decryption value will not work.")

  return d

# first step is to pick two prime numbers
p = 2
q = 7

# find the modulus number
N = p * q

# find phi_N
phi_N = phi(p, q)

# should get 5 for the example
e = compute_encryption_number(phi_N, N)
d = compute_decryption_number(e, phi_N)

# set the keys
public_lock = (e, N)
private_keys = (d, N)

print(f'public_lock: {public_lock}')
print(f'private_key: {private_keys}')

# checking encryption and decryption
message = "Hi! Cybersecurity is fun, especially all of the modular arthmetic!"








