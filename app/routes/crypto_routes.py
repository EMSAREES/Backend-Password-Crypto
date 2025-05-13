from flask import Blueprint, request, jsonify
from app.services.crypto_service import CryptoService
from app.errors.exceptions import BadRequestException
from app.utils.auth_utils import require_api_key

# Creamos un Blueprint (una mini app para agrupar rutas)
crypto_bp = Blueprint('crypto', __name__)

@crypto_bp.route('/generate-password', methods=['POST'])
@require_api_key()
def generate_password():
    try:
        # Obtenemos los datos del cuerpo de la solicitud (JSON)
        data = request.get_json()

        # Llamamos al servicio que genera contraseñas
        password = CryptoService.generate_password(data)
        return jsonify({"password": password})  # Retornamos JSON con la contraseña
    except Exception as e:
        raise BadRequestException(str(e))  

@crypto_bp.route('/encrypt', methods=['POST'])
@require_api_key()
def encrypt():
    try:
        data = request.get_json()
        result = CryptoService.encrypt_text(data)
        return jsonify({"encrypted": result})  # Retornamos el texto cifrado
    except Exception as e:
        raise BadRequestException(str(e))

@crypto_bp.route('/decrypt', methods=['POST'])
@require_api_key()
def decrypt():
    try:
        data = request.get_json()
        result = CryptoService.decrypt_text(data)
        return jsonify({"decrypted": result})  # Retornamos el texto descifrado
    except Exception as e:
        raise BadRequestException(str(e))
