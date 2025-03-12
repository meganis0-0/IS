def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_shifts = []
    for char in keyword:
        if char.isupper():
            shift = ord(char) - ord('A')
        else:
            shift = ord(char) - ord('a')
        keyword_shifts.append(shift)
    
    keyword_len = len(keyword_shifts)
    if keyword_len == 0:
        return plaintext
    
    keyword_idx = 0
    for c in plaintext:
        if c.isalpha():
            shift = keyword_shifts[keyword_idx % keyword_len]
            keyword_idx += 1
            if c.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = (ord(c) - base + shift) % 26
            ciphertext += chr(base + shifted)
        else:
            ciphertext += c
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_shifts = []
    for char in keyword:
        if char.isupper():
            shift = ord(char) - ord('A')
        else:
            shift = ord(char) - ord('a')
        keyword_shifts.append(shift)
    
    keyword_len = len(keyword_shifts)
    if keyword_len == 0:
        return ciphertext
    
    keyword_idx = 0
    for c in ciphertext:
        if c.isalpha():
            shift = keyword_shifts[keyword_idx % keyword_len]
            keyword_idx += 1
            if c.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = (ord(c) - base - shift) % 26
            plaintext += chr(base + shifted)
        else:
            plaintext += c
    return plaintext
