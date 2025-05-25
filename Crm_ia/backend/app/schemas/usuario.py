from pydantic import basemodel

class UsuarioLogin(basemodel):
    email: str
    password: str