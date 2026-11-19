from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.dialects.postgresql import JSONB
from .postgres import Base

class TrackMetadata(Base):
    __tablename__ = "tracks_metadata"

    # Clave Primaria
    id = Column(String, primary_key=True, index=True)
    
    # Metadatos básicos
    title = Column(String, index=True, nullable=True)
    artist = Column(String, index=True, nullable=True)
    year = Column(Integer, nullable=True)
    genre = Column(String, index=True, nullable=True)
    
    # Características musicales extraídas por Essentia
    bpm = Column(Float, nullable=True)
    
    # Valores continuos (emoción y energía)
    valence = Column(Float, nullable=True)
    arousal = Column(Float, nullable=True)
    
    # Diccionario con las puntuaciones de las 56 categorías (mood/theme)
    # Ejemplo: {"happy": 0.8, "energetic": 0.9, "party": 0.7}
    tags_scores = Column(JSONB, nullable=True)