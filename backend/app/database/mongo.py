"""
Conexión a la base de datos MongoDB
para persistencia de datos. 

MongoDB trabaja con colecciones y 
documentos JSON/BSON, no con tablas
y columnas. La organización es: 

MongoDB
 |- djcopilot (base de datos)
     |--- tracks (colección)
         |--- canción 1 (documento)
         |--- canción n
"""

from pymongo import MongoClient
from app.core.config import MONGO_URI, MONGO_DB

# Cliente de conexión con MongoDB.
# MONGO_URI identifica el servidor y 
# los parámetros de conexión.
mongo_client = MongoClient(MONGO_URI)

# Base de datos utilizada dentro del
# servidor MongoDB 
database = mongo_client[MONGO_DB]

# Colección donde se almacenan las
# canciones
tracks_collection = database["tracks"]