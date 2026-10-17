"""
Define los endpoints HTTP relacionados
con las canciones (tracks)
"""
from fastapi import APIRouter, HTTPException
from app.schemas.track import TrackCreate

# Agrupa los endpoints relacionados
# con las canciones
tracks_router = APIRouter()

# Almacenamiento temporal mientras
# no se conecte a una base de datos
tracks=[]

# Identificador temporal para asignar
# un id único a cada cancion
next_id = 1

#############################################
#          Endpoints métodos GET            #
#############################################

@tracks_router.get("/tracks")
def get_tracks():
    return tracks

@tracks_router.get("/tracks/{track_id}")
def get_track(track_id: int):

    for track in tracks:
        if track["id"] == track_id: 
            return track

    raise HTTPException(
        status_code = 404,
        detail = "Track not found"
    )

#############################################
#          Endpoints métodos POST           #
#############################################

@tracks_router.post("/tracks")
def create_track(track: TrackCreate):
# track es un objeto validado por Pydantic

    global next_id

    # Crea la cancion con un id unico
    new_track = {
        "id": next_id,

        # Convierte y desempaqueta el 
        # diccionario del objeto Pydantic 
        **track.model_dump()
    }
    tracks.append(new_track)
    next_id += 1

    return new_track

#############################################
#         Endpoints métodos DELETE          #
#############################################

@tracks_router.delete("/tracks/{track_id}")
def delete_track(track_id: int):

    for track in tracks: 
        if track["id"] == track_id:
            tracks.remove(track)
            return {"message":"Track deleted"}

    raise HTTPException(
        status_code=404,
        detail="Track not found"
    )