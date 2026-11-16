"""
Modelos Pydantic. Definen la estructura
que deben cumplir los datos enviados a 
la API y, cuando corresponde, los datos
que devuelve.
"""

from pydantic import BaseModel
from typing import Optional, Dict

class TrackCreate(BaseModel):
    """
    Modelo Pydantic que define los datos 
    necesarios para crear una canción 
    mediante una petición POST.
    """
    title: str
    artist: str
    genre: str
    bpm: int


class TrackMetadataCreate(BaseModel):
    id: str
    title: Optional[str] = None
    artist: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
    bpm: Optional[float] = None
    valence: Optional[float] = None
    arousal: Optional[float] = None
    # Diccionario dinámico para las 56 etiquetas de Essentia
    tags_scores: Optional[Dict[str, float]] = None