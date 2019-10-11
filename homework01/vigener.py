def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    ciphertext = ""
    for j in plaintext:
        if not j.isalpha():
            ciphertext += j
    if len(plaintext) > len(keyword):
        keyword += keyword*((len(plaintext) // len(keyword))-1)
        keyword += keyword[:(len(plaintext) % len(keyword))]
    number = 0
    for char in plaintext:
        if keyword[number].isupper():
            value = ord(keyword[number])-65
        else:
            value = ord(keyword[number])-97
        if char.isupper():
            ciphertext += chr((ord(char) + value - ord('A')) % 26 + ord('A'))
        else:
            ciphertext += chr((ord(char) + value - ord('a')) % 26 + ord('a'))
        number += 1
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    plaintext = ''
    for j in ciphertext:
        if not j.isalpha():
            plaintext += j
    if len(ciphertext) > len(keyword):
        keyword += keyword*((len(ciphertext) // len(keyword)) - 1)
        keyword += keyword[:(len(ciphertext) % len(keyword))]
    number = 0
    for char in ciphertext:
        if keyword[number].isupper():
            value = ord(keyword[number]) - 65
        elif keyword[number].islower():
            value = ord(keyword[number]) - 97
        if char.isupper():
            plaintext += chr((ord(char) - value - ord('A')) % 26 + ord('A'))
        elif char.islower():
            plaintext += chr((ord(char) - value - ord('a')) % 26 + ord('a'))
        number += 1

    return plaintext