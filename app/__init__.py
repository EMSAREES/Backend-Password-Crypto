from flask import Flask
from app.routes.crypto_routes import crypto_bp  # Importa las rutas
from app.errors.handlers import register_error_handlers  # Manejo de errores

def create_app():
    app = Flask(__name__)  # Crea la app Flask

    # Registrar las rutas bajo el prefijo /api
    app.register_blueprint(crypto_bp, url_prefix='/api')

    # Registrar el manejador de errores personalizados
    register_error_handlers(app)

    return app
