def encrypt(text: str, key: int):
    result = ""
    for letter in text.lower():
        if (ord(letter) + key) > 122:
            result += chr(ord(letter) + key - 26)
        else:
            result += chr(ord(letter) + key)
    return result


def decrypt(code: str, key: int):
    result = ""
    for letter in code.lower():
        if (ord(letter) - key) < 97:
            result += chr((ord(letter) - key) + 26)
        else:
            result += chr(ord(letter) - key)
    return result
