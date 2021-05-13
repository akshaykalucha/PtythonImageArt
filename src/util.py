import os
import sys
import numpy as np
from PIL import Image
import math

"""

Add custom functions here.

"""


def phi(n):
    original_n = n
    prime_factors = []
    prime_index = 0
    while n > 1: # As long as there are more factors to be found
        p = PRIMES[prime_index]
        if (n % p == 0): # is this prime a factor?
            prime_factors.append(p)
            while math.ceil(n / p) == math.floor(n / p): # as long as we can devide our current number by this factor and it gives back a integer remove it
                n = n // p

        prime_index += 1

    for v in prime_factors: # Now we have the prime factors, we do the same calculation as wikipedia
        original_n *= 1 - (1/v)

    return int(original_n)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2",os.path.abspath("."))

    return os.path.join(base_path, relative_path)

def quick_show(array):
    Image.fromarray(array).transpose(Image.ROTATE_90).show()

def get_blank_array(dimensions):
    return np.zeros(dimensions + (3,), dtype=np.uint8)


def save_array_as_img(f_name, array):
    img = Image.fromarray(array).transpose(Image.ROTATE_90)
    img.save(f_name)


def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


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
        i = i + 6
    return True


# Mandelbrot calculation constants
MAX_ITER = 100
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    return n

import math

MAX = 10**1

# CREDIT TO https://stackoverflow.com/a/18997575/7217653
def sieve_for_primes_to(n): 
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

PRIMES = sieve_for_primes_to(MAX)
print("Primes generated")
