from app.utils.crypto_utils import (
    generate_password as gen_pwd,
    derive_key,
    encrypt_aes,
    decrypt_aes
)

class CryptoService:
    @staticmethod
    def generate_password(data):
        # Extrae opciones desde los datos del usuario
        length = int(data.get('length', 16))
        return gen_pwd(
            length=length,
            uppercase=data.get('uppercase', True),
            lowercase=data.get('lowercase', True),
            numbers=data.get('numbers', True),
            symbols=data.get('symbols', True)
        )

    @staticmethod
    def encrypt_text(data):
        master_password = data['master_password']
        text = data['text']
        key = derive_key(master_password)  # Deriva clave AES desde la contraseña
        return encrypt_aes(text, key)

    @staticmethod
    def decrypt_text(data):
        master_password = data['master_password']
        encrypted_text = data['text']
        key = derive_key(master_password)
        return decrypt_aes(encrypted_text, key)
