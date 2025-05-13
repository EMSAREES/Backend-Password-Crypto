import os
import secrets
import string
import base64
import hashlib

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def generate_password(length=16, uppercase=True, lowercase=True, numbers=True, symbols=True):
    """Genera una contraseña aleatoria segura según las opciones dadas"""
    charset = ''
    if uppercase:
        charset += string.ascii_uppercase
    if lowercase:
        charset += string.ascii_lowercase
    if numbers:
        charset += string.digits
    if symbols:
        charset += string.punctuation

    if not charset:
        return None  # Si no se eligió ningún tipo de carácter

    # Elige caracteres aleatorios del conjunto permitido
    return ''.join(secrets.choice(charset) for _ in range(length))

def derive_key(master_password):
    """Deriva una clave de 256 bits (32 bytes) usando SHA-256 desde una contraseña"""
    return hashlib.sha256(master_password.encode()).digest()

def encrypt_aes(plaintext, key):
    """Cifra un texto usando AES en modo CBC con padding PKCS7"""
    iv = os.urandom(16)  # Vector de inicialización aleatorio
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Aplicar padding para asegurar múltiplos de 16 bytes
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded) + encryptor.finalize()

    # Devolver texto cifrado junto al IV, codificado en base64
    return base64.b64encode(iv + ciphertext).decode()

def decrypt_aes(encrypted_text, key):
    """Descifra un texto cifrado en AES-CBC"""
    data = base64.b64decode(encrypted_text)
    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Quitar el padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded) + unpadder.finalize()
    return plaintext.decode()
