from app.database.models import Usuario
from app-utils.auth import verify_password , crear_token
from sqlalchemy.orm import Session

def autenticar_usuario(email: str, password: str , db: Session):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return None
    if not verify_password(password, usuario.password):
        return None
        return crear_token("sub":usuario.email)