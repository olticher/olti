import math

def is_prime(n):
    """
    Tests to see if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: 
            return False
    return n > 1

def gcd(a, b):
    """
    Euclid's algorithm for determining the greatest common divisor.

    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if a == 0:
        return b
    else:
        return gcd(b %a, a)


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.

    >>> multiplicative_inverse(7, 40)
    23
    """
    number1 = e
    number2 = phi
    x1, x2, y1, y2 = 0, 1, 1, 0
    while e != 0:
        cifra, phi, e = phi // e, e, phi % e
        y1, y2 = y2, y1 - cifra * y2
        x1, x2 = x2, x1 - cifra * x2
    if number1 > number2:
        return y1 % number1
    else:
        return x1 % number2

