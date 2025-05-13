from app import create_app  # Importa la función que crea la app Flask

app = create_app()  # Crea la instancia de la aplicación

if __name__ == "__main__":
    # Ejecuta la app en modo desarrollo (con recarga automática y errores detallados)
    app.run(debug=True)
