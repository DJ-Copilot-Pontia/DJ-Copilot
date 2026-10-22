"""
Define los endpoints HTTP relacionados
con las canciones (tracks)
"""

from app.database.mongo import tracks_collection
from app.schemas.track import TrackCreate
from bson import ObjectId
from fastapi import APIRouter, HTTPException

# Agrupa los endpoints relacionados
# con las canciones
tracks_router = APIRouter()

#############################################
#          Endpoints métodos GET            #
#############################################

@tracks_router.get("/tracks")
def get_tracks():

    tracks=[]

    # Find() devuelve todos los docs de la
    # colección tracks
    for track in tracks_collection.find():

        track["id"] = str(track["_id"])
        del track["_id"]
        tracks.append(track)

    return tracks

@tracks_router.get("/tracks/{track_id}")
def get_track(track_id: str):

    # Valida el formato del identificador
    # sin conectar a MongoDB
    if not ObjectId.is_valid(track_id):
        raise HTTPException(
            status_code=404,
            detail="Track not found"
        )

    # Comprueba si el identificador existe
    # en MongoDB
    track = tracks_collection.find_one(
        {"_id": ObjectId(track_id)}
    )

    if track is None:
        raise HTTPException(
            status_code=404,
            detail="Track not found"
        )

    # Prepara la respuesta JSON para cliente.
    # Convierte el ObjectId de MongoDB a texto
    # y elimina el campo _id del diccionario
    track["id"] = str(track["_id"])
    del track["_id"]

    return track

#############################################
#          Endpoints métodos POST           #
#############################################

@tracks_router.post("/tracks")
def create_track(track: TrackCreate):
# track es un objeto validado por Pydantic

    # Convierte el objeto Pydantic en un 
    # diccionario Python. 
    track_data = track.model_dump()

    # Inserta la canción en MongoDB
    result = tracks_collection.insert_one(track_data)

    # Preparar respuesta al usuario. Se añade al 
    # diccionario el id creado por MongoDB al 
    # insertar el documento en la colección.
    track_data["id"] = str(result.inserted_id)
    
    # Las canciones se representan en MongoDB con
    # la siguiente estructura de documento: 
    #  {
    #    _id: ObjectId('6ad4717e831b983e85e17558'),
    #    title: 'nombre',
    #    ...
    #  }
    # FastAPI no puede convertir ObjectId a JSON, 
    # por ser un datatype propio de Mongo. Se 
    # elimina del diccionario de la respuesta.
    del track_data["_id"]

    return track_data

#############################################
#         Endpoints métodos DELETE          #
#############################################

@tracks_router.delete("/tracks/{track_id}")
def delete_track(track_id: str):

    # Valida el formato del identificador
    # sin conectar a MongoDB
    if not ObjectId.is_valid(track_id):
        raise HTTPException(
            status_code=404,
            detail="Track not found"
        )

    # Intenta eliminar el documento aplicando
    # como filtro el _id
    result = tracks_collection.delete_one(
        {"_id": ObjectId(track_id)}
    )

    # Si no se ha eliminado ningún doc, 
    # el identificador no existia
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Track no found"
        )

    return {"message":"Track deleted"}