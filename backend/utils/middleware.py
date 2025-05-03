from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
import time 
import logging

logger = logging.getLogger("backend.middleware")


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

class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, request: Request, call_next):
        start = time.time()
        logger.info(f"->  {request.method} {request.url.path}")
        
        response: Response = await call_next(request)
        
        process_time = (time.time() - start) * 1000
        logger.info(
            f"<- {request.method} {request.url.path} "
            f"completed_in={process_time:.2f}ms status_code={response.status_code}"
        )
        return response