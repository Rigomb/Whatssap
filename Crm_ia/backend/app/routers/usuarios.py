from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemes.usuario import UsuarioLogin
from app.services.usuario_service import autenticar_usuario
from app.database.db_session import get_db

router = APIRouter()

@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    token = autenticar_usuario(datos.email, datos.password, db)
    
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"access_token": token, "token_type": "bearer"}
    