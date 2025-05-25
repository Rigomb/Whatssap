from app.database.db_session import Base, engine
from app.database import models

print("Creando Tablas...")
Base.metadata.create_all(bind=engine)
print("Listo!")
