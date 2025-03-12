import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for c in plaintext:
        if c.isupper():
            base = ord('A')
            shifted = (ord(c) - base + shift) % 26
            ciphertext += chr(base + shifted)
        elif c.islower():
            base = ord('a')
            shifted = (ord(c) - base + shift) % 26
            ciphertext += chr(base + shifted)
        else:
            ciphertext += c
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for c in ciphertext:
        if c.isupper():
            base = ord('A')
            shifted = (ord(c) - base - shift) % 26
            plaintext += chr(base + shifted)
        elif c.islower():
            base = ord('a')
            shifted = (ord(c) - base - shift) % 26
            plaintext += chr(base + shifted)
        else:
            plaintext += c
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    max_count = 0

    for shift in range(26):
        candidate = decrypt_caesar(ciphertext, shift)
        words = candidate.split()
        count = sum(1 for word in words if word in dictionary)

        if count > max_count:
            max_count = count
            best_shift = shift
        elif count == max_count and shift < best_shift:
            best_shift = shift

    return best_shift
