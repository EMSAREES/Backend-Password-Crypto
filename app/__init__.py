from flask import Flask, jsonify
from flask_cors import CORS 
from app.routes.crypto_routes import crypto_bp  # Importa las rutas
from app.errors.handlers import register_error_handlers  # Manejo de errores
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)  # Crea la app Flask

    CORS(app)
    
    # Registrar las rutas bajo el prefijo /api
    app.register_blueprint(crypto_bp, url_prefix='/api')

    # Registrar el manejador de errores personalizados
    register_error_handlers(app)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"mensaje": "API funcionando en Flask"})


    return app
