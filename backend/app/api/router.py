"""
Agrupa y registra los routers de la API
"""

from fastapi import APIRouter
from app.api.endpoints.tracks import tracks_router

# Router principal de la API. Agrupa
# los distintos grupos de endpoints
api_router = APIRouter()

# Registra los endpoints relacionados 
# con las canciones
api_router.include_router(tracks_router)