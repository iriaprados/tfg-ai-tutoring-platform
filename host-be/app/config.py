import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de la aplicación
class Settings:
    APP_NAME = "TFG AI Tutoring Platform"
    APP_VERSION = "1.0.0"
    
    # Base de datos
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tutoring_platform.db")
    
    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    # Redis (opcional)
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

settings = Settings()
