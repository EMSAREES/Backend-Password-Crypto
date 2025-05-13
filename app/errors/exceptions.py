class BadRequestException(Exception):
    """Excepción personalizada para errores de solicitud incorrecta"""
    def __init__(self, message="Bad Request"):
        self.message = message
        super().__init__(self.message)
