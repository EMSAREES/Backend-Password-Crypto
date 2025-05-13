from flask import jsonify
from app.errors.exceptions import BadRequestException

def register_error_handlers(app):
    @app.errorhandler(BadRequestException)
    def handle_bad_request(e):
        # Devuelve error 400 con mensaje personalizado
        return jsonify({"error": e.message}), 400

    @app.errorhandler(Exception)
    def handle_generic_error(e):
        # Para cualquier otro error no manejado
        return jsonify({"error": str(e)}), 500
