from flask import request, abort
import os
from functools import wraps  # NUEVO: importa wraps

API_KEY = os.getenv("API_KEY")

def require_api_key():
    def decorator(f):
        @wraps(f)  # NUEVO: esto mantiene el nombre original de la función
        def decorated_function(*args, **kwargs):
            key = request.headers.get("x-api-key")
            if not key or key != API_KEY:
                abort(401, description="Unauthorized: Invalid or missing API key")   
            return f(*args, **kwargs)
        return decorated_function
    return decorator
