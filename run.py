import os
from app import create_app  #
from dotenv import load_dotenv

load_dotenv()

app = create_app()  # Crea la instancia de la aplicación

if __name__ == "__main__":
    # Ejecuta la app en modo desarrollo (con recarga automática y errores detallados)
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", 5000))
