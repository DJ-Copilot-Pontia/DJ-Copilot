"""
Modelos Pydantic. Definen la estructura
que deben cumplir los datos enviados a 
la API y, cuando corresponde, los datos
que devuelve.
"""

from pydantic import BaseModel

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