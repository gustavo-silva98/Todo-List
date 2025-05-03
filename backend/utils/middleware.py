from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def add_cors_middleware(app: FastAPI) -> None:
    """
    Adiciona o middleware CORS à aplicação FastAPI.

    Args:
        app: Instância da aplicação FastAPI.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # ou especifique a origem: ["http://localhost:5500"]
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

