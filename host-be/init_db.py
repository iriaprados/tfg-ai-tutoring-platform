"""
Script para inicializar la base de datos
Ejecutar: python init_db.py
"""

from app.database.database import engine, Base
from app.database.models import User, Session, ChatMessage

def init_db():
    """Crea todas las tablas en la base de datos"""
    print("Iniciando base de datos...")
    
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    print("✓ Base de datos inicializada correctamente")
    print("✓ Tablas creadas:")
    print("  - users")
    print("  - sessions")
    print("  - chat_messages")
    print("\nArchivo de BD: tutoring_platform.db")

if __name__ == "__main__":
    init_db()
