from fastapi import FastAPI
from app.routes import user, session, chat 

app = FastAPI(
    title="TFG AI Tutoring Platform",
    description="API REST para plataforma de aprendizaje tutorizada por IA",
    version="1.0.0"
)

app.include_router(user.router)
app.include_router(session.router)
app.include_router(chat.router)


@app.get("/")
def root():
    return {"message": "Host-be is running"}