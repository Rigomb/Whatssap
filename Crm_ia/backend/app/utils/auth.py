from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

secret_key ="Tu_clave_secreta"
algorithm = "HS256"

def verify_password(password_plano, password_hash):
    return pwd_context.verify(password_plano, password_hash)

def crear_token(data: dict, expires_en_=30):
    datos = data.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=expires_en_min)
    datos.update({"exp": expiracion})
    return jwt.encode(datos, secret_key, algorithm=algorithm)
